#!/usr/bin/env python3
"""Generates /chimney-services/ and /handyman-services/ generic hub pages."""

import os, base64

ROOT = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(ROOT, "favicon-32.png"), "rb") as f:
        FAVICON_B64 = base64.b64encode(f.read()).decode()
    FAVICON_TAG = f'<link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{FAVICON_B64}">'
except:
    FAVICON_TAG = '<link rel="icon" href="/favicon.ico" type="image/x-icon">'

GFONTS = "https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"
FA     = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"

# ── Shared partials ───────────────────────────────────────────────────────────

NAVBAR = """\
    <nav id="navbar" class="navbar">
        <div class="container nav-container">
            <a href="../" class="logo"><img src="../assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img" width="199" height="110"></a>
            <ul class="nav-links">
                <li><a href="../" class="nav-link">Home</a></li>
                <li><a href="../#services" class="nav-link">Services</a></li>
                <li><a href="../#why-us" class="nav-link">About</a></li>
                <li><a href="../#contact" class="nav-link">Contact</a></li>
                <li class="nav-dropdown">
                    <a href="../locations/" class="nav-link flex items-center gap-1.5">Locations <i class="fas fa-chevron-down text-[10px] opacity-50 mt-px"></i></a>
                    <div class="nav-dropdown-menu">
                        <a href="../new-jersey/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> New Jersey</a>
                        <a href="../cleveland-ohio/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                        <div class="nav-dropdown-divider"></div>
                        <a href="../locations/" class="nav-dropdown-item" style="color:rgba(255,255,255,.45)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
                    </div>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="tel:+15551234567" class="nav-phone"><i class="fas fa-phone"></i><span>(555) 123-4567</span></a>
                <a href="../#contact" class="btn btn-primary nav-cta">Free Quote
                    <svg class="btn-spark bs-1" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                    <svg class="btn-spark bs-2" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                    <svg class="btn-spark bs-3" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                </a>
            </div>
            <button class="hamburger" id="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
        </div>
    </nav>
    <div class="mobile-menu" id="mobileMenu">
        <button class="mobile-menu-close" id="mobileClose"><i class="fas fa-times"></i></button>
        <ul class="mobile-nav-links">
            <li><a href="../" class="mobile-link">Home</a></li>
            <li><a href="../#services" class="mobile-link">Services</a></li>
            <li><a href="../#why-us" class="mobile-link">About</a></li>
            <li><a href="../#contact" class="mobile-link">Contact</a></li>
            <li>
                <span class="mobile-loc-label">Locations</span>
                <a href="../new-jersey/"     class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> New Jersey</a>
                <a href="../cleveland-ohio/" class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                <a href="../locations/"      class="mobile-link mobile-loc-sub" style="color:rgba(255,255,255,.4)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
            </li>
        </ul>
        <a href="tel:+15551234567" class="mobile-phone"><i class="fas fa-phone"></i>(555) 123-4567</a>
        <a href="../#contact" class="btn btn-primary mobile-cta mobile-link">Get Free Quote</a>
    </div>
    <div class="mobile-overlay" id="mobileOverlay"></div>"""

FOOTER = """\
    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="../" class="logo"><img src="../assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img footer-logo-img" width="199" height="110"></a>
                <p>The Fix Wizard handles the repairs most people dread. Quality work, honest pricing, and results that last.</p>
                <div class="social-links">
                    <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="#" aria-label="Google"><i class="fab fa-google"></i></a>
                    <a href="#" aria-label="Yelp"><i class="fab fa-yelp"></i></a>
                </div>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <ul>
                    <li><a href="../chimney-services/">Chimney &amp; Masonry</a></li>
                    <li><a href="../handyman-services/">Handyman Services</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Service Areas</h4>
                <ul>
                    <li><a href="../new-jersey/">New Jersey</a></li>
                    <li><a href="../cleveland-ohio/">Cleveland, Ohio</a></li>
                    <li><a href="../locations/">All Locations</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <ul class="footer-contact">
                    <li><i class="fas fa-phone"></i><a href="tel:+15551234567">(555) 123-4567</a></li>
                    <li><i class="fas fa-envelope"></i><a href="mailto:hello@handypro.com">hello@handypro.com</a></li>
                    <li><i class="fas fa-clock"></i><span>Mon–Sat: 7am – 7pm</span></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container footer-bottom-inner">
                <p>&copy; <span id="year"></span> The Fix Wizard. All rights reserved.</p>
                <p>Made with <i class="fas fa-heart" style="color:var(--orange)"></i> for homeowners everywhere</p>
            </div>
        </div>
    </footer>"""

