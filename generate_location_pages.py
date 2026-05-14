#!/usr/bin/env python3
"""Generates /new-jersey/ and /cleveland-ohio/ location landing pages."""

import os, base64

ROOT = os.path.dirname(os.path.abspath(__file__))

# Load favicon base64 for inline embedding
try:
    with open(os.path.join(ROOT, "favicon-32.png"), "rb") as f:
        FAVICON_B64 = base64.b64encode(f.read()).decode()
    FAVICON_TAG = f'<link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{FAVICON_B64}">'
except:
    FAVICON_TAG = '<link rel="icon" href="/favicon.ico" type="image/x-icon">'

GFONTS = "https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"
FA     = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"

PIN_SVG = '<svg viewBox="0 0 24 30" fill="none" aria-hidden="true"><path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 18 12 18S24 21 24 12C24 5.4 18.6 0 12 0z" fill="#FF6B35"/><circle cx="12" cy="12" r="4.5" fill="white"/></svg>'

NJ_COUNTIES = [
    {"name": "Bergen County",     "slug": "bergen-county-nj",     "towns": "Hackensack · Paramus · Fort Lee · Englewood",             "desc": "NJ's most populous county — dense suburban neighborhoods with aging homes in need of expert repair."},
    {"name": "Essex County",      "slug": "essex-county-nj",      "towns": "Newark · Montclair · Bloomfield · Maplewood",             "desc": "From Newark's urban housing to Montclair's Victorian homes — skilled repairs for every property type."},
    {"name": "Middlesex County",  "slug": "middlesex-county-nj",  "towns": "Edison · New Brunswick · Woodbridge · Piscataway",       "desc": "Fast-growing county with diverse housing stock, from ranch homes to newer developments."},
    {"name": "Monmouth County",   "slug": "monmouth-county-nj",   "towns": "Red Bank · Freehold · Asbury Park · Middletown",         "desc": "Shore county with coastal homes, salt-air wear, and a mix of historic and modern properties."},
    {"name": "Morris County",     "slug": "morris-county-nj",     "towns": "Morristown · Parsippany · Madison · Rockaway",           "desc": "Wooded suburbs with colonial and split-level homes common across northern New Jersey."},
    {"name": "Hudson County",     "slug": "hudson-county-nj",     "towns": "Jersey City · Hoboken · Bayonne · Union City",           "desc": "Densely packed brownstones, townhouses, and multi-family buildings in one of NJ's busiest counties."},
    {"name": "Union County",      "slug": "union-county-nj",      "towns": "Elizabeth · Westfield · Summit · Plainfield",            "desc": "Central NJ county blending affluent suburbs with working-class neighborhoods — we serve them all."},
    {"name": "Ocean County",      "slug": "ocean-county-nj",      "towns": "Toms River · Lakewood · Brick · Jackson",                "desc": "Shore and inland county where storm damage repairs and coastal home maintenance are a year-round need."},
    {"name": "Somerset County",   "slug": "somerset-county-nj",   "towns": "Bridgewater · Somerville · Bound Brook · Raritan",       "desc": "Upscale suburban county with well-maintained homes that still benefit from expert professional repair."},
    {"name": "Passaic County",    "slug": "passaic-county-nj",    "towns": "Paterson · Clifton · Wayne · Pompton Lakes",             "desc": "Busy northern county with dense residential neighborhoods and older building stock requiring skilled upkeep."},
    {"name": "Camden County",     "slug": "camden-county-nj",     "towns": "Cherry Hill · Voorhees · Haddonfield · Camden",          "desc": "South Jersey's most populous county — rowhouses, ranches, and suburban homes served with care."},
    {"name": "Burlington County", "slug": "burlington-county-nj", "towns": "Moorestown · Medford · Evesham · Mount Holly",           "desc": "Large central county with historic towns and newer suburban developments throughout the Pinelands."},
    {"name": "Mercer County",     "slug": "mercer-county-nj",     "towns": "Trenton · Princeton · Hamilton · Lawrence",              "desc": "From Trenton's urban housing to Princeton's prestigious estates — expert repairs across the board."},
    {"name": "Atlantic County",   "slug": "atlantic-county-nj",   "towns": "Atlantic City · Egg Harbor · Galloway · Absecon",        "desc": "Shore and casino country with aging properties and high demand for reliable home repair services."},
    {"name": "Gloucester County", "slug": "gloucester-county-nj", "towns": "Woodbury · Deptford · Washington Twp · Glassboro",       "desc": "Growing suburb of Philadelphia with a range of home styles and steady demand for quality repairs."},
    {"name": "Cumberland County", "slug": "cumberland-county-nj", "towns": "Vineland · Bridgeton · Millville · Commercial Twp",      "desc": "South Jersey's rural county with older housing stock and unique repair needs we're equipped to handle."},
    {"name": "Cape May County",   "slug": "cape-may-county-nj",   "towns": "Cape May City · Wildwood · Ocean City · Avalon",         "desc": "Vacation homes, Victorian properties, and shore houses — seasonal and year-round maintenance covered."},
    {"name": "Warren County",     "slug": "warren-county-nj",     "towns": "Hackettstown · Washington · Phillipsburg · Belvidere",   "desc": "Rural-suburban mix with older farmhouses and modest residential neighborhoods throughout the valley."},
    {"name": "Sussex County",     "slug": "sussex-county-nj",     "towns": "Newton · Sparta · Vernon · Hardyston",                   "desc": "NJ's northernmost county — mountain-area homes with weather-related wear and older construction."},
    {"name": "Hunterdon County",  "slug": "hunterdon-county-nj",  "towns": "Flemington · Clinton · Lambertville · Raritan",          "desc": "Scenic rural county with historic farmhouses, horse properties, and charming older homes."},
    {"name": "Salem County",      "slug": "salem-county-nj",      "towns": "Salem City · Woodstown · Carneys Point · Penns Grove",  "desc": "South Jersey's smallest county — older housing requiring skilled, attentive home repair professionals."},
]

