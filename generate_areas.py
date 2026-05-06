#!/usr/bin/env python3
"""
Generates:
  1. /locations/index.html  — hub page with all 21 NJ county cards
  2. /[service]-in-[county]-nj/index.html  — 168 service-area pages (21 × 8)
  3. Patches Locations nav link into all existing service pages and blog posts
"""

import os, re, textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))

# ─── Data ──────────────────────────────────────────────────────────────────────

COUNTIES = [
    {"name": "Bergen County",    "slug": "bergen-county-nj",    "towns": "Hackensack · Paramus · Fort Lee · Englewood",             "desc": "NJ's most populous county — dense suburban neighborhoods with aging homes in need of expert repair."},
    {"name": "Essex County",     "slug": "essex-county-nj",     "towns": "Newark · Montclair · Bloomfield · Maplewood",             "desc": "From Newark's urban housing to Montclair's Victorian homes — skilled repairs for every property type."},
    {"name": "Middlesex County", "slug": "middlesex-county-nj", "towns": "Edison · New Brunswick · Woodbridge · Piscataway",        "desc": "Fast-growing county with diverse housing stock, from ranch homes to newer developments."},
    {"name": "Monmouth County",  "slug": "monmouth-county-nj",  "towns": "Red Bank · Freehold · Asbury Park · Middletown",          "desc": "Shore county with coastal homes, salt-air wear, and a mix of historic and modern properties."},
    {"name": "Morris County",    "slug": "morris-county-nj",    "towns": "Morristown · Parsippany · Madison · Rockaway",            "desc": "Wooded suburbs with colonial and split-level homes common across northern New Jersey."},
    {"name": "Hudson County",    "slug": "hudson-county-nj",    "towns": "Jersey City · Hoboken · Bayonne · Union City",            "desc": "Densely packed brownstones, townhouses, and multi-family buildings in one of NJ's busiest counties."},
    {"name": "Union County",     "slug": "union-county-nj",     "towns": "Elizabeth · Westfield · Summit · Plainfield",             "desc": "Central NJ county blending affluent suburbs with working-class neighborhoods — we serve them all."},
    {"name": "Ocean County",     "slug": "ocean-county-nj",     "towns": "Toms River · Lakewood · Brick · Jackson",                 "desc": "Shore and inland county where storm damage repairs and coastal home maintenance are a year-round need."},
    {"name": "Somerset County",  "slug": "somerset-county-nj",  "towns": "Bridgewater · Somerville · Bound Brook · Raritan",        "desc": "Upscale suburban county with well-maintained homes that still benefit from expert professional repair."},
    {"name": "Passaic County",   "slug": "passaic-county-nj",   "towns": "Paterson · Clifton · Wayne · Pompton Lakes",              "desc": "Busy northern county with dense residential neighborhoods and older building stock requiring skilled upkeep."},
    {"name": "Camden County",    "slug": "camden-county-nj",    "towns": "Cherry Hill · Voorhees · Haddonfield · Camden",           "desc": "South Jersey's most populous county — rowhouses, ranches, and suburban homes served with care."},
    {"name": "Burlington County","slug": "burlington-county-nj","towns": "Moorestown · Medford · Evesham · Mount Holly",            "desc": "Large central county with historic towns and newer suburban developments throughout the Pinelands."},
    {"name": "Mercer County",    "slug": "mercer-county-nj",    "towns": "Trenton · Princeton · Hamilton · Lawrence",               "desc": "From Trenton's urban housing to Princeton's prestigious estates — expert repairs across the board."},
    {"name": "Atlantic County",  "slug": "atlantic-county-nj",  "towns": "Atlantic City · Egg Harbor · Galloway · Absecon",         "desc": "Shore and casino country with aging properties and high demand for reliable home repair services."},
    {"name": "Gloucester County","slug": "gloucester-county-nj","towns": "Woodbury · Deptford · Washington Twp · Glassboro",        "desc": "Growing suburb of Philadelphia with a range of home styles and steady demand for quality repairs."},
    {"name": "Cumberland County","slug": "cumberland-county-nj","towns": "Vineland · Bridgeton · Millville · Commercial Twp",       "desc": "South Jersey's rural county with older housing stock and unique repair needs we're equipped to handle."},
    {"name": "Cape May County",  "slug": "cape-may-county-nj",  "towns": "Cape May City · Wildwood · Ocean City · Avalon",          "desc": "Vacation homes, Victorian properties, and shore houses — seasonal and year-round maintenance covered."},
    {"name": "Warren County",    "slug": "warren-county-nj",    "towns": "Hackettstown · Washington · Phillipsburg · Belvidere",    "desc": "Rural-suburban mix with older farmhouses and modest residential neighborhoods throughout the valley."},
    {"name": "Sussex County",    "slug": "sussex-county-nj",    "towns": "Newton · Sparta · Vernon · Hardyston",                    "desc": "NJ's northernmost county — mountain-area homes with weather-related wear and older construction."},
    {"name": "Hunterdon County", "slug": "hunterdon-county-nj", "towns": "Flemington · Clinton · Lambertville · Raritan",           "desc": "Scenic rural county with historic farmhouses, horse properties, and charming older homes."},
    {"name": "Salem County",     "slug": "salem-county-nj",     "towns": "Salem City · Woodstown · Carneys Point · Penns Grove",   "desc": "South Jersey's smallest county — older housing requiring skilled, attentive home repair professionals."},
]