SPARKLES = """\
        <div class="hero-sparkles absolute inset-0 pointer-events-none z-[2] overflow-hidden" aria-hidden="true">
            <svg class="sparkle sp-1" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
            <svg class="sparkle sp-2" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
            <svg class="sparkle sp-3" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
            <svg class="sparkle sp-4" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
            <svg class="sparkle sp-5" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
        </div>
        <div class="absolute bottom-7 left-1/2 -translate-x-1/2 flex flex-col items-center gap-1.5 text-white/30 text-[10px] font-medium tracking-[2px] uppercase z-[2]">
            <span>Scroll</span>
            <i class="fas fa-chevron-down text-[12px]"></i>
        </div>"""

HEAD_COMMON = f"""\
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {FAVICON_TAG}
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <style>:root{{--nav-h:150px}}*,*::before,*::after{{box-sizing:border-box}}body{{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}}body.no-scroll{{overflow:hidden}}a{{text-decoration:none;color:inherit}}.reveal{{opacity:0;transform:translateY(28px)}}.hero{{background-color:#091236;color:#fff}}.mobile-menu{{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}}.mobile-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}}.faq-answer{{max-height:0;overflow:hidden}}#navbar{{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}}@media(max-width:768px){{:root{{--nav-h:96px}}}}</style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="{GFONTS}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{GFONTS}"></noscript>
    <link rel="preload" href="{FA}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{FA}"></noscript>
    <link rel="preload" href="../css/tw.css" as="style">
    <link rel="stylesheet" href="../css/tw.css">
    <link rel="preload" href="../css/custom.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="../css/custom.css"></noscript>"""

# Bubble CSS — plain string (no f-string) to avoid escaping {}
BUBBLE_CSS = """
<style>
@keyframes bubble-float {
  0%,100% { transform: translateY(0px); }
  50%      { transform: translateY(-6px); }
}
.svc-bubble {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #fff;
  border: 2px solid #e8edf5;
  border-radius: 100px;
  padding: 10px 18px 10px 13px;
  font-size: 13.5px;
  font-weight: 500;
  color: #1e2d5a;
  cursor: default;
  user-select: none;
  animation: bubble-float var(--dur,3.8s) ease-in-out var(--delay,0s) infinite;
  transition: transform .28s cubic-bezier(.34,1.56,.64,1),
              opacity .2s ease,
              border-color .15s ease,
              box-shadow .15s ease,
              background .15s ease;
  will-change: transform, opacity;
}
.svc-bubble:hover {
  border-color: #FF6B35;
  background: #fff7f4;
  box-shadow: 0 8px 24px rgba(255,107,53,.18);
  animation-play-state: paused;
  transform: translateY(-4px) scale(1.05) !important;
}
.svc-bubble.b-hide {
  transform: scale(0) !important;
  opacity: 0 !important;
  pointer-events: none;
  animation: none !important;
}
.svc-bubble .b-icon {
  font-size: 11px;
  color: #FF6B35;
  flex-shrink: 0;
}
.svc-category { transition: opacity .2s ease; }
.svc-category.c-hide { display: none; }
.bubbles-row { display: flex; flex-wrap: wrap; gap: 10px; }
.cat-hdr {
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 14px;
}
.cat-hdr-icon {
  width: 30px; height: 30px;
  background: rgba(255,107,53,.1);
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.cat-hdr-icon i { color: #FF6B35; font-size: 12px; }
.cat-hdr-label {
  font-size: 11px; font-weight: 800;
  color: #0d1b4b; text-transform: uppercase;
  letter-spacing: .1em; white-space: nowrap;
}
.cat-hdr-line { flex: 1; height: 1px; background: #eef1f7; }
.srch-wrap {
  position: relative;
  display: flex; align-items: center;
}
.srch-icon {
  position: absolute; left: 17px;
  color: #94a3b8; font-size: 15px; pointer-events: none;
}
.srch-input {
  width: 100%;
  padding: 15px 50px 15px 46px;
  border: 2px solid #e2e8f0;
  border-radius: 18px;
  font-size: 15px; font-weight: 500;
  color: #0d1b4b; font-family: Inter, sans-serif;
  outline: none; background: #fff;
  transition: border-color .2s, box-shadow .2s;
}
.srch-input:focus {
  border-color: #FF6B35;
  box-shadow: 0 0 0 4px rgba(255,107,53,.1);
}
.srch-input::placeholder { color: #94a3b8; }
.srch-clear {
  position: absolute; right: 16px;
  width: 26px; height: 26px;
  background: #f1f5f9; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #64748b; font-size: 11px; cursor: pointer;
  opacity: 0; pointer-events: none;
  transition: opacity .15s, background .15s;
}
.srch-clear.show { opacity: 1; pointer-events: all; }
.srch-clear:hover { background: #FF6B35; color: #fff; }
.srch-hint {
  text-align: center; font-size: 13px; color: #94a3b8;
  margin-top: 10px; min-height: 18px;
}
.srch-none {
  text-align: center; font-size: 15px; color: #64748b;
  padding: 40px 0; display: none;
}
.srch-none button {
  color: #FF6B35; font-weight: 600;
  background: none; border: none; cursor: pointer; margin-left: 4px;
}
</style>"""