CLEVELAND_SUBURBS = [
    {"name": "Cleveland",          "slug": "cleveland-oh",          "towns": "Downtown · Ohio City · Tremont",              "desc": "Ohio's second-largest city — century-old housing stock with high demand for chimney and handyman work."},
    {"name": "Cleveland Heights",  "slug": "cleveland-heights-oh",  "towns": "Cedar Lee · Coventry · Noble · Taylor",        "desc": "Historic inner-ring suburb with Tudor Revivals and Colonials built in the 1920s–1940s."},
    {"name": "Lakewood",           "slug": "lakewood-oh",           "towns": "Gold Coast · Birdtown · Downtown Lakewood",    "desc": "Dense west-side suburb with craftsman bungalows and brick Colonials — one of Ohio's most repair-active communities."},
    {"name": "Parma",              "slug": "parma-oh",              "towns": "Parma Center · Ridgewood · Greenbriar",        "desc": "Ohio's seventh-largest city with postwar ranches and cape cods needing regular upkeep."},
    {"name": "Mentor",             "slug": "mentor-oh",             "towns": "Mentor-on-the-Lake · City Center",             "desc": "Growing northeastern suburb with diverse housing from mid-century builds to newer developments."},
    {"name": "Strongsville",       "slug": "strongsville-oh",       "towns": "Old Town · SouthPark · Northwood",             "desc": "Upscale southwestern suburb with established neighborhoods and growing demand for premium home services."},
    {"name": "Westlake",           "slug": "westlake-oh",           "towns": "Crocker Park · Bradley · Dover Center",        "desc": "Affluent western suburb with well-established neighborhoods and active home improvement market."},
    {"name": "Beachwood",          "slug": "beachwood-oh",          "towns": "Chagrin Highlands · Cedar Center",             "desc": "Prosperous eastern suburb with custom homes and high expectations for service quality."},
    {"name": "Solon",              "slug": "solon-oh",              "towns": "Solon Square · Miles Road · Aurora Road",       "desc": "High-income southeastern suburb with newer construction and older custom homes."},
    {"name": "North Olmsted",      "slug": "north-olmsted-oh",      "towns": "Butternut Ridge · Great Northern",              "desc": "Western suburb with postwar housing and strong demand for chimney and handyman services."},
    {"name": "Rocky River",        "slug": "rocky-river-oh",        "towns": "Detroit Road · Wooster Road · Lake Road",      "desc": "Charming lakefront suburb with historic homes and waterfront properties requiring specialized care."},
    {"name": "Euclid",             "slug": "euclid-oh",             "towns": "Euclid Beach · Nottingham · Shore Cultural",   "desc": "Eastern suburb with industrial-era housing demanding skilled masonry and handyman repair work."},
    {"name": "Shaker Heights",     "slug": "shaker-heights-oh",     "towns": "Van Aken · Ludlow · Onaway · Moreland",        "desc": "Architecturally significant planned community — Tudor Revivals and Colonials with premium masonry demand."},
    {"name": "Bay Village",        "slug": "bay-village-oh",        "towns": "Bay Square · Wolf Road · Porter Creek",        "desc": "Lakefront suburb with vintage properties and coastal exposure that accelerates masonry wear."},
    {"name": "Avon Lake",          "slug": "avon-lake-oh",          "towns": "Walker Road · Moore Road · Lake Road",         "desc": "Growing western suburb with lakeshore homes and newer residential developments."},
    {"name": "Fairview Park",      "slug": "fairview-park-oh",      "towns": "Lorain Road · Mastick Road",                   "desc": "Established mid-century suburb with active home renovation and community investment in property upkeep."},
    {"name": "Broadview Heights",  "slug": "broadview-heights-oh",  "towns": "Royalton Road · Broadview Road",               "desc": "Upscale southern suburb with custom builds and growing families investing in quality home services."},
    {"name": "North Royalton",     "slug": "north-royalton-oh",     "towns": "Royalton Road · State Road · York Road",       "desc": "Suburban community with consistent demand for chimney and handyman repairs."},
    {"name": "Brunswick",          "slug": "brunswick-oh",          "towns": "Center Road · Pearl Road · Grafton Road",      "desc": "Growing suburban community with a strong handyman and chimney service market."},
    {"name": "Chardon",            "slug": "chardon-oh",            "towns": "Chardon Square · South Street",                "desc": "Small-town Geauga County community with older housing and severe winters that accelerate chimney wear."},
]

