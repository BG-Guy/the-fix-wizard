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


# ── Chimney Services ─────────────────────────────────────────────────────────

CHIMNEY_SERVICES = [
    ("fa-broom",           "Chimney Sweeping & Cleaning",      "Annual sweeping removes creosote buildup — the #1 cause of chimney fires. We use rotary brushes and HEPA vacuums from top to bottom, leaving no mess."),
    ("fa-trowel-bricks",   "Tuckpointing & Mortar Repointing", "Crumbling mortar joints let water into the masonry. We grind out deteriorated mortar and pack new mortar to the correct depth to stop water infiltration."),
    ("fa-hat-hard",        "Chimney Crown Repair & Sealing",   "The crown sheds water away from the flue opening. Cracked crowns allow water to enter and accelerate deterioration — we repair or fully replace them."),
    ("fa-circle-dot",      "Chimney Cap Installation",         "A stainless steel cap keeps rain, animals, and debris out while letting exhaust escape. We measure and install the correctly sized cap with stainless screws."),
    ("fa-droplet-slash",   "Chimney Flashing Repair",          "Failed flashing at the roof–chimney junction is the most common source of attic water damage. We install new step and counterflashing and seal correctly."),
    ("fa-fire-flame-curved","Firebox Repair",                  "Cracked or spalled firebrick allows combustion gases to reach framing. We re-mortar loose joints with refractory mortar and replace damaged brick."),
    ("fa-pipe",            "Chimney Liner Installation",        "A properly sized liner is required by code and ensures combustion gases exhaust safely. We install stainless steel liner systems for all fuel types."),
    ("fa-shield-halved",   "Chimney Waterproofing",            "We apply penetrating, vapor-permeable masonry waterproofer to the exterior — blocking water entry while allowing moisture to escape from inside."),
    ("fa-wind",            "Chimney Draft Repair",             "Smoke backing into the room signals a draft problem — blockage, undersized flue, or negative pressure. We diagnose and correct the root cause."),
    ("fa-toggle-on",       "Fireplace Damper Repair",          "A stuck damper wastes energy year-round. We repair throat dampers or install top-mount dampers that seal the flue when not in use."),
    ("fa-layer-group",     "Brick & Mortar Restoration",       "Spalling brick and deteriorated mortar are common in older housing stock. We clean, tuckpoint, and stabilize aging masonry to stop further weathering."),
    ("fa-magnifying-glass","Chimney Inspection",               "A Level 1 inspection covers all accessible interior and exterior surfaces. We check for obstructions, deterioration, and code compliance, and provide a written report."),
]

CHIMNEY_FAQS = [
    ("How often should I have my chimney swept?",
     "Most chimney safety organizations recommend annual sweeping and inspection before each heating season. Homes that burn wood regularly may need sweeping twice a year. Gas appliances still require annual inspection even without heavy creosote buildup."),
    ("How much does chimney repair cost?",
     "Chimney sweeping typically costs $150–$300. Tuckpointing ranges from $500–$3,000 depending on extent. Crown repair runs $200–$800. Liner installation starts at $1,500. We provide free itemized estimates with no obligation."),
    ("What is tuckpointing and do I need it?",
     "Tuckpointing is the process of grinding out deteriorated mortar joints and packing in fresh mortar. If you can see gaps, crumbling, or missing mortar between your chimney bricks, tuckpointing is overdue. Left untreated, water infiltration causes much costlier structural damage."),
    ("Do you service both wood-burning and gas fireplaces?",
     "Yes. We service all chimney and fireplace types — wood-burning fireplaces, gas inserts, oil appliances, and pellet stoves. The specific services differ by fuel type, but we handle all of them."),
    ("What areas do you serve for chimney repair?",
     "We serve all 21 counties in New Jersey and the greater Cleveland, Ohio area including Lakewood, Parma, Strongsville, Westlake, Beachwood, and 15+ more suburbs. Select your location below for area-specific service details."),
]


