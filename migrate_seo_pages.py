#!/usr/bin/env python3
"""
Moves the 24 SEO blog posts from /[service]-new-jersey/[slug]/
into /seo-pages/[slug]/, fixes breadcrumbs inside each post,
and updates service page links to the new location.
"""

import os, shutil, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# blog slug → (parent_service_dir, parent_label)
BLOG_POSTS = {
    "cheap-drywall-repair-new-jersey-cost-guide":      ("drywall-repair-new-jersey",       "Drywall Repair in NJ"),
    "drywall-repair-mistakes-new-jersey":              ("drywall-repair-new-jersey",       "Drywall Repair in NJ"),
    "wall-damage-types-new-jersey-homes":              ("drywall-repair-new-jersey",       "Drywall Repair in NJ"),
    "garage-door-opener-security-new-jersey":          ("garage-door-repair-new-jersey",   "Garage Door Repair in NJ"),
    "garage-door-repair-cost-new-jersey":              ("garage-door-repair-new-jersey",   "Garage Door Repair in NJ"),
    "garage-door-warning-signs-new-jersey":            ("garage-door-repair-new-jersey",   "Garage Door Repair in NJ"),
    "furniture-assembly-time-new-jersey":              ("furniture-assembly-new-jersey",   "Furniture Assembly in NJ"),
    "heavy-furniture-safety-new-jersey":               ("furniture-assembly-new-jersey",   "Furniture Assembly in NJ"),
    "ikea-assembly-mistakes-new-jersey":               ("furniture-assembly-new-jersey",   "Furniture Assembly in NJ"),
    "best-interior-paint-new-jersey":                  ("painting-new-jersey",             "Painting in NJ"),
    "painting-contractor-shortcuts-new-jersey":        ("painting-new-jersey",             "Painting in NJ"),
    "painting-prep-mistakes-new-jersey":               ("painting-new-jersey",             "Painting in NJ"),
    "door-lock-safety-new-jersey":                     ("door-repair-new-jersey",          "Door Repair in NJ"),
    "door-repair-problems-new-jersey":                 ("door-repair-new-jersey",          "Door Repair in NJ"),
    "door-security-new-jersey-homeowners":             ("door-repair-new-jersey",          "Door Repair in NJ"),
    "chimney-inspection-new-jersey-fire-risk":         ("chimney-masonry-new-jersey",      "Chimney & Masonry in NJ"),
    "chimney-maintenance-cost-new-jersey":             ("chimney-masonry-new-jersey",      "Chimney & Masonry in NJ"),
    "masonry-problems-new-jersey-winter":              ("chimney-masonry-new-jersey",      "Chimney & Masonry in NJ"),
    "electrical-outlet-safety-new-jersey":             ("electrical-repair-new-jersey",    "Electrical Repair in NJ"),
    "electrical-repair-cost-new-jersey":               ("electrical-repair-new-jersey",    "Electrical Repair in NJ"),
    "smart-switch-review-new-jersey":                  ("electrical-repair-new-jersey",    "Electrical Repair in NJ"),
    "faucet-leaks-new-jersey-guide":                   ("plumbing-repair-new-jersey",      "Plumbing Repair in NJ"),
    "plumbing-cost-new-jersey-homeowner-guide":        ("plumbing-repair-new-jersey",      "Plumbing Repair in NJ"),
    "under-sink-plumbing-new-jersey-risks":            ("plumbing-repair-new-jersey",      "Plumbing Repair in NJ"),
}

seo_dir = os.path.join(ROOT, "seo-pages")
os.makedirs(seo_dir, exist_ok=True)

moved = 0
for slug, (parent_dir, parent_label) in BLOG_POSTS.items():
    src = os.path.join(ROOT, parent_dir, slug)
    dst = os.path.join(seo_dir, slug)
    if not os.path.exists(src):
        print(f"  ⚠  skipping {slug} (not found at {src})")
        continue

    # Copy to new location (keep original until service pages are updated)
    shutil.copytree(src, dst, dirs_exist_ok=True)

    # Fix breadcrumb inside the copied index.html
    page = os.path.join(dst, "index.html")
    with open(page) as f:
        content = f.read()

    # Replace breadcrumb parent link: <a href="../"> → <a href="../../[parent_dir]/">
    content = content.replace(
        '<a href="../">',
        f'<a href="../../{parent_dir}/">'
    )

    with open(page, "w") as f:
        f.write(content)

    moved += 1

print(f"  ✓  {moved} blog posts copied to seo-pages/")

# ── Update service page links ─────────────────────────────────────────────────
# Each service page currently has links like:
#   href="cheap-drywall-repair-new-jersey-cost-guide/"
# These must become:
#   href="../seo-pages/cheap-drywall-repair-new-jersey-cost-guide/"

service_dirs = set(v[0] for v in BLOG_POSTS.values())
patched_svc = 0
for svc_dir in service_dirs:
    page = os.path.join(ROOT, svc_dir, "index.html")
    if not os.path.exists(page):
        continue
    with open(page) as f:
        content = f.read()
    new_content = content
    for slug, (pd, _) in BLOG_POSTS.items():
        if pd == svc_dir:
            # relative same-dir link → relative up-and-over to seo-pages
            new_content = new_content.replace(
                f'href="{slug}/"',
                f'href="../seo-pages/{slug}/"'
            )
    if new_content != content:
        with open(page, "w") as f:
            f.write(new_content)
        patched_svc += 1

print(f"  ✓  {patched_svc} service pages updated with new blog post paths")

# ── Remove original blog post dirs ────────────────────────────────────────────
removed = 0
for slug, (parent_dir, _) in BLOG_POSTS.items():
    old_path = os.path.join(ROOT, parent_dir, slug)
    if os.path.exists(old_path):
        shutil.rmtree(old_path)
        removed += 1

print(f"  ✓  {removed} original blog post directories removed")
print("\nDone.")
