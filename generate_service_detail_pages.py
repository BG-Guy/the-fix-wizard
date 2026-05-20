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
    build_service_lookup, SERVICE_CONTENT
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

BLOG_STYLES = """
.blog-section-title{font-size:20px;font-weight:800;color:#091236;padding-left:14px;border-left:3px solid var(--orange,#e85c1e);line-height:1.3;margin:0}
.blog-lead{font-size:18px;color:#3a4560;line-height:1.85;font-weight:450}
.blog-p{font-size:16px;color:#566070;line-height:1.9}
.step-line{position:absolute;left:15px;top:32px;bottom:0;width:2px;background:linear-gradient(to bottom,#e2e8f0,transparent)}
.tag-pill{display:inline-flex;align-items:center;gap:6px;background:rgba(232,92,30,.1);color:var(--orange,#e85c1e);padding:4px 12px;border-radius:99px;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.meta-sep{color:#cbd5e1;margin:0 4px}
.includes-check{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid #f1f5f9;font-size:14px;color:#3a4560}
.includes-check:last-child{border-bottom:none}
.sidebar-card{background:#fff;border:1px solid #e8ecf3;border-radius:18px;padding:24px;margin-bottom:16px}
.sidebar-book{background:#091236;border-radius:18px;padding:24px;margin-bottom:16px;color:#fff}
@media(min-width:1024px){.article-sidebar{position:sticky;top:calc(var(--nav-h,96px) + 24px)}}
"""


def blog_sections_html(slug, name, loc_name):
    c = SERVICE_CONTENT.get(slug)
    if not c:
        return ""

    paras = [p.strip() for p in c["intro"].split("\n\n") if p.strip()]
    intro_html = ""
    for i, p in enumerate(paras):
        cls = "blog-lead mb-5" if i == 0 else "blog-p mb-5"
        intro_html += f'<p class="{cls}">{p}</p>'

    signs_li = "".join(
        f'<li class="flex items-start gap-3 text-[15px] text-slate-700 leading-snug py-2">'
        f'<i class="fas fa-chevron-right text-orange text-[11px] mt-[5px] shrink-0"></i>'
        f'<span>{s}</span></li>'
        for s in c["signs"]
    )

    total = len(c["steps"])
    steps_html = ""
    for i, (title, desc) in enumerate(c["steps"]):
        line = '<div class="step-line"></div>' if i < total - 1 else ""
        steps_html += (
            f'<div class="relative flex gap-5 pb-8 last:pb-0">'
            f'{line}'
            f'<div class="shrink-0 w-[30px] h-[30px] rounded-full bg-navy-900 text-white text-[12px] font-bold flex items-center justify-center z-10 mt-0.5">{i+1}</div>'
            f'<div><p class="font-bold text-navy-900 text-[15px] mb-1 mt-0.5">{title}</p>'
            f'<p class="blog-p text-[14px] leading-relaxed">{desc}</p></div></div>'
        )

    benefits_html = "".join(
        f'<div class="flex items-start gap-4 py-5 border-b border-slate-100 last:border-0">'
        f'<div class="shrink-0 w-9 h-9 rounded-xl bg-orange/[.1] flex items-center justify-center">'
        f'<i class="fas fa-check text-orange text-[13px]"></i></div>'
        f'<div><p class="font-bold text-navy-900 text-[15px] mb-1">{title}</p>'
        f'<p class="blog-p text-[14px]">{desc}</p></div></div>'
        for title, desc in c["benefits"]
    )

    return f"""
            <!-- INTRO -->
            <div class="mb-10">
                {intro_html}
            </div>

            <!-- SIGNS -->
            <div class="mb-10">
                <h2 class="blog-section-title">Signs You Need {name}</h2>
                <div class="mt-4 bg-amber-50 border-l-[3px] border-orange rounded-r-2xl px-6 py-4">
                    <ul class="list-none p-0 m-0 divide-y divide-amber-100">
                        {signs_li}
                    </ul>
                </div>
            </div>

            <!-- PROCESS -->
            <div class="mb-10">
                <h2 class="blog-section-title">How It Works</h2>
                <div class="mt-6 pl-1">
                    {steps_html}
                </div>
            </div>

            <!-- BENEFITS -->
            <div class="mb-10">
                <h2 class="blog-section-title">Benefits of Professional {name} in {loc_name}</h2>
                <div class="mt-4 border border-slate-200 rounded-2xl px-6">
                    {benefits_html}
                </div>
            </div>

            <!-- PRICING -->
            <div class="mb-10 relative overflow-hidden rounded-2xl bg-navy-900 p-7 text-white">
                <div class="relative z-10">
                    <div class="tag-pill mb-3" style="background:rgba(232,92,30,.2);color:#f97e4a">
                        <i class="fas fa-tag"></i> Pricing &amp; Estimates
                    </div>
                    <p class="text-[15px] text-white/70 leading-relaxed">{c["price"]}</p>
                    <a href="../#contact" class="inline-flex items-center gap-2 mt-5 btn btn-primary">
                        <i class="fas fa-paper-plane"></i> Get a Free Estimate
                    </a>
                </div>
                <div class="absolute right-5 bottom-2 text-white/[.04] text-[110px] font-black leading-none select-none pointer-events-none">$</div>
            </div>"""


