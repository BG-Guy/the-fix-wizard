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
                <li><a href="../locations/" class="nav-link active">Locations</a></li>
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
            <li><a href="../locations/" class="mobile-link">Locations</a></li>
        </ul>
        <a href="tel:+15551234567" class="mobile-phone"><i class="fas fa-phone"></i>(555) 123-4567</a>
        <a href="../#contact" class="btn btn-primary mobile-cta mobile-link">Get Free Quote</a>
    </div>
    <div class="mobile-overlay" id="mobileOverlay"></div>

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-[80vh] pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_400px] gap-12 items-center py-16 md:py-12">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <nav class="flex items-center gap-2 text-white/40 text-[13px] mb-6 flex-wrap justify-center tab:justify-start">
                        <a href="../" class="hover:text-orange transition-colors">Home</a>
                        <i class="fas fa-chevron-right text-[10px]"></i>
                        <span class="text-white/70">{loc['name']}</span>
                    </nav>
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-6 tracking-wide">
                        <i class="fas fa-location-dot text-orange text-[11px]"></i>
                        <span>{loc['badge']}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(28px,4.5vw,56px)] font-black leading-[1.1] tracking-tight text-white mb-5">
                        {loc['hero_title']}
                    </h1>
                    <p class="text-[17px] text-white/65 leading-[1.75] mb-8 max-w-[540px]">
                        {loc['hero_sub']}
                    </p>
                    <div class="flex items-center gap-3 mb-10 flex-wrap justify-center tab:justify-start">
                        <a href="tel:+15551234567" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                        <a href="../#contact" class="btn btn-outline btn-lg"><i class="fas fa-calendar-alt"></i> Free Estimate</a>
                    </div>
                    <div class="flex items-center gap-6 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 text-[13px] font-semibold text-white/60"><i class="fas fa-shield-halved text-orange"></i> Licensed &amp; Insured</div>
                        <div class="flex items-center gap-2 text-[13px] font-semibold text-white/60"><i class="fas fa-calendar-check text-orange"></i> Same-Day Available</div>
                        <div class="flex items-center gap-2 text-[13px] font-semibold text-white/60"><i class="fas fa-tag text-orange"></i> Free Estimates</div>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[400px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-7 flex flex-col gap-5">
                        <div class="text-center">
                            <div class="text-[14px] font-semibold text-white/50 mb-1">Our 2 Specialties in {loc['name']}</div>
                        </div>
                        <a href="{loc['chimney_link']}" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[20px] text-white transition-transform group-hover:scale-110"><i class="fas fa-fire"></i></div>
                            <div class="flex-1 text-left">
                                <div class="text-[14px] font-bold text-white">Chimney &amp; Masonry</div>
                                <div class="text-[11px] text-white/50 mt-0.5">Sweeping · Tuckpointing · Crown · Liner</div>
                            </div>
                            <i class="fas fa-arrow-right text-orange text-[12px] opacity-0 group-hover:opacity-100 transition-opacity"></i>
                        </a>
                        <a href="{loc['handyman_link']}" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[20px] text-white transition-transform group-hover:scale-110"><i class="fas fa-screwdriver-wrench"></i></div>
                            <div class="flex-1 text-left">
                                <div class="text-[14px] font-bold text-white">Handyman Services</div>
                                <div class="text-[11px] text-white/50 mt-0.5">Drywall · Painting · Plumbing · Electrical</div>
                            </div>
                            <i class="fas fa-arrow-right text-orange text-[12px] opacity-0 group-hover:opacity-100 transition-opacity"></i>
                        </a>
                        <a href="../#contact" class="btn btn-primary btn-full"><i class="fas fa-paper-plane"></i> Request a Free Quote</a>
                        <p class="text-[11px] text-white/35 text-center">Response within 2 hours · No obligation</p>
                    </div>
                </div>
            </div>
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