SERVICES = [
    {"name": "Drywall Repair",       "slug_prefix": "drywall-repair-in",       "icon": "fa-layer-group",   "parent": "drywall-repair-new-jersey",       "parent_label": "Drywall Repair in NJ"},
    {"name": "Garage Door Repair",   "slug_prefix": "garage-door-repair-in",   "icon": "fa-warehouse",     "parent": "garage-door-repair-new-jersey",   "parent_label": "Garage Door Repair in NJ"},
    {"name": "Painting",             "slug_prefix": "painting-in",             "icon": "fa-paint-roller",  "parent": "painting-new-jersey",             "parent_label": "Painting in NJ"},
    {"name": "Door Repair",          "slug_prefix": "door-repair-in",          "icon": "fa-door-open",     "parent": "door-repair-new-jersey",          "parent_label": "Door Repair in NJ"},
    {"name": "Chimney Repair",       "slug_prefix": "chimney-repair-in",       "icon": "fa-fire",          "parent": "chimney-masonry-new-jersey",      "parent_label": "Chimney & Masonry in NJ"},
    {"name": "Electrical Repair",    "slug_prefix": "electrical-repair-in",    "icon": "fa-bolt",          "parent": "electrical-repair-new-jersey",    "parent_label": "Electrical Repair in NJ"},
    {"name": "Plumbing Repair",      "slug_prefix": "plumbing-repair-in",      "icon": "fa-faucet",        "parent": "plumbing-repair-new-jersey",      "parent_label": "Plumbing Repair in NJ"},
    {"name": "Furniture Assembly",   "slug_prefix": "furniture-assembly-in",   "icon": "fa-chair",         "parent": "furniture-assembly-new-jersey",   "parent_label": "Furniture Assembly in NJ"},
]

PIN_SVG = '<svg viewBox="0 0 24 30" fill="none" aria-hidden="true"><path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 18 12 18S24 21 24 12C24 5.4 18.6 0 12 0z" fill="#FF6B35"/><circle cx="12" cy="12" r="4.5" fill="white"/></svg>'

# ─── Helpers ───────────────────────────────────────────────────────────────────

COMMON_HEAD = """\
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">"""