LOCATIONS = [
    {
        "slug":       "new-jersey",
        "name":       "New Jersey",
        "short":      "NJ",
        "h1_chimney": "Chimney Repair &amp; Masonry Services in New Jersey",
        "h1_handyman":"Handyman Services in New Jersey",
        "hero_title": "Chimney &amp; Handyman Services<br><span class=\"text-orange\">in <span class=\"lightning-word\">New Jersey</span></span>",
        "hero_sub":   "NJ's trusted specialists for chimney repair, masonry, and handyman services. Licensed &amp; insured, same-day available across all 21 counties — from Bergen to Cape May.",
        "meta_desc":  "Expert chimney repair, masonry, and handyman services across New Jersey. Serving all 21 NJ counties. Licensed & insured, same-day available. Free estimates.",
        "tab_title":  "Chimney &amp; Handyman Services in New Jersey | The Fix Wizard",
        "badge":      "Serving All 21 NJ Counties",
        "areas_title":"Counties We Serve in New Jersey",
        "areas":      ["Bergen County", "Essex County", "Middlesex County", "Monmouth County", "Morris County",
                       "Hudson County", "Union County", "Ocean County", "Somerset County", "Passaic County",
                       "Camden County", "Burlington County", "Mercer County", "Atlantic County", "Gloucester County",
                       "Cumberland County", "Cape May County", "Warren County", "Sussex County", "Hunterdon County", "Salem County"],
        "chimney_link": "../chimney-masonry-new-jersey/",
        "handyman_link":"../handyman-services-new-jersey/",
        "chimney_desc": "From chimney sweeping and tuckpointing to crown repair and full liner installation — we've serviced hundreds of NJ chimneys across Bergen, Morris, Essex, Monmouth, and all 21 counties.",
        "handyman_desc":"Drywall, painting, plumbing, electrical, doors, furniture assembly and more — one call covers your entire repair list across every NJ county.",
        "card_areas":   NJ_COUNTIES,
        "card_h2":      "Services by County in New Jersey",
        "card_desc":    "Select your county below to see chimney repair and handyman services available in your area.",
        "card_count":   "21 Counties",
        "faqs": [
            ("Do you offer chimney services in all NJ counties?",
             "Yes. The Fix Wizard serves all 21 New Jersey counties for chimney repair and masonry — from Bergen and Essex in the north to Camden, Atlantic, and Cape May in the south."),
            ("How much does chimney repair cost in New Jersey?",
             "Chimney sweeping in NJ typically costs $150–$300. Tuckpointing ranges from $500–$3,000. Crown repair runs $200–$800. Liner installation starts at $1,500. We provide free, itemized estimates with no obligation."),
            ("Can I get same-day handyman services in New Jersey?",
             "Yes. We offer same-day handyman appointments across New Jersey. Call (555) 123-4567 for urgent requests and we will dispatch a licensed technician as quickly as possible."),
            ("Are you licensed for home repair work in New Jersey?",
             "Yes. The Fix Wizard is fully licensed and insured in the state of New Jersey for all chimney, masonry, and handyman services we offer. We carry liability insurance on every job."),
            ("What handyman services do you offer in New Jersey?",
             "Our NJ handyman services include drywall repair, interior and exterior painting, door repair and installation, furniture assembly, TV mounting, light electrical, light plumbing, weatherstripping, caulking, and general home repairs."),
        ],
        "schema_area": '{"@type": "State", "name": "New Jersey"}',
        "url_path":    "https://thefixwizard.com/new-jersey/",
    },
    {
        "slug":       "cleveland-ohio",
        "name":       "Cleveland, Ohio",
        "short":      "Cleveland",
        "h1_chimney": "Chimney Repair &amp; Masonry Services in Cleveland, Ohio",
        "h1_handyman":"Handyman Services in Cleveland, Ohio",
        "hero_title": "Chimney &amp; Handyman Services<br><span class=\"text-orange\">in <span class=\"lightning-word\">Cleveland, Ohio</span></span>",
        "hero_sub":   "Cleveland's trusted specialists for chimney repair, masonry, and handyman services. Licensed &amp; insured, same-day available across the greater Cleveland area.",
        "meta_desc":  "Expert chimney repair, masonry, and handyman services in Cleveland, Ohio. Serving Cleveland and surrounding suburbs. Licensed & insured, same-day available. Free estimates.",
        "tab_title":  "Chimney &amp; Handyman Services in Cleveland, Ohio | The Fix Wizard",
        "badge":      "Serving Greater Cleveland, Ohio",
        "areas_title":"Areas We Serve in Greater Cleveland",
        "areas":      ["Cleveland", "Cleveland Heights", "Lakewood", "Parma", "Mentor",
                       "Strongsville", "Westlake", "Beachwood", "Solon", "North Olmsted",
                       "Rocky River", "Euclid", "Shaker Heights", "Bay Village", "Avon Lake",
                       "Fairview Park", "Broadview Heights", "North Royalton", "Brunswick", "Chardon"],
        "chimney_link": "../chimney-masonry-new-jersey/",
        "handyman_link":"../handyman-services-new-jersey/",
        "chimney_desc": "Cleveland's older housing stock and harsh winters create demanding chimney conditions. We handle chimney sweeping, tuckpointing, crown repair, liner installation, and full masonry restoration across the greater Cleveland area.",
        "handyman_desc":"From Lakewood to Mentor, our licensed handymen tackle drywall, painting, plumbing, electrical, doors, furniture assembly, TV mounting, and any other repair on your list.",
        "card_areas":   CLEVELAND_SUBURBS,
        "card_h2":      "Services by Area in Greater Cleveland",
        "card_desc":    "Select your area below to see chimney repair and handyman services available near you.",
        "card_count":   "20 Areas",
        "faqs": [
            ("Do you offer chimney services in Cleveland and surrounding suburbs?",
             "Yes. The Fix Wizard serves Cleveland and the greater Cleveland area including Cleveland Heights, Lakewood, Parma, Mentor, Strongsville, Westlake, Beachwood, Solon, and more. Call us to confirm coverage in your specific area."),
            ("How much does chimney repair cost in Cleveland, Ohio?",
             "Chimney sweeping in Cleveland typically costs $150–$300. Tuckpointing ranges from $500–$3,000 depending on the extent of damage. Crown repair runs $200–$800. Cleveland's freeze-thaw winters accelerate mortar deterioration, so annual inspections are strongly recommended."),
            ("Can I get same-day handyman services in Cleveland?",
             "Yes. We offer same-day handyman appointments across the greater Cleveland area. Call (555) 123-4567 for urgent repairs and we will dispatch a licensed technician as quickly as possible."),
            ("Are you licensed for home repair work in Ohio?",
             "Yes. The Fix Wizard is fully licensed and insured in Ohio for all chimney, masonry, and handyman services. We carry liability insurance on every job and all technicians are background-checked."),
            ("What handyman services do you offer in Cleveland?",
             "Our Cleveland handyman services include drywall repair and patching, interior and exterior painting, door repair and installation, furniture assembly, TV mounting, light electrical, light plumbing, weatherstripping, caulking, and general home repairs across the greater Cleveland area."),
        ],
        "schema_area": '{"@type": "City", "name": "Cleveland", "containedInPlace": {"@type": "State", "name": "Ohio"}}',
        "url_path":    "https://thefixwizard.com/cleveland-ohio/",
    },
]