def chimney_page():
    services_html = ""
    for icon, title, desc in CHIMNEY_SERVICES:
        services_html += f"""
                <div class="group bg-white rounded-card border border-slate-200 p-6 flex flex-col gap-3 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(13,27,75,.14)] hover:border-orange/30 reveal">
                    <div class="w-11 h-11 bg-orange/10 rounded-xl flex items-center justify-center shrink-0">
                        <i class="fas {icon} text-orange text-[18px]"></i>
                    </div>
                    <h3 class="text-[16px] font-bold text-navy-900">{title}</h3>
                    <p class="text-[13px] text-slate-500 leading-relaxed">{desc}</p>
                </div>"""

    faqs_html = ""
    for q, a in CHIMNEY_FAQS:
        faqs_html += f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false">
                        <span>{q}</span>
                        <i class="fas fa-plus"></i>
                    </button>
                    <div class="faq-answer" aria-hidden="true"><p>{a}</p></div>
                </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <meta name="description" content="Expert chimney repair and masonry services — sweeping, tuckpointing, crown repair, liner installation, flashing, and more. Serving New Jersey and Cleveland, Ohio. Licensed & insured. Free estimates.">
    <title>Chimney Repair &amp; Masonry Services | The Fix Wizard</title>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "Chimney Repair and Masonry",
      "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard", "telephone": "(555) 123-4567"}},
      "areaServed": [{{"@type":"State","name":"New Jersey"}},{{"@type":"City","name":"Cleveland","containedInPlace":{{"@type":"State","name":"Ohio"}}}}],
      "description": "Expert chimney repair and masonry services including sweeping, tuckpointing, crown repair, liner installation, and waterproofing."
    }}
    </script>
</head>
<body>