def navbar_html(depth, active=""):
    prefix = "../" * depth
    loc_active = ' style="color:#FF6B35;"' if active == "locations" else ""
    return f"""\
    <nav id="navbar" class="navbar">
        <div class="container nav-container">
            <a href="{prefix}" class="logo"><img src="{prefix}assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img" width="199" height="110"></a>
            <ul class="nav-links">
                <li><a href="{prefix}" class="nav-link">Home</a></li>
                <li><a href="{prefix}#services" class="nav-link">Services</a></li>
                <li><a href="{prefix}#why-us" class="nav-link">About</a></li>
                <li><a href="{prefix}#contact" class="nav-link">Contact</a></li>
                <li><a href="{prefix}locations/" class="nav-link"{loc_active}>Locations</a></li>
            </ul>
            <div class="nav-actions">
                <a href="tel:+15551234567" class="nav-phone"><i class="fas fa-phone"></i><span>(555) 123-4567</span></a>
                <a href="{prefix}#contact" class="btn btn-primary nav-cta">Free Quote
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
            <li><a href="{prefix}" class="mobile-link">Home</a></li>
            <li><a href="{prefix}#services" class="mobile-link">Services</a></li>
            <li><a href="{prefix}#why-us" class="mobile-link">About</a></li>
            <li><a href="{prefix}#contact" class="mobile-link">Contact</a></li>
            <li><a href="{prefix}locations/" class="mobile-link"{loc_active}>Locations</a></li>
        </ul>
        <a href="tel:+15551234567" class="mobile-phone"><i class="fas fa-phone"></i>(555) 123-4567</a>
        <a href="{prefix}#contact" class="btn btn-primary mobile-cta mobile-link">Get Free Quote</a>
    </div>
    <div class="mobile-overlay" id="mobileOverlay"></div>"""