def build_area_cards(loc):
    cards = []
    for a in loc["card_areas"]:
        slug = a["slug"]
        cards.append(f"""\
                <div class="loc-card">
                    <div class="loc-card__header">
                        <div class="loc-pin-icon">{PIN_SVG}</div>
                        <div>
                            <h3 class="loc-card__name">{a['name']}</h3>
                            <p class="loc-card__towns">{a['towns']}</p>
                        </div>
                    </div>
                    <p class="loc-card__desc">{a['desc']}</p>
                    <div class="loc-card__divider"></div>
                    <div class="loc-services-grid">
                        <a href="../locations/chimney-repair-in-{slug}/" class="loc-svc-btn"><i class="fas fa-fire"></i> Chimney Repair</a>
                        <a href="../locations/handyman-services-in-{slug}/" class="loc-svc-btn"><i class="fas fa-screwdriver-wrench"></i> Handyman Services</a>
                    </div>
                </div>""")
    return "\n".join(cards)


def build_page(loc):
    faqs_html = ""
    for q, a in loc["faqs"]:
        faqs_html += f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false">
                        <span>{q}</span>
                        <i class="fas fa-plus"></i>
                    </button>
                    <div class="faq-answer" aria-hidden="true">
                        <p>{a}</p>
                    </div>
                </div>"""

    faq_schema_items = ",\n          ".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a.replace(chr(34), chr(39))}"}}}}'
        for q, a in loc["faqs"]
    )

    areas_html = "".join(
        f'<span class="inline-flex items-center gap-1.5 bg-white border border-slate-200 rounded-full px-3.5 py-1.5 text-[13px] font-medium text-navy-900"><i class="fas fa-location-dot text-orange text-[11px]"></i>{a}</span>'
        for a in loc["areas"]
    )

    cards_html = build_area_cards(loc)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {FAVICON_TAG}
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <meta name="description" content="{loc['meta_desc']}">
    <title>{loc['tab_title']}</title>
    <style>:root{{--nav-h:150px}}*,*::before,*::after{{box-sizing:border-box}}body{{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}}body.no-scroll{{overflow:hidden}}a{{text-decoration:none;color:inherit}}.reveal{{opacity:0;transform:translateY(28px)}}.sp-hero,.hero{{background-color:#091236;color:#fff}}.mobile-menu{{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}}.mobile-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}}.faq-answer{{max-height:0;overflow:hidden}}#navbar{{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}}.loader{{position:fixed;inset:0;background:#0d1b4b;z-index:9999;display:flex;align-items:center;justify-content:center}}@media(max-width:768px){{:root{{--nav-h:96px}}}}</style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="{GFONTS}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{GFONTS}"></noscript>
    <link rel="preload" href="{FA}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{FA}"></noscript>
    <link rel="preload" href="../css/tw.css" as="style">
    <link rel="stylesheet" href="../css/tw.css">
    <link rel="preload" href="../css/custom.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="../css/custom.css"></noscript>
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": "The Fix Wizard",
        "description": "{loc['meta_desc']}",
        "url": "{loc['url_path']}",
        "telephone": "(555) 123-4567",
        "email": "hello@handypro.com",
        "priceRange": "$$",
        "openingHoursSpecification": {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
          "opens": "07:00",
          "closes": "19:00"
        }},
        "areaServed": {loc['schema_area']}
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {faq_schema_items}
        ]
      }}
    ]
    </script>
</head>
<body>

    <nav id="navbar" class="navbar">
        <div class="container nav-container">
            <a href="../" class="logo"><img src="../assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img" width="199" height="110"></a>
            <ul class="nav-links">
                <li><a href="../" class="nav-link">Home</a></li>
                <li><a href="../#services" class="nav-link">Services</a></li>
                <li><a href="../#why-us" class="nav-link">About</a></li>
                <li><a href="../#contact" class="nav-link">Contact</a></li>
                <li class="nav-dropdown">
                    <a href="../locations/" class="nav-link flex items-center gap-1.5" style="color:#FF6B35;">Locations <i class="fas fa-chevron-down text-[10px] opacity-50 mt-px"></i></a>
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
    <div class="mobile-overlay" id="mobileOverlay"></div>

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">

                <!-- LEFT -->
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-location-dot text-orange text-[11px]"></i>
                        <span>{loc['badge']}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(32px,5vw,64px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        {loc['hero_title']}
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-6 max-w-[560px]">
                        {loc['hero_sub']}
                    </p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-fire text-orange text-[12px]"></i> Chimney &amp; Masonry
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-screwdriver-wrench text-orange text-[12px]"></i> Handyman Services
                        </div>
                    </div>
                    <div class="flex items-center gap-3 mb-12 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="tel:+15551234567" class="btn btn-primary btn-lg">
                            <i class="fas fa-phone"></i> Call Now
                        </a>
                        <a href="../#contact" class="btn btn-outline btn-lg">
                            <i class="fas fa-calendar-alt"></i> Free Estimate
                        </a>
                    </div>
                    <div class="w-full h-px bg-white/10 mb-8"></div>
                    <div class="flex items-center gap-8 flex-wrap justify-center tab:justify-start hero-stats">
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-target="500">0</span>+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Projects Done</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-target="10">0</span>+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Years Exp</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-target="98">0</span>%</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Satisfaction</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-target="2">0</span></div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Specialties</div>
                        </div>
                    </div>
                </div>

                <!-- RIGHT -->
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[520px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-6">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas fa-house-chimney-crack"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">Get a Free Estimate</div>
                                <p class="text-[13px] text-white/50">Response within 2 hours · No obligation</p>
                            </div>
                        </div>
                        <div class="flex flex-col gap-3">
                            <a href="{loc['chimney_link']}" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-fire"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">Chimney &amp; Masonry</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">Sweeping · Tuckpointing · Crown Repair · Liner</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                            <a href="{loc['handyman_link']}" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-screwdriver-wrench"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">Handyman Services</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">Drywall · Painting · Plumbing · Electrical &amp; More</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                        </div>
                        <a href="../#contact" class="btn btn-primary btn-full">
                            <i class="fas fa-paper-plane"></i> Request a Quote
                        </a>
                        <div class="flex gap-3 pt-1 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-shield-halved text-orange text-[13px]"></i><span>Licensed &amp; Insured</span></div>
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-clock text-orange text-[13px]"></i><span>Same Day Available</span></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- Sparkles -->
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
        </div>
    </section>

    <!-- SERVICES -->
    <section class="py-20" style="background:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">{loc['name']}</span>
                <h2 class="section-title">Our <span class="text-accent">Services</span> in {loc['name']}</h2>
                <p class="section-desc">Two focused specialties — chimney &amp; masonry and handyman services — delivered by licensed, insured technicians across {loc['name']}.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-[860px] mx-auto">
                <div class="group relative bg-white rounded-card border border-slate-200 flex flex-col overflow-hidden cursor-pointer transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.22)] hover:border-transparent reveal">
                    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-dark via-orange to-orange-light scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-left rounded-b-card z-10"></div>
                    <img src="../assets/images/chimney-repair-in-new-jersey.webp" alt="Chimney repair and masonry in {loc['name']}" class="w-full h-[220px] object-cover object-top shrink-0 transition-transform duration-500 group-hover:scale-105" width="800" height="220" loading="lazy">
                    <div class="p-6 flex flex-col gap-3 flex-1">
                        <div class="flex items-center gap-3">
                            <div class="w-9 h-9 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-fire text-orange text-[15px]"></i></div>
                            <h2 class="text-[18px] font-bold text-navy-900">{loc['h1_chimney']}</h2>
                        </div>
                        <p class="text-sm text-slate-500 leading-relaxed flex-1">{loc['chimney_desc']}</p>
                        <ul class="flex flex-col gap-1 text-sm text-slate-600">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Chimney sweeping &amp; inspection</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Tuckpointing &amp; mortar repair</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Crown repair, cap &amp; liner install</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Brick &amp; masonry restoration</li>
                        </ul>
                        <a href="{loc['chimney_link']}" class="stretched-link inline-flex items-center gap-2 text-sm font-semibold text-orange hover:text-orange-dark transition-colors mt-auto">Chimney Services in {loc['name']} <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i></a>
                    </div>
                </div>
                <div class="group relative bg-white rounded-card border border-slate-200 flex flex-col overflow-hidden cursor-pointer transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.22)] hover:border-transparent reveal">
                    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-dark via-orange to-orange-light scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-left rounded-b-card z-10"></div>
                    <img src="../assets/images/tv-mounting-new-jersey.webp" alt="Handyman services in {loc['name']}" class="w-full h-[220px] object-cover object-top shrink-0 transition-transform duration-500 group-hover:scale-105" width="800" height="220" loading="lazy">
                    <div class="p-6 flex flex-col gap-3 flex-1">
                        <div class="flex items-center gap-3">
                            <div class="w-9 h-9 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-screwdriver-wrench text-orange text-[15px]"></i></div>
                            <h2 class="text-[18px] font-bold text-navy-900">{loc['h1_handyman']}</h2>
                        </div>
                        <p class="text-sm text-slate-500 leading-relaxed flex-1">{loc['handyman_desc']}</p>
                        <ul class="flex flex-col gap-1 text-sm text-slate-600">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Drywall repair &amp; painting</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Doors, plumbing &amp; light electrical</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Furniture assembly &amp; TV mounting</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> General repairs — any size job</li>
                        </ul>
                        <a href="{loc['handyman_link']}" class="stretched-link inline-flex items-center gap-2 text-sm font-semibold text-orange hover:text-orange-dark transition-colors mt-auto">Handyman Services in {loc['name']} <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- AREAS -->
    <section class="py-16 bg-white">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Coverage</span>
                <h2 class="section-title">{loc['areas_title']}</h2>
                <p class="section-desc">Licensed &amp; insured technicians dispatched same-day across all areas below.</p>
            </div>
            <div class="flex flex-wrap gap-2.5 justify-center max-w-[900px] mx-auto reveal">
                {areas_html}
            </div>
        </div>
    </section>

    <!-- AREA CARDS GRID -->
    <section class="loc-section" style="position:relative;">
        <div class="loc-bg-pin" style="right:-40px;top:40px;width:320px;height:400px;">
            <svg viewBox="0 0 100 130" fill="#0d1b4b" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;"><path d="M50 0C22.4 0 0 22.4 0 50c0 37.5 50 80 50 80S100 87.5 100 50C100 22.4 77.6 0 50 0z"/><circle cx="50" cy="50" r="19" fill="white" fill-opacity=".6"/></svg>
        </div>
        <div class="loc-bg-pin" style="left:-60px;bottom:80px;width:280px;height:350px;">
            <svg viewBox="0 0 100 130" fill="#0d1b4b" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;"><path d="M50 0C22.4 0 0 22.4 0 50c0 37.5 50 80 50 80S100 87.5 100 50C100 22.4 77.6 0 50 0z"/><circle cx="50" cy="50" r="19" fill="white" fill-opacity=".6"/></svg>
        </div>
        <div class="container" style="position:relative;z-index:1;">
            <div style="text-align:center;margin-bottom:48px;">
                <div style="display:flex;align-items:center;justify-content:center;gap:40px;flex-wrap:wrap;margin-bottom:28px;">
                    <div style="text-align:center;">
                        <span style="display:block;font-size:2.2rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">{loc['card_count']}</span>
                        <span style="color:#64748b;font-size:13px;margin-top:2px;display:block;">Areas Covered</span>
                    </div>
                    <div style="width:1px;height:48px;background:#e2e8f0;"></div>
                    <div style="text-align:center;">
                        <span style="display:block;font-size:2.2rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">2</span>
                        <span style="color:#64748b;font-size:13px;margin-top:2px;display:block;">Services</span>
                    </div>
                    <div style="width:1px;height:48px;background:#e2e8f0;"></div>
                    <div style="text-align:center;">
                        <span style="display:block;font-size:1.4rem;font-weight:800;color:var(--orange);font-family:'Cinzel',serif;">Same-Day</span>
                        <span style="color:#64748b;font-size:13px;margin-top:2px;display:block;">Available</span>
                    </div>
                </div>
                <h2 style="font-size:clamp(22px,3vw,30px);font-weight:800;color:#0d1b4b;margin-bottom:8px;">{loc['card_h2']}</h2>
                <p style="color:#64748b;font-size:15px;">{loc['card_desc']}</p>
            </div>
            <div class="loc-grid">
{cards_html}
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="faq">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Q&amp;A</span>
                <h2 class="section-title">Questions About <span class="text-accent">{loc['name']}</span></h2>
                <p class="section-desc">Common questions from homeowners in {loc['name']} before booking chimney or handyman services.</p>
            </div>
            <div class="faq-accordion">
                {faqs_html}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>Need Chimney or Handyman Services in {loc['name']}?</h2>
                <p>Free estimates · Licensed &amp; insured · Same-day available</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15551234567" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Free Quote</a>
            </div>
        </div>
    </section>

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
                    <li><a href="{loc['chimney_link']}">Chimney &amp; Masonry</a></li>
                    <li><a href="{loc['handyman_link']}">Handyman Services</a></li>
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
    </footer>

    <script type="module" src="../js/service-page.js"></script>
</body>
</html>"""


if __name__ == "__main__":
    for loc in LOCATIONS:
        out_dir = os.path.join(ROOT, loc["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(build_page(loc))
        print(f"  ✓  /{loc['slug']}/index.html")