# Bubble JS — plain string
BUBBLE_JS = """
<script>
(function() {
  var inp    = document.getElementById('srch');
  var clr    = document.getElementById('srch-clr');
  var hint   = document.getElementById('srch-hint');
  var none   = document.getElementById('srch-none');
  var bubbles = document.querySelectorAll('.svc-bubble');
  var cats   = document.querySelectorAll('.svc-category');

  function run(q) {
    q = q.toLowerCase().trim();
    var shown = 0;
    bubbles.forEach(function(b) {
      var match = !q || b.dataset.s.includes(q);
      if (match) { b.classList.remove('b-hide'); shown++; }
      else        { b.classList.add('b-hide'); }
    });
    cats.forEach(function(c) {
      var any = Array.from(c.querySelectorAll('.svc-bubble')).some(function(b) {
        return !b.classList.contains('b-hide');
      });
      c.classList.toggle('c-hide', !any);
    });
    clr.classList.toggle('show', q.length > 0);
    hint.textContent = q ? (shown + ' service' + (shown !== 1 ? 's' : '') + ' found') : '';
    none.style.display = (q && shown === 0) ? 'block' : 'none';
  }

  inp.addEventListener('input', function() { run(inp.value); });
  clr.addEventListener('click', function() { inp.value = ''; run(''); inp.focus(); });
  document.getElementById('srch-none-clr').addEventListener('click', function() {
    inp.value = ''; run(''); inp.focus();
  });
})();
</script>"""


# ── Service data ──────────────────────────────────────────────────────────────

CHIMNEY_CATS = [
    {
        "cat": "Inspections &amp; Sweep Services",
        "icon": "fa-magnifying-glass",
        "items": [
            ("fa-magnifying-glass",  "Level 1 Inspection &amp; Standard Sweep"),
            ("fa-camera",            "Level 2 Inspection (Real Estate / Camera Scan)"),
            ("fa-broom",             "Heavy Creosote Rotary Cleaning"),
        ],
    },
    {
        "cat": "Caps, Covers &amp; Maintenance",
        "icon": "fa-circle-dot",
        "items": [
            ("fa-circle-dot",        "Single-Flue Stainless Steel Cap Installation"),
            ("fa-layer-group",       "Multi-Flue / Custom Top-Mount Cap Installation"),
            ("fa-square",            "Outside Mount Chase Cover Replacement"),
            ("fa-droplet-slash",     "Chimney Water Repellent Application"),
        ],
    },
    {
        "cat": "Masonry &amp; Crown Repairs",
        "icon": "fa-trowel-bricks",
        "items": [
            ("fa-helmet-safety",     "Crown Repair (Elastomeric Coating)"),
            ("fa-hat-hard",          "Full Chimney Crown Rebuild"),
            ("fa-trowel-bricks",     "Minor Tuckpointing &amp; Mortar Repair"),
            ("fa-fire-flame-curved", "Firebox Re-bricking / Refractory Panel Swap"),
        ],
    },
    {
        "cat": "Components &amp; Liners",
        "icon": "fa-pipe",
        "items": [
            ("fa-toggle-on",         "Top-Damper Installation (Lyemance/Lock-Top)"),
            ("fa-pipe",              "Stainless Steel Flue Liner Installation"),
        ],
    },
]