def footer_html(depth):
    p = "../" * depth
    return f"""\
    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="{p}" class="logo"><img src="{p}assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img footer-logo-img" width="199" height="110"></a>
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
                    <li><a href="{p}garage-door-repair-new-jersey/">Garage Door Repair</a></li>
                    <li><a href="{p}drywall-repair-new-jersey/">Drywall Repair</a></li>
                    <li><a href="{p}furniture-assembly-new-jersey/">Furniture Assembly</a></li>
                    <li><a href="{p}painting-new-jersey/">Painting</a></li>
                    <li><a href="{p}door-repair-new-jersey/">Door Repair &amp; Replacement</a></li>
                    <li><a href="{p}chimney-masonry-new-jersey/">Chimney &amp; Masonry</a></li>
                    <li><a href="{p}electrical-repair-new-jersey/">Light Electrical</a></li>
                    <li><a href="{p}plumbing-repair-new-jersey/">Light Plumbing</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="{p}">Home</a></li>
                    <li><a href="{p}#services">All Services</a></li>
                    <li><a href="{p}locations/">Locations</a></li>
                    <li><a href="{p}#contact">Get a Quote</a></li>
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


# ─── 1. LOCATIONS HUB PAGE ──────────────────────────────────────────────────────

def county_card(county):
    slug = county["slug"]
    lines = []
    lines.append(f'                <div class="loc-card">')
    lines.append(f'                    <div class="loc-card__header">')
    lines.append(f'                        <div class="loc-pin-icon">{PIN_SVG}</div>')
    lines.append(f'                        <div>')
    lines.append(f'                            <h2 class="loc-card__name">{county["name"]}</h2>')
    lines.append(f'                            <p class="loc-card__towns">{county["towns"]}</p>')
    lines.append(f'                        </div>')
    lines.append(f'                    </div>')
    lines.append(f'                    <p class="loc-card__desc">{county["desc"]}</p>')
    lines.append(f'                    <div class="loc-card__divider"></div>')
    lines.append(f'                    <div class="loc-services-grid">')
    for svc in SERVICES:
        url = f'../{svc["slug_prefix"]}-{slug}/'
        lines.append(f'                        <a href="{url}" class="loc-svc-btn"><i class="fas {svc["icon"]}"></i> {svc["name"]}</a>')
    lines.append(f'                    </div>')
    lines.append(f'                </div>')
    return "\n".join(lines)

def build_locations_page():
    cards_html = "\n".join(county_card(c) for c in COUNTIES)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
    <meta name="description" content="The Fix Wizard serves all 21 counties across New Jersey — from Bergen to Cape May. Find licensed handyman, drywall, painting, plumbing, and more in your area.">
    <title>Service Areas in New Jersey | The Fix Wizard — All 21 Counties</title>
    <link rel="stylesheet" href="../css/tw.css">
    <link rel="stylesheet" href="../css/custom.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "The Fix Wizard",
      "description": "Professional home repair services across all 21 counties in New Jersey",
      "url": "https://thefixwizard.com",
      "telephone": "(555) 123-4567",
      "areaServed": {{"@type": "State", "name": "New Jersey"}}
    }}
    </script>
</head>
<body>

{navbar_html(1, active="locations")}

    <!-- HERO -->
    <section class="sp-hero" style="padding-bottom:56px;">
        <div class="container" style="text-align:center;">
            <div class="sp-hero-tag"><i class="fas fa-map-marker-alt"></i> Service Areas</div>
            <h1 class="sp-hero-title">We Serve All of <span class="text-accent">New Jersey</span></h1>
            <p class="sp-hero-desc" style="max-width:640px;margin:0 auto 32px;">From Bergen County in the north to Cape May in the south, The Fix Wizard brings licensed, same-day home repair to every corner of the Garden State. Licensed &amp; insured. Free estimates.</p>
            <div style="display:flex;align-items:center;justify-content:center;gap:40px;flex-wrap:wrap;">
                <div style="text-align:center;">
                    <span style="display:block;font-size:2.2rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">21</span>
                    <span style="color:rgba(255,255,255,.6);font-size:13px;margin-top:2px;display:block;">Counties Served</span>
                </div>
                <div style="width:1px;height:48px;background:rgba(255,255,255,.2);"></div>
                <div style="text-align:center;">
                    <span style="display:block;font-size:2.2rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">8</span>
                    <span style="color:rgba(255,255,255,.6);font-size:13px;margin-top:2px;display:block;">Core Services</span>
                </div>
                <div style="width:1px;height:48px;background:rgba(255,255,255,.2);"></div>
                <div style="text-align:center;">
                    <span style="display:block;font-size:1.4rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">Same-Day</span>
                    <span style="color:rgba(255,255,255,.6);font-size:13px;margin-top:2px;display:block;">Available</span>
                </div>
            </div>
        </div>
    </section>

    <!-- COUNTY GRID -->
    <section class="loc-section">
        <!-- decorative background pins -->
        <div class="loc-bg-pin" style="right:-40px;top:40px;width:320px;height:400px;">
            <svg viewBox="0 0 100 130" fill="#0d1b4b" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;"><path d="M50 0C22.4 0 0 22.4 0 50c0 37.5 50 80 50 80S100 87.5 100 50C100 22.4 77.6 0 50 0z"/><circle cx="50" cy="50" r="19" fill="white" fill-opacity=".6"/></svg>
        </div>
        <div class="loc-bg-pin" style="left:-60px;bottom:80px;width:280px;height:350px;">
            <svg viewBox="0 0 100 130" fill="#0d1b4b" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;"><path d="M50 0C22.4 0 0 22.4 0 50c0 37.5 50 80 50 80S100 87.5 100 50C100 22.4 77.6 0 50 0z"/><circle cx="50" cy="50" r="19" fill="white" fill-opacity=".6"/></svg>
        </div>
        <div class="container" style="position:relative;z-index:1;">
            <div style="text-align:center;margin-bottom:48px;">
                <h2 style="font-size:clamp(22px,3vw,30px);font-weight:800;color:#0d1b4b;margin-bottom:8px;">Choose Your County</h2>
                <p style="color:#64748b;font-size:15px;">Select a county below to see all available services in your area</p>
            </div>
            <div class="loc-grid">
{cards_html}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>Need a Handyman Anywhere in New Jersey?</h2>
                <p>Free estimates across all 21 NJ counties. Licensed &amp; insured. Same-day available.</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15551234567" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Send Message</a>
            </div>
        </div>
    </section>

{footer_html(1)}

    <script type="module" src="../js/service-page.js"></script>
</body>
</html>"""

    out_dir = os.path.join(ROOT, "locations")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  ✓  locations/index.html")


