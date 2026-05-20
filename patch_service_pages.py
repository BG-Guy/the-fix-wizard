#!/usr/bin/env python3
"""
Patches chimney-masonry-new-jersey and handyman-services-new-jersey:
  1. Updates H1 title to "X Services in New Jersey"
  2. Replaces sp-work-section grid with bubble display + search
  3. Creates Cleveland equivalents

Run: python3 patch_service_pages.py
"""

import os, re
from services_data import (
    CHIMNEY_CATS as SD_CHIMNEY_CATS, HANDYMAN_CATS as SD_HANDYMAN_CATS,
    CHIMNEY_SERVICES_FULL, HANDYMAN_SERVICES_FULL, build_service_lookup
)

def _build_cats(sd_cats, svc_full):
    lookup = build_service_lookup(svc_full)
    return [(cat_name, cat_icon, [(lookup[s][0], lookup[s][1], s) for s in slugs if s in lookup])
            for cat_name, cat_icon, slugs in sd_cats]

CHIMNEY_CATS  = _build_cats(SD_CHIMNEY_CATS,  CHIMNEY_SERVICES_FULL)
HANDYMAN_CATS = _build_cats(SD_HANDYMAN_CATS, HANDYMAN_SERVICES_FULL)

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Bubble CSS / JS (same as generate_service_hubs.py) ───────────────────────

BUBBLE_CSS = """
<style id="bubble-styles">
@keyframes bubble-float {
  0%,100% { transform: translateY(0px); }
  50%      { transform: translateY(-6px); }
}
.svc-bubble {
  display: inline-flex; align-items: center; gap: 8px;
  background: #fff; border: 2px solid #e8edf5; border-radius: 100px;
  padding: 10px 18px 10px 13px; font-size: 13.5px; font-weight: 500;
  color: #1e2d5a; cursor: pointer; user-select: none;
  animation: bubble-float var(--dur,3.8s) ease-in-out var(--delay,0s) infinite;
  transition: transform .28s cubic-bezier(.34,1.56,.64,1),
              opacity .2s ease, border-color .15s ease,
              box-shadow .15s ease, background .15s ease;
  will-change: transform, opacity;
}
.svc-bubble:hover {
  border-color: #FF6B35; background: #fff7f4;
  box-shadow: 0 8px 24px rgba(255,107,53,.18);
  animation-play-state: paused;
  transform: translateY(-4px) scale(1.05) !important;
}
.svc-bubble.b-hide {
  transform: scale(0) !important; opacity: 0 !important;
  pointer-events: none; animation: none !important;
}
.svc-bubble .b-icon { font-size: 11px; color: #FF6B35; flex-shrink: 0; }
.svc-category.c-hide { display: none; }
.bubbles-row { display: flex; flex-wrap: wrap; gap: 10px; }
.cat-hdr { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.cat-hdr-icon {
  width: 30px; height: 30px; background: rgba(255,107,53,.1);
  border-radius: 9px; display: flex; align-items: center;
  justify-content: center; flex-shrink: 0;
}
.cat-hdr-icon i { color: #FF6B35; font-size: 12px; }
.cat-hdr-label {
  font-size: 11px; font-weight: 800; color: #0d1b4b;
  text-transform: uppercase; letter-spacing: .1em; white-space: nowrap;
}
.cat-hdr-line { flex: 1; height: 1px; background: #eef1f7; }
.srch-wrap { position: relative; display: flex; align-items: center; }
.srch-icon { position: absolute; left: 17px; color: #94a3b8; font-size: 15px; pointer-events: none; }
.srch-input {
  width: 100%; padding: 15px 50px 15px 46px;
  border: 2px solid #e2e8f0; border-radius: 18px;
  font-size: 15px; font-weight: 500; color: #0d1b4b;
  font-family: Inter, sans-serif; outline: none; background: #fff;
  transition: border-color .2s, box-shadow .2s;
}
.srch-input:focus { border-color: #FF6B35; box-shadow: 0 0 0 4px rgba(255,107,53,.1); }
.srch-input::placeholder { color: #94a3b8; }
.srch-clear {
  position: absolute; right: 16px; width: 26px; height: 26px;
  background: #f1f5f9; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #64748b; font-size: 11px; cursor: pointer;
  opacity: 0; pointer-events: none; transition: opacity .15s, background .15s;
}
.srch-clear.show { opacity: 1; pointer-events: all; }
.srch-clear:hover { background: #FF6B35; color: #fff; }
.srch-hint { text-align: center; font-size: 13px; color: #94a3b8; margin-top: 10px; min-height: 18px; }
.srch-none { text-align: center; font-size: 15px; color: #64748b; padding: 40px 0; display: none; }
.srch-none button { color: #FF6B35; font-weight: 600; background: none; border: none; cursor: pointer; margin-left: 4px; }
</style>"""