HANDYMAN_CATS = [
    {
        "cat": "Mounting &amp; Hanging",
        "icon": "fa-tv",
        "items": [
            ("fa-tv",                "TV Wall Mounting"),
            ("fa-image",             "Heavy Mirror / Large Artwork Hanging"),
            ("fa-window-restore",    "Blinds / Shades / Curtain Rod Installation"),
            ("fa-layer-group",       "Floating Shelves Installation"),
        ],
    },
    {
        "cat": "Minor Plumbing &amp; Bath",
        "icon": "fa-faucet",
        "items": [
            ("fa-faucet",            "Kitchen or Bathroom Faucet Replacement"),
            ("fa-trash-can",         "Garbage Disposal Replacement"),
            ("fa-toilet",            "Toilet Reset / Flange Repair / Inner Components Swap"),
            ("fa-fan",               "Bathroom Exhaust Fan Replacement"),
            ("fa-shower",            "Shower Head &amp; Grab Bar Installation"),
        ],
    },
    {
        "cat": "Minor Electrical &amp; Fixtures",
        "icon": "fa-bolt",
        "items": [
            ("fa-fan",               "Ceiling Fan Installation"),
            ("fa-lightbulb",         "Standard Light Fixture / Chandelier Swap"),
            ("fa-plug",              "Outlet / Switch Upgrades"),
            ("fa-bell",              "Video Doorbell / Smart Lock Installation"),
        ],
    },
    {
        "cat": "Carpentry, Drywall &amp; Trim",
        "icon": "fa-fill-drip",
        "items": [
            ("fa-fill-drip",         "Drywall Patching"),
            ("fa-ruler-horizontal",  "Baseboard / Shoe Molding Installation"),
            ("fa-screwdriver-wrench","Cabinet Hinge &amp; Hardware Upgrade"),
            ("fa-dog",               "Pet Door Installation"),
        ],
    },
    {
        "cat": "Assembly &amp; Miscellaneous",
        "icon": "fa-couch",
        "items": [
            ("fa-couch",             "Flat-Pack Furniture Assembly"),
            ("fa-stairs",            "Attic Ladder Replacement"),
            ("fa-inbox",             "Mailbox &amp; Post Installation"),
        ],
    },
]


# ── Bubble section builder ────────────────────────────────────────────────────

def bubble_section(cats, section_title, section_tag):
    # Float durations/delays staggered per bubble so they move independently
    DURATIONS = [3.6, 4.1, 3.9, 4.4, 3.7, 4.2, 3.8, 4.5]
    DELAYS    = [0, 0.4, 0.8, 1.2, 0.2, 0.6, 1.0, 1.4]

    idx = 0
    cats_html = ""
    for cat in cats:
        bubbles_html = ""
        for icon, name in cat["items"]:
            dur   = DURATIONS[idx % len(DURATIONS)]
            delay = DELAYS[idx % len(DELAYS)]
            # search key: strip html entities and lowercase
            s_key = name.lower().replace("&amp;", "and").replace("/", " ").replace("(", "").replace(")", "")
            bubbles_html += f"""
                    <div class="svc-bubble" data-s="{s_key}" style="--dur:{dur}s;--delay:{delay}s">
                        <i class="fas {icon} b-icon"></i><span>{name}</span>
                    </div>"""
            idx += 1
        cats_html += f"""
            <div class="svc-category">
                <div class="cat-hdr">
                    <div class="cat-hdr-icon"><i class="fas {cat['icon']}"></i></div>
                    <span class="cat-hdr-label">{cat['cat']}</span>
                    <div class="cat-hdr-line"></div>
                </div>
                <div class="bubbles-row">{bubbles_html}
                </div>
            </div>"""

    total = sum(len(c["items"]) for c in cats)
    return f"""
    <!-- BUBBLE SERVICES -->
    <section class="py-20 bg-white">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">{section_tag}</span>
                <h2 class="section-title">{section_title}</h2>
                <p class="section-desc">All {total} services we offer — search to find yours instantly.</p>
            </div>

            <div class="max-w-[580px] mx-auto mb-12 reveal">
                <div class="srch-wrap">
                    <i class="fas fa-search srch-icon"></i>
                    <input id="srch" type="text" class="srch-input" placeholder="Search services…" autocomplete="off" spellcheck="false">
                    <div id="srch-clr" class="srch-clear" role="button" aria-label="Clear search">
                        <i class="fas fa-times"></i>
                    </div>
                </div>
                <p id="srch-hint" class="srch-hint"></p>
            </div>

            <div id="svc-container" class="flex flex-col gap-10 max-w-[960px] mx-auto">
{cats_html}
            </div>

            <div id="srch-none" class="srch-none">
                No services match your search.
                <button id="srch-none-clr">Clear search</button>
            </div>
        </div>
    </section>"""