# ─── 2. SERVICE AREA PAGES ──────────────────────────────────────────────────────

SERVICE_INTROS = {
    "Drywall Repair":     ("walls, cracks, holes, water-stained drywall, and texture matching",
                           "cracked walls, water-stained drywall, or holes that need a professional finish",
                           "patches, water damage repair, texture matching, and smooth finishing"),
    "Garage Door Repair": ("broken springs, off-track panels, faulty openers, and full door replacements",
                           "a garage door that won't open, makes grinding noises, or has a broken spring",
                           "spring replacement, panel repair, opener service, cable repair, and full replacements"),
    "Painting":           ("interior and exterior painting, trim work, and cabinet refinishing",
                           "faded walls, peeling paint, or rooms that need a fresh new look",
                           "interior painting, exterior painting, trim work, and touch-up services"),
    "Door Repair":        ("sticking doors, broken hinges, damaged frames, and full door replacements",
                           "a door that sticks, drags, or no longer closes securely",
                           "hinge repair, frame adjustment, weatherstripping, and full door replacements"),
    "Chimney Repair":     ("chimney sweeping, tuckpointing, crown repair, and masonry restoration",
                           "a crumbling chimney, damaged mortar, or a flue that needs inspecting",
                           "chimney cleaning, tuckpointing, crown repair, cap installation, and masonry work"),
    "Electrical Repair":  ("outlet repair, switch replacement, fixture installation, and panel assessment",
                           "dead outlets, flickering lights, or switches that need replacing",
                           "outlet repair, switch replacement, fixture installation, and minor electrical work"),
    "Plumbing Repair":    ("leaky faucets, running toilets, drain clearing, and fixture replacement",
                           "a dripping faucet, slow drain, or toilet that keeps running",
                           "faucet repair, toilet service, drain clearing, and fixture replacement"),
    "Furniture Assembly": ("flat-pack assembly, TV mounting, shelving, and desk setup",
                           "flat-pack furniture waiting to be built, or a TV that needs mounting",
                           "flat-pack assembly (IKEA, Wayfair, Amazon), TV mounting, shelving, and desk setup"),
}