{NAVBAR}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">

                <!-- LEFT -->
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-fire text-orange text-[11px]"></i>
                        <span>Chimney &amp; Masonry Specialists</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(32px,5vw,64px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Expert Chimney Repair<br>
                        <span class="text-orange">&amp; <span class="lightning-word">Masonry Services</span></span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-6 max-w-[560px]">
                        From annual chimney sweeping and tuckpointing to full liner installation and masonry restoration — licensed specialists covering every repair your chimney needs, done right the first time.
                    </p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-broom text-orange text-[12px]"></i> Sweeping &amp; Inspection
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-trowel-bricks text-orange text-[12px]"></i> Tuckpointing
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-pipe text-orange text-[12px]"></i> Liner Install
                        </div>
                    </div>
                    <div class="flex items-center gap-3 mb-12 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="../new-jersey/" class="btn btn-primary btn-lg">
                            <i class="fas fa-map-marker-alt"></i> New Jersey
                        </a>
                        <a href="../cleveland-ohio/" class="btn btn-outline btn-lg">
                            <i class="fas fa-map-marker-alt"></i> Cleveland, Ohio
                        </a>
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

                <!-- RIGHT -->
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[520px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-6">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas fa-fire"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">Chimney Services Near You</div>
                                <p class="text-[13px] text-white/50">Select your location to get started</p>
                            </div>
                        </div>
                        <div class="flex flex-col gap-3">
                            <a href="../new-jersey/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-location-dot"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">New Jersey</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">All 21 counties · Bergen to Cape May</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                            <a href="../cleveland-ohio/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-location-dot"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">Cleveland, Ohio</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">Greater Cleveland · 20 suburbs</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                        </div>
                        <a href="../#contact" class="btn btn-primary btn-full">
                            <i class="fas fa-paper-plane"></i> Request a Free Quote
                        </a>
                        <div class="flex gap-3 pt-1 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-shield-halved text-orange text-[13px]"></i><span>Licensed &amp; Insured</span></div>
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-clock text-orange text-[13px]"></i><span>Same Day Available</span></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
{SPARKLES}
    </section>

    <!-- SERVICES GRID -->
    <section class="py-20" style="background:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">What We Cover</span>
                <h2 class="section-title">Complete Chimney &amp; <span class="text-accent">Masonry Services</span></h2>
                <p class="section-desc">Every chimney repair and masonry service your home needs — performed by licensed, insured technicians with same-day availability.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 max-w-[1060px] mx-auto">
{services_html}
            </div>
        </div>
    </section>

    <!-- LOCATION CTA -->
    <section class="py-16 bg-white">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Our Locations</span>
                <h2 class="section-title">Chimney Services in <span class="text-accent">Your Area</span></h2>
                <p class="section-desc">Choose your location for local pricing, same-day availability, and area-specific service details.</p>
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
    </section>

    <!-- FAQ -->
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

    <!-- CTA -->
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
</body>
</html>"""


# ── Handyman Services ─────────────────────────────────────────────────────────

HANDYMAN_SERVICES = [
    ("fa-fill-drip",           "Drywall Repair &amp; Patching",    "Holes, cracks, water damage, and texture matching handled invisibly — we blend the repair with your existing wall so you'd never know anything happened."),
    ("fa-paint-roller",        "Interior &amp; Exterior Painting",  "Proper prep first: patching, sanding, priming, and taping before a single drop of paint. Low-VOC paints, two full coats, clean results every time."),
    ("fa-door-open",           "Door Repair &amp; Installation",    "Sticking doors, broken hinges, damaged frames, squeaking hardware — we adjust, repair, or replace interior and exterior doors cleanly."),
    ("fa-couch",               "Furniture Assembly",                "IKEA, Wayfair, and Amazon flat-pack assembled correctly — beds, desks, wardrobes, shelving, TV stands, and dining sets of any size."),
    ("fa-tv",                  "TV Mounting &amp; Installation",    "We mount TVs on drywall, concrete, tile, and brick. Studs located, mount leveled, cables routed in-wall when requested."),
    ("fa-bolt",                "Light Electrical Repairs",          "Dead outlets, flickering lights, switches, ceiling fans, and light fixtures replaced safely — all code-compliant work done right."),
    ("fa-faucet",              "Light Plumbing Repairs",            "Dripping faucets, running toilets, slow drains, and under-sink leaks diagnosed and fixed on the same visit."),
    ("fa-shelves",             "Shelf &amp; Storage Installation",  "Floating shelves and wall-mounted storage anchored to studs, genuinely level and rated for the load."),
    ("fa-wind",                "Weatherstripping &amp; Door Seals", "We replace door weatherstripping, bottom seals, and threshold gaskets to stop drafts and reduce heating and cooling costs."),
    ("fa-droplet",             "Caulking &amp; Sealing",            "Failed caulk around tubs, sinks, windows, and exterior trim removed completely and replaced with fresh, cleanly tooled lines."),
    ("fa-border-all",          "Tile Repair &amp; Grout",           "Cracked or loose tiles replaced, deteriorated grout re-done, tub and shower transitions re-caulked for a clean waterproof surface."),
    ("fa-clipboard-list",      "Handyman Home Inspection",          "Room-by-room walkthrough identifying deferred maintenance items — prioritized by urgency with honest cost estimates so you can plan ahead."),
]

HANDYMAN_FAQS = [
    ("What handyman services do you offer?",
     "We handle a wide range of home repairs: drywall patching and texture matching, interior and exterior painting, door repair and installation, furniture assembly, TV mounting, light electrical (outlets, switches, fans, fixtures), light plumbing (faucets, toilets, drains, disposals), weatherstripping, caulking, tile repair, and general home maintenance."),
    ("Can you do multiple jobs in one visit?",
     "Absolutely. Combining multiple tasks in one visit is actually the most efficient way to use our time and yours. Common combinations include drywall patching + paint touch-ups, outlet replacement + fan installation, and furniture assembly + TV mounting — all in a single appointment."),
    ("How much does handyman service cost?",
     "Most handyman jobs run $150–$500 depending on complexity and time. Furniture assembly typically runs $75–$200 per piece. TV mounting is $100–$200. Drywall patch and texture match averages $150–$350. We provide free estimates before any work begins."),
    ("Are your handymen licensed and insured?",
     "Yes. All technicians are background-checked, and The Fix Wizard carries full liability insurance on every job in both New Jersey and Ohio. You're protected on every visit."),
    ("What areas do you serve for handyman services?",
     "We serve all 21 counties in New Jersey and the greater Cleveland, Ohio area — including Lakewood, Parma, Strongsville, Westlake, Beachwood, Shaker Heights, and 14+ more suburbs. Select your location below for area-specific details."),
]


def handyman_page():
    services_html = ""
    for icon, title, desc in HANDYMAN_SERVICES:
        services_html += f"""
                <div class="group bg-white rounded-card border border-slate-200 p-6 flex flex-col gap-3 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(13,27,75,.14)] hover:border-orange/30 reveal">
                    <div class="w-11 h-11 bg-orange/10 rounded-xl flex items-center justify-center shrink-0">
                        <i class="fas {icon} text-orange text-[18px]"></i>
                    </div>
                    <h3 class="text-[16px] font-bold text-navy-900">{title}</h3>
                    <p class="text-[13px] text-slate-500 leading-relaxed">{desc}</p>
                </div>"""

    faqs_html = ""
    for q, a in HANDYMAN_FAQS:
        faqs_html += f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false">
                        <span>{q}</span>
                        <i class="fas fa-plus"></i>
                    </button>
                    <div class="faq-answer" aria-hidden="true"><p>{a}</p></div>
                </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <meta name="description" content="Expert handyman services — drywall repair, painting, plumbing, electrical, door repair, furniture assembly, TV mounting, and more. Serving New Jersey and Cleveland, Ohio. Licensed & insured. Free estimates.">
    <title>Handyman Services | The Fix Wizard</title>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "Handyman Services",
      "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard", "telephone": "(555) 123-4567"}},
      "areaServed": [{{"@type":"State","name":"New Jersey"}},{{"@type":"City","name":"Cleveland","containedInPlace":{{"@type":"State","name":"Ohio"}}}}],
      "description": "Expert handyman services including drywall repair, painting, plumbing, electrical, door repair, furniture assembly, and TV mounting."
    }}
    </script>
</head>
<body>

{NAVBAR}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">

                <!-- LEFT -->
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-screwdriver-wrench text-orange text-[11px]"></i>
                        <span>Licensed Handyman Specialists</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(32px,5vw,64px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Expert Handyman<br>
                        <span class="text-orange">Services <span class="lightning-word">Near You</span></span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-6 max-w-[560px]">
                        From drywall patching and painting to light plumbing, electrical, doors, and furniture assembly — one call covers your entire repair list. Licensed, insured, and same-day available.
                    </p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-fill-drip text-orange text-[12px]"></i> Drywall &amp; Painting
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-faucet text-orange text-[12px]"></i> Plumbing &amp; Electrical
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-couch text-orange text-[12px]"></i> Assembly &amp; Mounting
                        </div>
                    </div>
                    <div class="flex items-center gap-3 mb-12 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="../new-jersey/" class="btn btn-primary btn-lg">
                            <i class="fas fa-map-marker-alt"></i> New Jersey
                        </a>
                        <a href="../cleveland-ohio/" class="btn btn-outline btn-lg">
                            <i class="fas fa-map-marker-alt"></i> Cleveland, Ohio
                        </a>
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

                <!-- RIGHT -->
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[520px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-6">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas fa-screwdriver-wrench"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">Handyman Services Near You</div>
                                <p class="text-[13px] text-white/50">Select your location to get started</p>
                            </div>
                        </div>
                        <div class="flex flex-col gap-3">
                            <a href="../new-jersey/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-location-dot"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">New Jersey</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">All 21 counties · Bergen to Cape May</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                            <a href="../cleveland-ohio/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                                <div class="w-12 h-12 shrink-0 bg-orange rounded-lg flex items-center justify-center text-[22px] text-white transition-transform group-hover:scale-110">
                                    <i class="fas fa-location-dot"></i>
                                </div>
                                <div class="flex-1 text-left">
                                    <div class="text-[15px] font-bold text-white leading-tight">Cleveland, Ohio</div>
                                    <div class="text-[12px] text-white/50 mt-0.5">Greater Cleveland · 20 suburbs</div>
                                </div>
                                <i class="fas fa-arrow-right text-orange text-[13px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-1 group-hover:translate-x-0 transition-transform"></i>
                            </a>
                        </div>
                        <a href="../#contact" class="btn btn-primary btn-full">
                            <i class="fas fa-paper-plane"></i> Request a Free Quote
                        </a>
                        <div class="flex gap-3 pt-1 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-shield-halved text-orange text-[13px]"></i><span>Licensed &amp; Insured</span></div>
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold text-white/55"><i class="fas fa-clock text-orange text-[13px]"></i><span>Same Day Available</span></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
{SPARKLES}
    </section>

    <!-- SERVICES GRID -->
    <section class="py-20" style="background:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">What We Cover</span>
                <h2 class="section-title">Complete <span class="text-accent">Handyman Services</span></h2>
                <p class="section-desc">Every repair and home maintenance task handled by licensed, insured technicians — single visit, transparent pricing, satisfaction guaranteed.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 max-w-[1060px] mx-auto">
{services_html}
            </div>
        </div>
    </section>

    <!-- LOCATION CTA -->
    <section class="py-16 bg-white">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Our Locations</span>
                <h2 class="section-title">Handyman Services in <span class="text-accent">Your Area</span></h2>
                <p class="section-desc">Choose your location for local pricing, same-day availability, and area-specific service details.</p>
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
    </section>

    <!-- FAQ -->
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

    <!-- CTA -->
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
</body>
</html>"""


if __name__ == "__main__":
    for slug, html_fn in [("chimney-services", chimney_page), ("handyman-services", handyman_page)]:
        out_dir = os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(html_fn())
        print(f"  ✓  /{slug}/index.html")