# ── Hero shared builder ───────────────────────────────────────────────────────

def hero_html(badge, h1_line1, h1_line2, description, pills, card_title, card_subtitle, card_icon, loc_nj_sub, loc_cle_sub):
    pills_html = "".join(
        f'<div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas {ic} text-orange text-[12px]"></i> {label}</div>'
        for ic, label in pills
    )
    return f"""\
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas {card_icon} text-orange text-[11px]"></i>
                        <span>{badge}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(32px,5vw,64px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        {h1_line1}<br>
                        <span class="text-orange">{h1_line2}</span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-6 max-w-[560px]">{description}</p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        {pills_html}
                    </div>
                    <div class="flex items-center gap-3 mb-12 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="../new-jersey/" class="btn btn-primary btn-lg"><i class="fas fa-map-marker-alt"></i> New Jersey</a>
                        <a href="../cleveland-ohio/" class="btn btn-outline btn-lg"><i class="fas fa-map-marker-alt"></i> Cleveland, Ohio</a>
                    </div>
                    <div class="w-full h-px bg-white/10 mb-8"></div>
                    <div class="flex items-center gap-8 flex-wrap justify-center tab:justify-start hero-stats">
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="projects">0</span>+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Jobs Done</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="years">0</span>+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Years Exp</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="satisfaction">0</span>%</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Satisfaction</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="specialties">0</span></div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Locations</div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[520px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-6">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas {card_icon}"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">{card_title}</div>
                                <p class="text-[13px] text-white/50">{card_subtitle}</p>
                            </div>
                        </div>
                        <div class="flex flex-col gap-3">
                            <a href="../new-jersey/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110"><i class="fas fa-location-dot"></i></div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">New Jersey</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">{loc_nj_sub}</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                            <a href="../cleveland-ohio/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110"><i class="fas fa-location-dot"></i></div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">Cleveland, Ohio</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">{loc_cle_sub}</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                        </div>
                        <a href="../#contact" class="btn btn-primary btn-full"><i class="fas fa-paper-plane"></i> Request a Free Quote</a>
                        <div class="flex gap-3 pt-1 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-shield-halved text-orange text-[13px]"></i><span>Licensed &amp; Insured</span></div>
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-clock text-orange text-[13px]"></i><span>Same Day Available</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
{SPARKLES}
    </section>"""


# ── Location CTA section ──────────────────────────────────────────────────────

def loc_cta(h2, desc):
    return f"""
    <section class="py-16 bg-white">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Our Locations</span>
                <h2 class="section-title">{h2}</h2>
                <p class="section-desc">{desc}</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-[760px] mx-auto reveal">
                <a href="../new-jersey/" class="group flex items-center gap-5 bg-white border-2 border-slate-200 rounded-card p-6 transition-all hover:border-orange hover:shadow-[0_8px_32px_rgba(255,107,53,.15)]">
                    <div class="w-14 h-14 shrink-0 bg-orange/10 rounded-xl flex items-center justify-center group-hover:bg-orange transition-colors">
                        <i class="fas fa-location-dot text-orange group-hover:text-white text-[22px] transition-colors"></i>
                    </div>
                    <div>
                        <div class="text-[18px] font-bold text-navy-900 mb-1">New Jersey</div>
                        <div class="text-[13px] text-slate-500">All 21 counties · Licensed in NJ · Same-day available</div>
                    </div>
                    <i class="fas fa-arrow-right text-slate-300 group-hover:text-orange ml-auto transition-colors"></i>
                </a>
                <a href="../cleveland-ohio/" class="group flex items-center gap-5 bg-white border-2 border-slate-200 rounded-card p-6 transition-all hover:border-orange hover:shadow-[0_8px_32px_rgba(255,107,53,.15)]">
                    <div class="w-14 h-14 shrink-0 bg-orange/10 rounded-xl flex items-center justify-center group-hover:bg-orange transition-colors">
                        <i class="fas fa-location-dot text-orange group-hover:text-white text-[22px] transition-colors"></i>
                    </div>
                    <div>
                        <div class="text-[18px] font-bold text-navy-900 mb-1">Cleveland, Ohio</div>
                        <div class="text-[13px] text-slate-500">Greater Cleveland · Licensed in OH · Same-day available</div>
                    </div>
                    <i class="fas fa-arrow-right text-slate-300 group-hover:text-orange ml-auto transition-colors"></i>
                </a>
            </div>
        </div>
    </section>"""