def area_page_html(svc, county):
    sn = svc["name"]
    cn = county["name"]
    slug = county["slug"]
    prefix = svc["slug_prefix"]
    towns_raw = county["towns"].replace(" · ", ", ")
    intro_a, intro_b, intro_c = SERVICE_INTROS[sn]
    parent_url = f'../../{svc["parent"]}/'
    parent_label = svc["parent_label"]
    page_title = f'{sn} in {cn}, NJ | The Fix Wizard'
    meta_desc = f'Expert {sn.lower()} in {cn}, NJ. Licensed & insured technicians serving {towns_raw} and surrounding areas. Free estimate — same-day available.'
    h1 = f'Expert {sn} in {cn}, New Jersey'
    other_svcs_html = "\n".join(
        f'                        <a href="../../{s["slug_prefix"]}-{slug}/"><i class="fas {s["icon"]}"></i> {s["name"]}</a>'
        for s in SERVICES if s["name"] != sn
    )
    schema = f"""{{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "{sn}",
      "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard"}},
      "areaServed": {{"@type": "AdministrativeArea", "name": "{cn}, New Jersey"}},
      "description": "{meta_desc}"
    }}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
    <meta name="description" content="{meta_desc}">
    <title>{page_title}</title>
    <link rel="stylesheet" href="../../css/tw.css">
    <link rel="stylesheet" href="../../css/custom.css">
    <script type="application/ld+json">{schema}</script>
</head>
<body>

{navbar_html(2)}

    <!-- HERO -->
    <section class="sp-hero" style="padding-bottom:52px;">
        <div class="container">
            <nav class="blog-breadcrumb">
                <a href="../../">Home</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../locations/">Locations</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../">{cn}</a>
                <i class="fas fa-chevron-right"></i>
                <span>{sn}</span>
            </nav>
            <h1 class="sp-hero-title" style="margin-top:20px;">{h1}</h1>
            <p class="sp-hero-desc">Licensed &amp; insured {sn.lower()} serving {towns_raw} and all of {cn}. Free estimates — same-day appointments available.</p>
        </div>
    </section>

    <!-- CONTENT -->
    <section class="area-content">
        <div class="container">
            <div class="area-layout">

                <!-- BODY -->
                <div class="area-body">
                    <h2>{sn} in {cn} — What We Do</h2>
                    <p>If you're a homeowner in {cn} dealing with {intro_b}, The Fix Wizard is your local solution. We cover {towns_raw}, and every community in between — with same-day availability and a commitment to quality work at transparent prices.</p>
                    <p>{cn}'s housing stock presents its own set of challenges. Whether you're in a post-war split-level, a newer development, or a historic property near downtown, our technicians have the experience to handle your specific situation correctly the first time.</p>

                    <h2>Our {sn} Services in {cn}</h2>
                    <p>We offer comprehensive {sn.lower()} covering {intro_c}. Every job comes with a free estimate, honest pricing, and a clean worksite when we leave.</p>
                    <ul>
                        <li>Licensed &amp; insured in New Jersey</li>
                        <li>Free estimates — no commitment required</li>
                        <li>Same-day appointments available</li>
                        <li>Transparent pricing, no hidden charges</li>
                        <li>Serving all towns across {cn}</li>
                    </ul>

                    <h2>Why {cn} Homeowners Choose The Fix Wizard</h2>
                    <p>We're not a national chain — we're a local New Jersey team that has worked in hundreds of {cn} homes. We know the housing types, the common issues, and the right fix for your specific situation. We show up on time, explain what needs doing, and get it done right.</p>
                    <p>Every technician is background-checked, licensed, and carries full liability insurance. We stand behind every repair with a satisfaction guarantee.</p>

                    <h2>Service Areas Within {cn}</h2>
                    <p>We serve homeowners across all of {cn}, including {towns_raw}, and the surrounding townships and boroughs. Not sure if we cover your area? Give us a call — we likely do.</p>
                </div>

                <!-- SIDEBAR -->
                <aside class="area-sidebar">
                    <div class="area-cta-box">
                        <h3>Get a Free Estimate</h3>
                        <p>Available same-day across {cn}. Licensed &amp; insured. No obligation.</p>
                        <a href="tel:+15551234567" class="btn btn-primary"><i class="fas fa-phone"></i> (555) 123-4567</a>
                        <a href="../../#contact" class="btn btn-outline-white">Send a Message</a>
                    </div>

                    <div class="area-trust-box">
                        <h3>Why Trust Us</h3>
                        <ul class="area-trust-list">
                            <li><i class="fas fa-shield-halved"></i> Licensed &amp; Insured in NJ</li>
                            <li><i class="fas fa-calendar-check"></i> Same-Day Available</li>
                            <li><i class="fas fa-tag"></i> Free Estimates</li>
                            <li><i class="fas fa-star"></i> 4.9★ Google Rating</li>
                            <li><i class="fas fa-clock"></i> Mon–Sat 7am–7pm</li>
                        </ul>
                    </div>

                    <div class="area-services-box">
                        <h3>More Services in {cn}</h3>
                        <div class="area-svc-list">
{other_svcs_html}
                        </div>
                    </div>

                    <div class="area-services-box">
                        <h3>All NJ Service Pages</h3>
                        <div class="area-svc-list">
                            <a href="{parent_url}"><i class="fas {svc['icon']}"></i> {parent_label}</a>
                            <a href="../../locations/"><i class="fas fa-map-marker-alt"></i> All Service Areas</a>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>{sn} in {cn}? We've Got You.</h2>
                <p>Free estimates across all of {cn}. Licensed &amp; insured. Same-day available.</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15551234567" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Quote</a>
            </div>
        </div>
    </section>

{footer_html(2)}

    <script type="module" src="../../js/service-page.js"></script>
</body>
</html>"""