def page_html(svc, loc, svc_type, all_svcs_in_cat, cat_name):
    icon, name, slug, short_desc, includes = svc
    loc_name   = loc["name"]
    loc_slug   = loc["slug"]
    loc_url    = loc["url"]
    loc_area   = loc["area"]
    hub_url    = f"../chimney-masonry-{loc_url}/" if svc_type == "chimney" else f"../handyman-services-{loc_url}/"
    hub_label  = f"Chimney Services in {loc_name}" if svc_type == "chimney" else f"Handyman Services in {loc_name}"
    clean_name = name.replace("&amp;", "&").replace("&", "and")

    includes_html = "\n".join(
        f'<div class="includes-check"><i class="fas fa-check text-orange text-[11px] mt-[3px] shrink-0"></i><span>{item}</span></div>'
        for item in includes
    )

    related = [s for s in all_svcs_in_cat if s[2] != slug][:4]
    related_html = "\n".join(
        f'<a href="../{s[2]}-in-{loc_slug}/" class="flex items-center gap-3 bg-white border border-slate-200 rounded-2xl p-4 hover:border-orange hover:shadow-md transition-all group">'
        f'<div class="w-10 h-10 rounded-xl bg-orange/[.08] flex items-center justify-center shrink-0 group-hover:bg-orange/[.15] transition-colors">'
        f'<i class="fas {s[0]} text-orange text-[14px]"></i></div>'
        f'<div class="flex-1 min-w-0"><div class="text-[14px] font-semibold text-navy-900 group-hover:text-orange transition-colors truncate">{s[1]}</div>'
        f'<div class="text-[12px] text-slate-400 mt-0.5">{loc_name}</div></div>'
        f'<i class="fas fa-arrow-right text-slate-300 text-[11px] group-hover:text-orange group-hover:translate-x-0.5 transition-all"></i>'
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
    <style>:root{{--nav-h:150px}}*,*::before,*::after{{box-sizing:border-box}}body{{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}}body.no-scroll{{overflow:hidden}}a{{text-decoration:none;color:inherit}}.reveal{{opacity:0;transform:translateY(28px)}}.sp-hero,.hero{{background-color:#091236;color:#fff}}.mobile-menu{{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}}.mobile-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}}.faq-answer{{max-height:0;overflow:hidden}}#navbar{{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}}@media(max-width:768px){{:root{{--nav-h:96px}}}}{BLOG_STYLES}</style>
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

    <!-- ===== ARTICLE HERO ===== -->
    <section class="sp-hero" style="padding-bottom:0">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="../">Home</a><i class="fas fa-chevron-right"></i>
                <a href="{hub_url}">{hub_label}</a><i class="fas fa-chevron-right"></i>
                <span>{clean_name}</span>
            </nav>
            <div class="max-w-[780px] py-10 md:py-14">
                <div class="flex items-center gap-3 mb-5 flex-wrap">
                    <span class="tag-pill"><i class="fas {icon}"></i> {cat_name}</span>
                    <span class="meta-sep">·</span>
                    <span class="flex items-center gap-1.5 text-[13px] text-white/50"><i class="fas fa-location-dot text-orange text-[11px]"></i>{loc_name}</span>
                    <span class="meta-sep">·</span>
                    <span class="flex items-center gap-1.5 text-[13px] text-white/50"><i class="fas fa-clock text-[11px]"></i> 5 min read</span>
                </div>
                <h1 class="sp-title" style="margin-bottom:16px">{name} <span class="text-accent">in {loc_name}</span></h1>
                <p class="sp-subtitle" style="margin-bottom:28px">{short_desc} Serving {loc_area}. Licensed &amp; insured. Same-day available.</p>
                <div class="flex items-center gap-3 flex-wrap">
                    <a href="tel:+15551234567" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                    <a href="../#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Estimate</a>
                </div>
            </div>
        </div>
    </section>

    <!-- ===== BLOG ARTICLE BODY ===== -->
    <div class="bg-white py-14">
        <div class="container">
            <div class="max-w-[1100px] mx-auto flex flex-col lg:flex-row gap-12 items-start">

                <!-- ARTICLE CONTENT -->
                <article class="flex-1 min-w-0">
                    {blog_sections_html(slug, clean_name, loc_name)}

                    <!-- RELATED SERVICES -->
                    <div class="mt-4 pt-8 border-t border-slate-100">
                        <h2 class="blog-section-title mb-5">More {cat_name} Services in {loc_name}</h2>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            {related_html}
                        </div>
                    </div>
                </article>

                <!-- STICKY SIDEBAR -->
                <aside class="article-sidebar w-full lg:w-[300px] shrink-0">

                    <!-- BOOK NOW CARD -->
                    <div class="sidebar-book">
                        <div class="text-[11px] font-bold text-white/40 uppercase tracking-widest mb-3">Free Estimate</div>
                        <div class="text-[18px] font-bold text-white mb-1">Book {name}</div>
                        <p class="text-[13px] text-white/50 mb-5">No obligation · Response within 2 hours</p>
                        <a href="tel:+15551234567" class="btn btn-primary btn-full mb-3"><i class="fas fa-phone"></i> (555) 123-4567</a>
                        <a href="../#contact" class="btn btn-outline-white btn-full"><i class="fas fa-paper-plane"></i> Send a Message</a>
                        <div class="flex items-center gap-4 mt-5 pt-4 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] text-white/40"><i class="fas fa-shield-halved text-orange text-[11px]"></i> Licensed &amp; Insured</div>
                            <div class="flex items-center gap-1.5 text-[12px] text-white/40"><i class="fas fa-clock text-orange text-[11px]"></i> Same Day</div>
                        </div>
                    </div>

                    <!-- WHAT'S INCLUDED CARD -->
                    <div class="sidebar-card">
                        <div class="flex items-center gap-2.5 mb-4">
                            <div class="w-8 h-8 rounded-lg bg-orange/[.1] flex items-center justify-center shrink-0">
                                <i class="fas fa-list-check text-orange text-[13px]"></i>
                            </div>
                            <div class="text-[15px] font-bold text-navy-900">What's Included</div>
                        </div>
                        {includes_html}
                        <a href="../#contact" class="btn btn-primary btn-full mt-4"><i class="fas fa-calendar-alt"></i> Book This Service</a>
                    </div>

                    <!-- NAV LINKS -->
                    <a href="{hub_url}" class="sidebar-card flex items-center gap-3 hover:border-orange transition-colors" style="margin-bottom:12px">
                        <div class="w-9 h-9 rounded-xl bg-orange/[.1] flex items-center justify-center shrink-0">
                            <i class="fas {icon} text-orange text-[13px]"></i>
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="font-semibold text-navy-900 text-[13px] truncate">{hub_label}</div>
                            <div class="text-[12px] text-slate-400 mt-0.5">See all services →</div>
                        </div>
                    </a>
                    <a href="../{loc_url}/" class="sidebar-card flex items-center gap-3 hover:border-orange transition-colors">
                        <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center shrink-0">
                            <i class="fas fa-location-dot text-orange text-[13px]"></i>
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="font-semibold text-navy-900 text-[13px] truncate">{loc_name} Services</div>
                            <div class="text-[12px] text-slate-400 mt-0.5">All services in your area →</div>
                        </div>
                    </a>

                </aside>

            </div>
        </div>
    </div>

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
