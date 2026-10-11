#!/usr/bin/env python3
"""Weekly Google Search Console "striking distance" report for thefixwizard.com.

Pulls the previous 7 days of search performance and lists queries that earn
plenty of impressions but few clicks while ranking in positions 6-20 — the
queries closest to page one / the top five, where improving the ranking page
pays off fastest.

Runs every Sunday night via .github/workflows/gsc-weekly-report.yml, or locally:
    pip install -r scripts/requirements.txt
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
    python3 scripts/gsc_weekly_report.py
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
DEFAULT_SITE = "sc-domain:thefixwizard.com"
REPORT_DIR = Path(__file__).resolve().parent.parent / "reports" / "gsc"
ROW_LIMIT = 25000  # API maximum per request


def parse_args():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--site", default=os.environ.get("GSC_SITE_URL") or DEFAULT_SITE,
                   help="GSC property, e.g. sc-domain:thefixwizard.com or https://thefixwizard.com/")
    p.add_argument("--end-date", type=date.fromisoformat,
                   help="last day of the 7-day window, YYYY-MM-DD (default: yesterday, US Eastern)")
    p.add_argument("--min-impressions", type=int, default=50,
                   help="minimum impressions over the week (default: 50)")
    p.add_argument("--max-ctr", type=float, default=0.03,
                   help="CTR at or below this counts as mediocre clicks (default: 0.03 = 3%%)")
    p.add_argument("--min-position", type=float, default=6)
    p.add_argument("--max-position", type=float, default=20)
    return p.parse_args()


def get_credentials():
    raw = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
    if raw:  # CI passes the key JSON itself as a secret
        return service_account.Credentials.from_service_account_info(json.loads(raw), scopes=SCOPES)
    key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not key_path:
        raise SystemExit("Set GSC_SERVICE_ACCOUNT_JSON (key contents) or "
                         "GOOGLE_APPLICATION_CREDENTIALS (path to the key file).")
    return service_account.Credentials.from_service_account_file(key_path, scopes=SCOPES)


def fetch_rows(service, site, start, end, dimensions):
    rows, start_row = [], 0
    while True:
        resp = service.searchanalytics().query(siteUrl=site, body={
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "dimensions": dimensions,
            "rowLimit": ROW_LIMIT,
            "startRow": start_row,
            # The last ~2 days are still "preliminary" in GSC; the default
            # "final" state would return nothing for them.
            "dataState": "all",
        }).execute()
        batch = resp.get("rows", [])
        rows.extend(batch)
        if len(batch) < ROW_LIMIT:
            return rows
        start_row += ROW_LIMIT


def find_opportunities(query_rows, page_rows, min_impressions, max_ctr, min_pos, max_pos):
    # The ranking page for a query = the page that earned the most impressions for it.
    top_page = {}
    for r in page_rows:
        query, page = r["keys"]
        if r["impressions"] > top_page.get(query, ("", -1))[1]:
            top_page[query] = (page, r["impressions"])

    picks = [
        {
            "query": r["keys"][0],
            "page": top_page.get(r["keys"][0], ("", 0))[0],
            "impressions": int(r["impressions"]),
            "clicks": int(r["clicks"]),
            "ctr": r["ctr"],
            "position": r["position"],
        }
        for r in query_rows
        if r["impressions"] >= min_impressions
        and r["ctr"] <= max_ctr
        and min_pos <= r["position"] <= max_pos
    ]
    return sorted(picks, key=lambda x: x["impressions"], reverse=True)


def write_reports(opps, start, end, args):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stem = REPORT_DIR / f"{end.isoformat()}_striking-distance"

    with open(f"{stem}.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["query", "page", "impressions", "clicks", "ctr", "position"])
        writer.writeheader()
        for o in opps:
            writer.writerow({**o, "ctr": round(o["ctr"], 4), "position": round(o["position"], 1)})

    lines = [
        f"## GSC striking-distance queries: {start} to {end}",
        "",
        f"Property `{args.site}` · positions {args.min_position:g}-{args.max_position:g} · "
        f"at least {args.min_impressions} impressions · CTR at or below {args.max_ctr:.1%}",
        "",
        f"**{len(opps)} queries found.**",
        "",
    ]
    if opps:
        lines += ["| Query | Ranking page | Impr. | Clicks | CTR | Pos. |",
                  "|---|---|---:|---:|---:|---:|"]
        for o in opps:
            query = o["query"].replace("|", "\\|")
            lines.append(f"| {query} | {o['page']} | {o['impressions']} | {o['clicks']} | "
                         f"{o['ctr']:.1%} | {o['position']:.1f} |")
    markdown = "\n".join(lines) + "\n"
    Path(f"{stem}.md").write_text(markdown)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")  # shows the table on the Actions run page
    if summary:
        with open(summary, "a") as f:
            f.write(markdown)
    return markdown, stem


def main():
    args = parse_args()
    end = args.end_date or datetime.now(ZoneInfo("America/New_York")).date() - timedelta(days=1)
    start = end - timedelta(days=6)

    service = build("searchconsole", "v1", credentials=get_credentials(), cache_discovery=False)
    query_rows = fetch_rows(service, args.site, start, end, ["query"])
    page_rows = fetch_rows(service, args.site, start, end, ["query", "page"])

    opps = find_opportunities(query_rows, page_rows, args.min_impressions, args.max_ctr,
                              args.min_position, args.max_position)
    markdown, stem = write_reports(opps, start, end, args)
    print(markdown)
    print(f"Saved {stem}.csv and {stem}.md")


if __name__ == "__main__":
    main()