BUBBLE_JS = """
<script id="bubble-search">
(function() {
  var inp  = document.getElementById('srch');
  var clr  = document.getElementById('srch-clr');
  var hint = document.getElementById('srch-hint');
  var none = document.getElementById('srch-none');
  var bubbles = document.querySelectorAll('.svc-bubble');
  var cats    = document.querySelectorAll('.svc-category');
  if (!inp) return;
  function run(q) {
    q = q.toLowerCase().trim();
    var shown = 0;
    bubbles.forEach(function(b) {
      var match = !q || b.dataset.s.includes(q);
      b.classList.toggle('b-hide', !match);
      if (match) shown++;
    });
    cats.forEach(function(c) {
      var any = Array.from(c.querySelectorAll('.svc-bubble')).some(function(b) { return !b.classList.contains('b-hide'); });
      c.classList.toggle('c-hide', !any);
    });
    clr.classList.toggle('show', q.length > 0);
    hint.textContent = q ? (shown + ' service' + (shown !== 1 ? 's' : '') + ' found') : '';
    none.style.display = (q && shown === 0) ? 'block' : 'none';
  }
  inp.addEventListener('input', function() { run(inp.value); });
  clr.addEventListener('click', function() { inp.value = ''; run(''); inp.focus(); });
  document.getElementById('srch-none-clr').addEventListener('click', function() { inp.value = ''; run(''); inp.focus(); });
})();
</script>"""

DURATIONS = [3.6, 4.1, 3.9, 4.4, 3.7, 4.2, 3.8, 4.5]
DELAYS    = [0, 0.4, 0.8, 1.2, 0.2, 0.6, 1.0, 1.4]

def bubble_section_html(cats, location_name, loc_slug="new-jersey", loc_url="new-jersey"):
    total = sum(len(items) for _, _, items in cats)
    idx = 0
    cats_html = ""
    for cat_name, cat_icon, items in cats:
        bubbles_html = ""
        for item in items:
            icon, name = item[0], item[1]
            slug = item[2] if len(item) > 2 else None
            dur   = DURATIONS[idx % len(DURATIONS)]
            delay = DELAYS[idx % len(DELAYS)]
            s_key = name.lower().replace("&amp;", "and").replace("/", " ").replace("(","").replace(")","")
            href  = f'../{slug}/' if slug else '#'
            bubbles_html += f'\n                    <a class="svc-bubble" href="{href}" data-s="{s_key}" style="--dur:{dur}s;--delay:{delay}s"><i class="fas {icon} b-icon"></i><span>{name}</span></a>'
            idx += 1
        cats_html += f"""
            <div class="svc-category">
                <div class="cat-hdr">
                    <div class="cat-hdr-icon"><i class="fas {cat_icon}"></i></div>
                    <span class="cat-hdr-label">{cat_name}</span>
                    <div class="cat-hdr-line"></div>
                </div>
                <div class="bubbles-row">{bubbles_html}
                </div>
            </div>"""

    return f"""    <section class="sp-work-section services">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Services</span>
                <h2 class="section-title">Every Service We <span class="text-accent">Offer in {location_name}</span></h2>
                <p class="section-desc">All {total} services — search to find yours instantly. Same-day available, free estimates.</p>
            </div>

            <div class="max-w-[580px] mx-auto mb-12 reveal">
                <div class="srch-wrap">
                    <i class="fas fa-search srch-icon"></i>
                    <input id="srch" type="text" class="srch-input" placeholder="Search services…" autocomplete="off" spellcheck="false">
                    <div id="srch-clr" class="srch-clear" role="button" aria-label="Clear search"><i class="fas fa-times"></i></div>
                </div>
                <p id="srch-hint" class="srch-hint"></p>
            </div>

            <div class="flex flex-col gap-10 max-w-[960px] mx-auto">
{cats_html}
            </div>
            <div id="srch-none" class="srch-none">No services match your search.<button id="srch-none-clr">Clear search</button></div>
        </div>
    </section>
"""