def build_area_pages():
    count = 0
    for county in COUNTIES:
        slug = county["slug"]
        # create a county hub directory that redirects to the locations page
        # and individual service pages
        for svc in SERVICES:
            dir_name = f'{svc["slug_prefix"]}-{slug}'
            out_dir = os.path.join(ROOT, dir_name)
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "index.html")
            with open(path, "w") as f:
                f.write(area_page_html(svc, county))
            count += 1
    print(f"  ✓  {count} service-area pages generated")


# ─── 3. PATCH EXISTING NAVBARS ──────────────────────────────────────────────────

def patch_navbar(filepath, depth):
    with open(filepath, "r") as f:
        content = f.read()

    # Skip if already patched
    if "locations/" in content and "Locations" in content:
        return False

    prefix = "../" * depth

    # Desktop nav — insert after Contact li
    desktop_contact = f'<li><a href="{prefix}#contact" class="nav-link">Contact</a></li>'
    desktop_contact_active = f'<li><a href="{prefix}#contact" class="nav-link active">Contact</a></li>'
    locations_desktop = f'\n                <li><a href="{prefix}locations/" class="nav-link">Locations</a></li>'

    if desktop_contact in content:
        content = content.replace(desktop_contact, desktop_contact + locations_desktop, 1)
    elif desktop_contact_active in content:
        content = content.replace(desktop_contact_active, desktop_contact_active + locations_desktop, 1)

    # Mobile nav — insert after Contact mobile li
    mobile_contact = f'<li><a href="{prefix}#contact" class="mobile-link">Contact</a></li>'
    locations_mobile = f'\n            <li><a href="{prefix}locations/" class="mobile-link">Locations</a></li>'

    if mobile_contact in content:
        content = content.replace(mobile_contact, mobile_contact + locations_mobile, 1)

    with open(filepath, "w") as f:
        f.write(content)
    return True


def patch_all_navbars():
    patched = 0
    # Service pages (depth 1)
    service_dirs = [
        "drywall-repair-new-jersey", "garage-door-repair-new-jersey",
        "furniture-assembly-new-jersey", "painting-new-jersey",
        "door-repair-new-jersey", "chimney-masonry-new-jersey",
        "electrical-repair-new-jersey", "plumbing-repair-new-jersey",
        "mounting-installation-new-jersey",
    ]
    for d in service_dirs:
        path = os.path.join(ROOT, d, "index.html")
        if os.path.exists(path):
            if patch_navbar(path, depth=1):
                patched += 1

    # Blog posts (depth 2)
    for d in service_dirs:
        service_path = os.path.join(ROOT, d)
        if not os.path.isdir(service_path):
            continue
        for sub in os.listdir(service_path):
            blog_path = os.path.join(service_path, sub, "index.html")
            if os.path.exists(blog_path):
                if patch_navbar(blog_path, depth=2):
                    patched += 1

    print(f"  ✓  {patched} existing pages patched with Locations nav link")


# ─── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building locations hub page...")
    build_locations_page()

    print("Generating service area pages...")
    build_area_pages()

    print("Patching existing navbars...")
    patch_all_navbars()

    print("\nDone. Run: ./node_modules/.bin/tailwind -i css/input.css -o css/tw.css --minify")