# ── Page builders ─────────────────────────────────────────────────────────────

def chimney_page():
    faqs = [
        ("How often should I have my chimney swept?",
         "Most chimney safety organizations recommend annual sweeping and inspection before each heating season. Homes that burn wood regularly may need sweeping twice per year. Gas appliances still require annual inspection even without heavy creosote buildup."),
        ("What is tuckpointing and do I need it?",
         "Tuckpointing is grinding out deteriorated mortar joints and packing in fresh mortar. If you see gaps, crumbling, or missing mortar between bricks, tuckpointing is overdue. Left untreated, water infiltration causes far costlier structural damage."),
        ("What is a chimney liner and why does it matter?",
         "A chimney liner contains combustion gases and directs them safely out of the flue. An improperly sized or deteriorated liner can allow carbon monoxide and heat to reach combustible framing. Liner installation is code-required for most fuel-burning appliances."),
        ("Do you service both wood-burning and gas fireplaces?",
         "Yes. We service all chimney and fireplace types — wood-burning, gas inserts, oil appliances, and pellet stoves. The specific services differ by fuel type but we handle all of them."),
        ("What areas do you serve for chimney repair?",
         "We serve all 21 counties in New Jersey and the greater Cleveland, Ohio area — Lakewood, Parma, Strongsville, Westlake, Beachwood, Shaker Heights, and 14 more suburbs."),
    ]
    faqs_html = "".join(f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false"><span>{q}</span><i class="fas fa-plus"></i></button>
                    <div class="faq-answer" aria-hidden="true"><p>{a}</p></div>
                </div>""" for q, a in faqs)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <meta name="description" content="Expert chimney repair and masonry services — inspections, sweeping, tuckpointing, crown repair, liner installation, caps, and more. Serving New Jersey and Cleveland, Ohio.">
    <title>Chimney Repair &amp; Masonry Services | The Fix Wizard</title>
{BUBBLE_CSS}
</head>
<body>
{NAVBAR}
{hero_html(
    badge="Chimney &amp; Masonry Specialists",
    h1_line1="Expert Chimney Repair",
    h1_line2="&amp; <span class='lightning-word'>Masonry Services</span>",
    description="From annual chimney sweeping and tuckpointing to full liner installation and masonry restoration — licensed specialists covering every repair your chimney needs.",
    pills=[("fa-broom","Sweeping &amp; Inspection"),("fa-trowel-bricks","Tuckpointing"),("fa-pipe","Liner Install")],
    card_title="Chimney Services Near You",
    card_subtitle="Select your location to get started",
    card_icon="fa-fire",
    loc_nj_sub="All 21 counties · Bergen to Cape May",
    loc_cle_sub="Greater Cleveland · 20 suburbs",
)}
{bubble_section(CHIMNEY_CATS, "Complete Chimney &amp; <span class='text-accent'>Masonry Services</span>", "What We Cover")}
{loc_cta("Chimney Services in <span class='text-accent'>Your Area</span>", "Choose your location for local pricing, same-day availability, and area-specific service details.")}
    <section id="faq" class="faq">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Q&amp;A</span>
                <h2 class="section-title">Chimney Service <span class="text-accent">Questions</span></h2>
                <p class="section-desc">Common questions homeowners ask before booking chimney repair or masonry services.</p>
            </div>
            <div class="faq-accordion">{faqs_html}
            </div>
        </div>
    </section>
    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>Ready to Book Chimney Service?</h2>
                <p>Free estimates · Licensed &amp; insured · Same-day available in NJ &amp; Cleveland</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15551234567" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Free Quote</a>
            </div>
        </div>
    </section>
{FOOTER}
    <script type="module" src="../js/service-page.js"></script>
{BUBBLE_JS}
</body>
</html>"""


def handyman_page():
    faqs = [
        ("What handyman services do you offer?",
         "Drywall patching and texture matching, interior and exterior painting, door repair and installation, furniture assembly, TV mounting, light electrical (outlets, switches, fans, fixtures), light plumbing (faucets, toilets, drains, disposals), weatherstripping, caulking, tile repair, and general home maintenance."),
        ("Can you do multiple jobs in one visit?",
         "Absolutely — combining multiple tasks is the most efficient way to use our time and yours. Common combinations include drywall patching + paint touch-ups, outlet replacement + fan installation, and furniture assembly + TV mounting, all in a single appointment."),
        ("How much does handyman service cost?",
         "Most jobs run $150–$500 depending on complexity. Furniture assembly typically runs $75–$200 per piece. TV mounting is $100–$200. Drywall patch and texture match averages $150–$350. We provide free estimates before any work begins."),
        ("Are your handymen licensed and insured?",
         "Yes. All technicians are background-checked, and The Fix Wizard carries full liability insurance on every job in both New Jersey and Ohio."),
        ("What areas do you serve for handyman services?",
         "All 21 counties in New Jersey and the greater Cleveland, Ohio area — including Lakewood, Parma, Strongsville, Westlake, Beachwood, Shaker Heights, and 14 more suburbs."),
    ]
    faqs_html = "".join(f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false"><span>{q}</span><i class="fas fa-plus"></i></button>
                    <div class="faq-answer" aria-hidden="true"><p>{a}</p></div>
                </div>""" for q, a in faqs)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <meta name="description" content="Expert handyman services — drywall repair, painting, plumbing, electrical, door repair, furniture assembly, TV mounting, and more. Serving New Jersey and Cleveland, Ohio.">
    <title>Handyman Services | The Fix Wizard</title>
{BUBBLE_CSS}
</head>
<body>
{NAVBAR}
{hero_html(
    badge="Licensed Handyman Specialists",
    h1_line1="Expert Handyman",
    h1_line2="Services <span class='lightning-word'>Near You</span>",
    description="From drywall patching and painting to light plumbing, electrical, doors, and furniture assembly — one call covers your entire repair list. Licensed, insured, same-day available.",
    pills=[("fa-fill-drip","Drywall &amp; Painting"),("fa-faucet","Plumbing &amp; Electrical"),("fa-couch","Assembly &amp; Mounting")],
    card_title="Handyman Services Near You",
    card_subtitle="Select your location to get started",
    card_icon="fa-screwdriver-wrench",
    loc_nj_sub="All 21 counties · Bergen to Cape May",
    loc_cle_sub="Greater Cleveland · 20 suburbs",
)}
{bubble_section(HANDYMAN_CATS, "Complete <span class='text-accent'>Handyman Services</span>", "What We Cover")}
{loc_cta("Handyman Services in <span class='text-accent'>Your Area</span>", "Choose your location for local pricing, same-day availability, and area-specific service details.")}
    <section id="faq" class="faq">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Q&amp;A</span>
                <h2 class="section-title">Handyman Service <span class="text-accent">Questions</span></h2>
                <p class="section-desc">Common questions homeowners ask before booking handyman services.</p>
            </div>
            <div class="faq-accordion">{faqs_html}
            </div>
        </div>
    </section>
    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>Ready to Book a Handyman?</h2>
                <p>Free estimates · Licensed &amp; insured · Same-day available in NJ &amp; Cleveland</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15551234567" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Free Quote</a>
            </div>
        </div>
    </section>
{FOOTER}
    <script type="module" src="../js/service-page.js"></script>
{BUBBLE_JS}
</body>
</html>"""


if __name__ == "__main__":
    for slug, fn in [("chimney-services", chimney_page), ("handyman-services", handyman_page)]:
        out_dir = os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(fn())
        print(f"  ✓  /{slug}/index.html")