# ── Patch function ────────────────────────────────────────────────────────────

def patch_page(path, old_h1, new_h1, cats, location_name, loc_slug="new-jersey", loc_url="new-jersey"):
    with open(path) as f:
        html = f.read()

    # 1. Update H1
    html = html.replace(old_h1, new_h1)

    # 2. Replace sp-work-section with bubble section
    start_tag = '    <section class="sp-work-section services">'
    end_tag   = '    <section class="sp-process-section">'
    start_idx = html.find(start_tag)
    end_idx   = html.find(end_tag)
    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + bubble_section_html(cats, location_name, loc_slug, loc_url) + '\n    ' + html[end_idx:]

    # 3. Inject/replace BUBBLE_CSS (always update so CSS changes propagate)
    import re as _re
    html = _re.sub(r'<style id="bubble-styles">.*?</style>', '', html, flags=_re.DOTALL)
    html = html.replace('</head>', BUBBLE_CSS + '\n</head>', 1)

    # 4. Inject BUBBLE_JS before </body> (only if not already there)
    if 'id="bubble-search"' not in html:
        html = html.replace('</body>', BUBBLE_JS + '\n</body>', 1)

    with open(path, 'w') as f:
        f.write(html)
    print(f'  ✓  {path.replace(ROOT, "")}')


