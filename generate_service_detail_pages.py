#!/usr/bin/env python3
"""
Generates individual service detail pages.
URL pattern: /{service-slug}-in-{location-slug}/index.html
e.g. /chimney-tuckpointing-in-new-jersey/index.html
     /tub-caulking-in-cleveland/index.html
"""

import os, base64
from services_data import (
    CHIMNEY_SERVICES_FULL, HANDYMAN_SERVICES_FULL,
    LOCATIONS, CHIMNEY_CATS, HANDYMAN_CATS,
    build_service_lookup
)

ROOT = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(ROOT, "favicon-32.png"), "rb") as f:
        FAVICON_B64 = base64.b64encode(f.read()).decode()
    FAVICON_TAG = f'<link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{FAVICON_B64}">'
except:
    FAVICON_TAG = '<link rel="icon" href="/favicon.ico" type="image/x-icon">'

GFONTS = "https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"
FA     = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"


def page_html(svc, loc, svc_type, all_svcs_in_cat, cat_name):
    icon, name, slug, short_desc, includes = svc
    loc_name   = loc["name"]
    loc_slug   = loc["slug"]   # "new-jersey" or "cleveland"
    loc_url    = loc["url"]    # "new-jersey" or "cleveland-ohio" (matches directory)
    loc_area   = loc["area"]
    page_slug  = f"{slug}-in-{loc_slug}"
    svc_hub    = "chimney-masonry" if svc_type == "chimney" else "handyman-services"
    hub_url    = f"../chimney-masonry-{loc_url}/" if svc_type == "chimney" else f"../handyman-services-{loc_url}/"
    hub_label  = f"Chimney Services in {loc_name}" if svc_type == "chimney" else f"Handyman Services in {loc_name}"
    clean_name = name.replace("&amp;", "&").replace("&", "and")

    includes_html = "\n".join(
        f'                            <li class="flex items-center gap-2.5"><i class="fas fa-check text-orange text-[11px]"></i>{item}</li>'
        for item in includes
    )

    # Related services in same category (excluding self)
    related = [s for s in all_svcs_in_cat if s[2] != slug][:4]
    related_html = "\n".join(
        f'                    <a href="../{s[2]}-in-{loc_slug}/" class="flex items-center gap-3 bg-white border border-slate-200 rounded-xl p-4 hover:border-orange hover:shadow-md transition-all group">'
        f'<i class="fas {s[0]} text-orange text-[14px] w-5 shrink-0"></i>'
        f'<span class="text-[14px] font-medium text-navy-900 group-hover:text-orange transition-colors">{s[1]}</span>'
        f'</a>'
        for s in related
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {FAVICON_TAG}
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <meta name="description" content="{clean_name} in {loc_name}. {short_desc.replace('&amp;','and')} Licensed &amp; insured. Same-day available. Free estimates.">
    <title>{clean_name} in {loc_name} | The Fix Wizard</title>
    <style>:root{{--nav-h:150px}}*,*::before,*::after{{box-sizing:border-box}}body{{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}}body.no-scroll{{overflow:hidden}}a{{text-decoration:none;color:inherit}}.reveal{{opacity:0;transform:translateY(28px)}}.sp-hero,.hero{{background-color:#091236;color:#fff}}.mobile-menu{{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}}.mobile-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}}.faq-answer{{max-height:0;overflow:hidden}}#navbar{{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}}@media(max-width:768px){{:root{{--nav-h:96px}}}}</style>
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
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "{clean_name}",
      "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard", "telephone": "(555) 123-4567"}},
      "areaServed": {{"@type": "{"State" if loc_slug == "new-jersey" else "City"}", "name": "{"New Jersey" if loc_slug == "new-jersey" else "Cleveland"}"}},
      "description": "{short_desc.replace(chr(34), chr(39))}"
    }}
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
    <div class="mobile-overlay" id="mobileOverlay"></div>

    <section class="sp-hero">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="../">Home</a><i class="fas fa-chevron-right"></i>
                <a href="{hub_url}">{hub_label}</a><i class="fas fa-chevron-right"></i>
                <span>{clean_name}</span>
            </nav>
            <div class="sp-hero-inner">
                <div class="sp-hero-left">
                    <div class="sp-icon-wrap"><i class="fas {icon}"></i></div>
                    <h1 class="sp-title">{name} <span class="text-accent">in {loc_name}</span></h1>
                    <p class="sp-subtitle">{short_desc} Serving {loc_area}. Licensed &amp; insured. Same-day available.</p>
                    <div class="sp-actions">
                        <a href="tel:+15551234567" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                        <a href="../#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Estimate</a>
                    </div>
                    <div class="sp-badges">
                        <span><i class="fas fa-shield-halved"></i> Licensed &amp; Insured</span>
                        <span><i class="fas fa-clock"></i> Same Day Available</span>
                        <span><i class="fas fa-tag"></i> Free Estimates</span>
                    </div>
                </div>
                <div class="sp-hero-right">
                    <div class="sp-includes-card">
                        <h3>What's Included</h3>
                        <ul class="sp-includes-list">
{includes_html}
                        </ul>
                        <a href="../#contact" class="btn btn-primary btn-full"><i class="fas fa-calendar-alt"></i> Book This Service</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="py-16 bg-white">
        <div class="container">
            <div class="grid grid-cols-1 md:grid-cols-[1fr_340px] gap-12 max-w-[960px] mx-auto">
                <div>
                    <h2 class="text-[24px] font-bold text-navy-900 mb-4">{name} in {loc_name}</h2>
                    <p class="text-[16px] text-slate-600 leading-relaxed mb-6">{short_desc} We serve {loc_area} with licensed technicians, transparent pricing, and same-day availability.</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
                        <div class="flex items-start gap-3 p-4 bg-slate-50 rounded-xl border border-slate-100">
                            <i class="fas fa-shield-halved text-orange text-[18px] mt-0.5 shrink-0"></i>
                            <div><div class="font-semibold text-navy-900 text-[14px]">Licensed &amp; Insured</div><div class="text-[13px] text-slate-500 mt-0.5">Full liability coverage on every job</div></div>
                        </div>
                        <div class="flex items-start gap-3 p-4 bg-slate-50 rounded-xl border border-slate-100">
                            <i class="fas fa-clock text-orange text-[18px] mt-0.5 shrink-0"></i>
                            <div><div class="font-semibold text-navy-900 text-[14px]">Same-Day Available</div><div class="text-[13px] text-slate-500 mt-0.5">Call for urgent appointment</div></div>
                        </div>
                        <div class="flex items-start gap-3 p-4 bg-slate-50 rounded-xl border border-slate-100">
                            <i class="fas fa-tag text-orange text-[18px] mt-0.5 shrink-0"></i>
                            <div><div class="font-semibold text-navy-900 text-[14px]">Free Estimates</div><div class="text-[13px] text-slate-500 mt-0.5">No cost, no obligation quote</div></div>
                        </div>
                        <div class="flex items-start gap-3 p-4 bg-slate-50 rounded-xl border border-slate-100">
                            <i class="fas fa-star text-orange text-[18px] mt-0.5 shrink-0"></i>
                            <div><div class="font-semibold text-navy-900 text-[14px]">500+ Jobs Done</div><div class="text-[13px] text-slate-500 mt-0.5">Experienced in every property type</div></div>
                        </div>
                    </div>
                    <h3 class="text-[18px] font-bold text-navy-900 mb-3">More {cat_name} Services in {loc_name}</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
{related_html}
                    </div>
                </div>
                <div class="flex flex-col gap-5">
                    <div class="bg-navy-900 rounded-2xl p-6 text-white flex flex-col gap-4">
                        <div class="text-[16px] font-bold">Book {name}</div>
                        <p class="text-[13px] text-white/60">Free estimate · No obligation · Response within 2 hours</p>
                        <a href="tel:+15551234567" class="btn btn-primary btn-full"><i class="fas fa-phone"></i> (555) 123-4567</a>
                        <a href="../#contact" class="btn btn-outline-white btn-full"><i class="fas fa-paper-plane"></i> Send a Message</a>
                        <div class="flex items-center gap-2 text-[12px] text-white/40"><i class="fas fa-map-marker-alt text-orange"></i> Serving {loc_name}</div>
                    </div>
                    <a href="{hub_url}" class="flex items-center gap-3 bg-orange/[.08] border border-orange/20 rounded-xl p-4 hover:bg-orange/[.14] transition-colors">
                        <i class="fas {icon} text-orange text-[18px] shrink-0"></i>
                        <div>
                            <div class="font-semibold text-navy-900 text-[14px]">{hub_label}</div>
                            <div class="text-[12px] text-slate-500 mt-0.5">See all services →</div>
                        </div>
                    </a>
                    <a href="../{loc_url}/" class="flex items-center gap-3 bg-slate-50 border border-slate-200 rounded-xl p-4 hover:border-orange hover:bg-orange/[.05] transition-colors">
                        <i class="fas fa-location-dot text-orange text-[18px] shrink-0"></i>
                        <div>
                            <div class="font-semibold text-navy-900 text-[14px]">{loc_name} Services</div>
                            <div class="text-[12px] text-slate-500 mt-0.5">All services in your area →</div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>{name} in {loc_name}? We've Got You.</h2>
                <p>Free estimate · Licensed &amp; insured · Same-day available</p>
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
    </footer>

    <script type="module" src="../js/service-page.js"></script>