def make_cleveland_page(nj_path, cle_path, nj_subs):
    """Clone the NJ page and localise it for Cleveland."""
    import re as _re
    with open(nj_path) as f:
        html = f.read()

    # Rewrite service bubble hrefs from ../new-jersey/{slug}/ to ../cleveland-ohio/{slug}/
    # Use regex to target only paths that have a slug (not the bare location link)
    html = _re.sub(
        r'href="\.\./new-jersey/([a-z0-9-]+)/"',
        r'href="../cleveland-ohio/\1/"',
        html
    )

    for old, new in nj_subs:
        html = html.replace(old, new)

    os.makedirs(os.path.dirname(cle_path), exist_ok=True)
    with open(cle_path, 'w') as f:
        f.write(html)
    print(f'  ✓  {cle_path.replace(ROOT, "")}')


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':

    # --- Chimney NJ ---
    patch_page(
        path=os.path.join(ROOT, 'new-jersey', 'chimney', 'index.html'),
        old_h1='<h1 class="sp-title"><span class="text-accent">Chimney &amp; Masonry</span><br>Across New Jersey</h1>',
        new_h1='<h1 class="sp-title">Chimney &amp; Masonry <span class="text-accent">Services in New Jersey</span></h1>',
        cats=CHIMNEY_CATS,
        location_name='New Jersey',
    )

    # --- Handyman NJ ---
    patch_page(
        path=os.path.join(ROOT, 'new-jersey', 'handyman', 'index.html'),
        old_h1='<h1 class="sp-title"><span class="text-accent">Handyman Services</span><br>Across New Jersey</h1>',
        new_h1='<h1 class="sp-title">Handyman <span class="text-accent">Services in New Jersey</span></h1>',
        cats=HANDYMAN_CATS,
        location_name='New Jersey',
    )

    # --- Chimney Cleveland (clone of NJ with substitutions) ---
    chimney_cle_subs = [
        # title / meta
        ('Chimney Repair &amp; Masonry Services in New Jersey (NJ) – Tuckpointing, Spalling &amp; Rebuilds | The Fix Wizard',
         'Chimney Repair &amp; Masonry Services in Cleveland, Ohio | The Fix Wizard'),
        ('chimney repair and masonry services across New Jersey', 'chimney repair and masonry services across Cleveland, Ohio'),
        ('Serving Bergen, Morris, Essex, Monmouth &amp; all NJ counties', 'Serving Lakewood, Parma, Strongsville, Westlake &amp; all Cleveland suburbs'),
        # h1 (already patched above won't match again — but this is the Cleveland copy)
        ('Chimney &amp; Masonry <span class="text-accent">Services in New Jersey</span>',
         'Chimney &amp; Masonry <span class="text-accent">Services in Cleveland, Ohio</span>'),
        # subtitle
        ('New Jersey winters are brutal on chimneys and masonry. We repair, rebuild, and waterproof — before the damage becomes a fire hazard or structural failure.',
         "Cleveland's lake-effect winters and freeze-thaw cycles are brutal on chimneys and masonry. We repair, rebuild, and waterproof — before the damage becomes a fire hazard or structural failure."),
        # badges / breadcrumb
        ('Across New Jersey', 'Across Cleveland, Ohio'),
        # section desc
        ("NJ's freeze-thaw cycles are the harshest test of any masonry. We repair what NJ winters break — across Morris, Bergen, Essex, Monmouth and every county.",
         "Cleveland's lake-effect freeze-thaw cycles are the harshest test of any masonry. We repair what Ohio winters break — across Lakewood, Parma, Shaker Heights, and every suburb."),
        # bubble section location label
        ('Every Service We <span class="text-accent">Offer in New Jersey</span>',
         'Every Service We <span class="text-accent">Offer in Cleveland, Ohio</span>'),
        # process desc
        ('Most chimney and masonry repairs are completed in one visit — before the next NJ winter makes things worse.',
         'Most chimney and masonry repairs are completed in one visit — before the next Cleveland winter makes things worse.'),
    ]

    make_cleveland_page(
        nj_path=os.path.join(ROOT, 'new-jersey', 'chimney', 'index.html'),
        cle_path=os.path.join(ROOT, 'cleveland-ohio', 'chimney', 'index.html'),
        nj_subs=chimney_cle_subs,
    )

    # --- Handyman Cleveland (clone of NJ with substitutions) ---
    handyman_cle_subs = [
        ('Handyman Services in New Jersey | The Fix Wizard',
         'Handyman Services in Cleveland, Ohio | The Fix Wizard'),
        ('One call handles every item on your home repair list. Drywall, painting, doors, plumbing, electrical, furniture assembly — we cover it all, licensed and insured across all of New Jersey.',
         'One call handles every item on your home repair list. Drywall, painting, doors, plumbing, electrical, furniture assembly — we cover it all, licensed and insured across greater Cleveland, Ohio.'),
        ('Handyman <span class="text-accent">Services in New Jersey</span>',
         'Handyman <span class="text-accent">Services in Cleveland, Ohio</span>'),
        ('From small fixes to full-room projects — we handle every repair on your list quickly and correctly, across all 21 New Jersey counties.',
         'From small fixes to full-room projects — we handle every repair on your list quickly and correctly, across all greater Cleveland suburbs.'),
        ('Every Service We <span class="text-accent">Offer in New Jersey</span>',
         'Every Service We <span class="text-accent">Offer in Cleveland, Ohio</span>'),
        ('Most handyman jobs are completed in a single visit — anywhere in New Jersey.',
         'Most handyman jobs are completed in a single visit — anywhere in greater Cleveland, Ohio.'),
    ]

    make_cleveland_page(
        nj_path=os.path.join(ROOT, 'new-jersey', 'handyman', 'index.html'),
        cle_path=os.path.join(ROOT, 'cleveland-ohio', 'handyman', 'index.html'),
        nj_subs=handyman_cle_subs,
    )

    print('\nDone.')