</body>
</html>"""


def get_cat_services(slug, svc_type):
    """Return all services in the same category as this slug."""
    cats = CHIMNEY_CATS if svc_type == "chimney" else HANDYMAN_CATS
    lookup = build_service_lookup(CHIMNEY_SERVICES_FULL if svc_type == "chimney" else HANDYMAN_SERVICES_FULL)
    all_svcs = CHIMNEY_SERVICES_FULL if svc_type == "chimney" else HANDYMAN_SERVICES_FULL
    for cat_name, _, slugs in cats:
        if slug in slugs:
            return cat_name, [lookup[s] for s in slugs if s in lookup]
    return "Services", all_svcs


if __name__ == "__main__":
    count = 0
    for svc_list, svc_type in [(CHIMNEY_SERVICES_FULL, "chimney"), (HANDYMAN_SERVICES_FULL, "handyman")]:
        for svc in svc_list:
            slug = svc[2]
            cat_name, cat_svcs = get_cat_services(slug, svc_type)
            for loc in LOCATIONS:
                page_slug = f"{slug}-in-{loc['slug']}"
                out_dir = os.path.join(ROOT, page_slug)
                os.makedirs(out_dir, exist_ok=True)
                html = page_html(svc, loc, svc_type, cat_svcs, cat_name)
                with open(os.path.join(out_dir, "index.html"), "w") as f:
                    f.write(html)
                count += 1
    print(f"  ✓  {count} service detail pages generated")
