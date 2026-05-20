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

# All blog-page styles defined here — no Tailwind scanning needed
BLOG_STYLES = """
/* ── Layout ── */
.blog-page-wrap{background:#fff;padding:60px 0 80px}
.blog-layout{display:flex;flex-direction:column;gap:48px;max-width:1100px;margin:0 auto;padding:0 24px}
@media(min-width:1024px){.blog-layout{flex-direction:row;gap:64px;align-items:flex-start}}

/* ── Article column ── */
.blog-article{flex:1;min-width:0}

/* ── Sticky sidebar ── */
.blog-sidebar{width:100%;flex-shrink:0}
@media(min-width:1024px){.blog-sidebar{width:300px;position:sticky;top:calc(var(--nav-h,96px) + 24px)}}

/* ── Hero meta bar ── */
.hero-meta-bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:24px}
.hero-meta-sep{color:rgba(255,255,255,.2);font-size:14px;line-height:1}
.hero-meta-chip{display:flex;align-items:center;gap:6px;font-size:13px;color:rgba(255,255,255,.5)}
.hero-meta-chip i{font-size:11px;color:#FF6B35}
.tag-pill{display:inline-flex;align-items:center;gap:6px;background:rgba(255,107,53,.12);color:#FF6B35;padding:5px 12px;border-radius:99px;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.07em}

/* ── Blog typography ── */
.blog-lead{font-size:18px;color:#3a4560;line-height:1.85;font-weight:500;margin-bottom:20px}
.blog-body-p{font-size:16px;color:#5a6478;line-height:1.9;margin-bottom:20px}

/* ── Section heading ── */
.blog-section-title{font-size:20px;font-weight:800;color:#091236;padding-left:14px;border-left:3px solid #FF6B35;line-height:1.3;margin:0 0 20px 0;display:block}

/* ── Blog section wrapper ── */
.blog-section{margin-bottom:44px}

/* ── Consequences box (subtle urgency) ── */
.consequences-box{background:#f7f8fc;border-left:3px solid #1e3480;border-radius:0 12px 12px 0;padding:20px 24px}
.consequences-box .blog-body-p{color:#3a4560}

/* ── Warning callout ── */
.warning-callout{background:#fffbeb;border-left:3px solid #d97706;border-radius:0 14px 14px 0;padding:20px 24px}
.warning-callout__title{font-size:16px;font-weight:700;color:#92400e;margin:0 0 12px;display:flex;align-items:center;gap:9px}
.warning-callout__title i{font-size:14px;color:#d97706}

/* ── Blog list ── */
.blog-list{list-style:none;padding:0;margin:10px 0 0;display:flex;flex-direction:column;gap:8px}
.blog-list li{display:flex;align-items:flex-start;gap:10px;font-size:15px;color:#3a4560;line-height:1.6}
.blog-list li::before{content:'';width:7px;height:7px;border-radius:50%;background:#FF6B35;flex-shrink:0;margin-top:7px}

/* ── Custom CTA box ── */
.custom-cta-box{background:#f1f5f9;border-radius:16px;padding:32px;text-align:center;margin-top:8px}
.custom-cta-box__headline{font-size:17px;font-weight:700;color:#091236;margin:0 0 20px}



/* ── Related services ── */
.related-section{padding-top:32px;border-top:1px solid #f0f2f7;margin-top:8px}
.related-grid{display:grid;grid-template-columns:1fr;gap:12px}
@media(min-width:600px){.related-grid{grid-template-columns:1fr 1fr}}
.related-card{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #e4e9f2;border-radius:16px;padding:16px;text-decoration:none;transition:all .2s ease}
.related-card:hover{border-color:#FF6B35;box-shadow:0 4px 20px rgba(13,27,75,.1);transform:translateY(-1px)}
.related-icon{flex-shrink:0;width:40px;height:40px;border-radius:10px;background:rgba(255,107,53,.07);display:flex;align-items:center;justify-content:center;transition:background .2s}
.related-card:hover .related-icon{background:rgba(255,107,53,.14)}
.related-icon i{color:#FF6B35;font-size:14px}
.related-body{flex:1;min-width:0}
.related-name{font-size:14px;font-weight:600;color:#091236;transition:color .2s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.related-card:hover .related-name{color:#FF6B35}
.related-loc{font-size:12px;color:#94a3b8;margin-top:2px}
.related-arrow{color:#d1d8e8;font-size:11px;flex-shrink:0;transition:all .2s}
.related-card:hover .related-arrow{color:#FF6B35;transform:translateX(2px)}

/* ── Sidebar: booking card ── */
.sb-book{background:#091236;border-radius:18px;padding:24px;margin-bottom:16px;color:#fff}
.sb-book-label{font-size:11px;font-weight:700;color:rgba(255,255,255,.32);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px}
.sb-book-title{font-size:17px;font-weight:700;color:#fff;margin-bottom:4px;line-height:1.3}
.sb-book-sub{font-size:13px;color:rgba(255,255,255,.45);margin-bottom:20px;line-height:1.55}
.sb-book-btns{display:flex;flex-direction:column;gap:10px}
.sb-book-footer{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)}
.sb-book-badge{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(255,255,255,.38)}
.sb-book-badge i{color:#FF6B35;font-size:11px}

/* ── Sidebar: includes card ── */
.sb-card{background:#fff;border:1px solid #e4e9f2;border-radius:18px;padding:24px;margin-bottom:16px;display:block;transition:border-color .2s}
.sb-card:hover{border-color:#FF6B35}
.sb-card-header{display:flex;align-items:center;gap:10px;margin-bottom:18px}
.sb-card-icon{width:32px;height:32px;border-radius:8px;background:rgba(255,107,53,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.sb-card-icon i{color:#FF6B35;font-size:13px}
.sb-card-title{font-size:15px;font-weight:700;color:#091236}

/* ── Includes checklist ── */
.includes-check{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid #f1f5f9;font-size:14px;color:#3a4560}
.includes-check:last-child{border-bottom:none}
.includes-check i{color:#FF6B35;font-size:11px;margin-top:3px;flex-shrink:0}

/* ── Sidebar: nav link cards ── */
.sb-nav-link{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #e4e9f2;border-radius:16px;padding:16px;margin-bottom:12px;text-decoration:none;transition:border-color .2s}
.sb-nav-link:hover{border-color:#FF6B35}
.sb-nav-icon{width:36px;height:36px;border-radius:10px;background:rgba(255,107,53,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.sb-nav-icon.grey{background:#f1f4f9}
.sb-nav-icon i{color:#FF6B35;font-size:13px}
.sb-nav-body{flex:1;min-width:0}
.sb-nav-title{font-size:13px;font-weight:600;color:#091236;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sb-nav-sub{font-size:12px;color:#94a3b8;margin-top:2px}
"""


def _first_sentence(text):
    idx = text.find('. ')
    return text[:idx + 1] if idx != -1 else text


def blog_sections_html(slug, name, loc_name, includes):
    c = SERVICE_CONTENT.get(slug)
    if not c:
        return ""

    if c.get("custom_html"):
        return c["custom_html"]

    includes_li = "\n".join(f'<li>{item}</li>' for item in includes)
    warning_text = _first_sentence(c["consequences"])

    return f"""
        <div class="blog-section">
            <p class="blog-lead">{c["why_need"]}</p>
        </div>

        <div class="blog-section">
            <span class="blog-section-title">What Our {name} Service Includes</span>
            <ul class="blog-list" style="margin-top:14px">
                {includes_li}
            </ul>
        </div>

        <div class="blog-section">
            <div class="warning-callout">
                <h3 class="warning-callout__title"><i class="fas fa-clock-rotate-left"></i> The Cost of Delay</h3>
                <p class="blog-body-p" style="margin:0">{warning_text} Contacting an expert early allows for targeted solutions before the damage becomes significantly more expensive to address.</p>
            </div>
        </div>

        <div class="blog-section">
            <span class="blog-section-title">What a Professional {name} Delivers</span>
            <p class="blog-body-p" style="margin-top:14px">{c["benefits"]}</p>
            <p class="blog-body-p">{c["longevity"]}</p>
        </div>

        <div class="blog-section">
            <span class="blog-section-title" style="border-left-color:#1e3480">What Happens When {name} Goes Unaddressed</span>
            <div class="consequences-box" style="margin-top:14px">
                <p class="blog-body-p" style="margin:0">{c["consequences"]}</p>
            </div>
        </div>

        <div class="blog-section">
            <span class="blog-section-title">Why Choose Professional Care?</span>
            <ul class="blog-list" style="margin-top:14px">
                <li><strong>The Details Matter:</strong> Our specialists arrive fully equipped to deliver precise, lasting results tailored exactly to your home's needs — no guesswork, no shortcuts.</li>
                <li><strong>We Stand Behind Our Work:</strong> Every job comes with our commitment to quality so you can rest easy knowing your home is properly protected.</li>
                <li><strong>Licensed &amp; Insured:</strong> Full liability coverage on every visit, protecting you and your property throughout the entire process.</li>
            </ul>
        </div>

        <div class="custom-cta-box">
            <p class="custom-cta-box__headline">Ready to protect your home before the next season?</p>
            <a href="../#contact" class="btn btn-primary btn-lg"><i class="fas fa-paper-plane"></i> Get a Free Estimate</a>
        </div>
"""


def page_html(svc, loc, svc_type, all_svcs_in_cat, cat_name):
    icon, name, slug, short_desc, includes = svc
    loc_name   = loc["name"]
    loc_slug   = loc["slug"]
    loc_url    = loc["url"]
    loc_area   = loc["area"]
    hub_url    = "../chimney/" if svc_type == "chimney" else "../handyman/"
    hub_label  = f"Chimney Services in {loc_name}" if svc_type == "chimney" else f"Handyman Services in {loc_name}"
    clean_name = name.replace("&amp;", "&").replace("&", "and")

    includes_html = "\n".join(
        f'<div class="includes-check"><i class="fas fa-check"></i><span>{item}</span></div>'
        for item in includes
    )

    related = [s for s in all_svcs_in_cat if s[2] != slug][:4]
    related_html = "\n".join(
        f'<a href="../{s[2]}/" class="related-card">'
        f'<div class="related-icon"><i class="fas {s[0]}"></i></div>'
        f'<div class="related-body"><div class="related-name">{s[1]}</div>'
        f'<div class="related-loc">{loc_name}</div></div>'
        f'<i class="fas fa-arrow-right related-arrow"></i></a>'
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
    <style>
:root{{--nav-h:150px}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}}
body.no-scroll{{overflow:hidden}}
a{{text-decoration:none;color:inherit}}
.reveal{{opacity:0;transform:translateY(28px)}}
.sp-hero,.hero{{background-color:#091236;color:#fff}}
.mobile-menu{{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}}
.mobile-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}}
.faq-answer{{max-height:0;overflow:hidden}}
#navbar{{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}}
@media(max-width:768px){{:root{{--nav-h:96px}}}}
{BLOG_STYLES}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="{GFONTS}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{GFONTS}"></noscript>
    <link rel="preload" href="{FA}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{FA}"></noscript>
    <link rel="preload" href="../../css/tw.css" as="style">
    <link rel="stylesheet" href="../../css/tw.css">
    <link rel="preload" href="../../css/custom.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="../../css/custom.css"></noscript>
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
            <a href="../../" class="logo"><img src="../../assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img" width="199" height="110"></a>
            <ul class="nav-links">
                <li><a href="../../" class="nav-link">Home</a></li>
                <li><a href="../../#services" class="nav-link">Services</a></li>
                <li><a href="../../#why-us" class="nav-link">About</a></li>
                <li><a href="../../#contact" class="nav-link">Contact</a></li>
                <li class="nav-dropdown">
                    <a href="../../locations/" class="nav-link" style="display:flex;align-items:center;gap:6px">Locations <i class="fas fa-chevron-down" style="font-size:10px;opacity:.5;margin-top:1px"></i></a>
                    <div class="nav-dropdown-menu">
                        <a href="../../new-jersey/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> New Jersey</a>
                        <a href="../../cleveland-ohio/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                        <div class="nav-dropdown-divider"></div>
                        <a href="../../locations/" class="nav-dropdown-item" style="color:rgba(255,255,255,.45)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
                    </div>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="tel:+15551234567" class="nav-phone"><i class="fas fa-phone"></i><span>(555) 123-4567</span></a>
                <a href="../../#contact" class="btn btn-primary nav-cta">Free Quote
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
            <li><a href="../../" class="mobile-link">Home</a></li>
            <li><a href="../../#services" class="mobile-link">Services</a></li>
            <li><a href="../../#why-us" class="mobile-link">About</a></li>
            <li><a href="../../#contact" class="mobile-link">Contact</a></li>
            <li>
                <span class="mobile-loc-label">Locations</span>
                <a href="../../new-jersey/"     class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> New Jersey</a>
                <a href="../../cleveland-ohio/" class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                <a href="../../locations/"      class="mobile-link mobile-loc-sub" style="color:rgba(255,255,255,.4)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
            </li>
        </ul>
        <a href="tel:+15551234567" class="mobile-phone"><i class="fas fa-phone"></i>(555) 123-4567</a>
        <a href="../../#contact" class="btn btn-primary mobile-cta mobile-link">Get Free Quote</a>
    </div>
    <div class="mobile-overlay" id="mobileOverlay"></div>

    <!-- ===== ARTICLE HERO ===== -->
    <section class="sp-hero" style="padding-bottom:0;border-radius:0">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="../../">Home</a><i class="fas fa-chevron-right"></i>
                <a href="{hub_url}">{hub_label}</a><i class="fas fa-chevron-right"></i>
                <span>{clean_name}</span>
            </nav>
            <div style="max-width:780px;padding:36px 0 52px">
                <div class="hero-meta-bar">
                    <span class="tag-pill"><i class="fas {icon}"></i> {cat_name}</span>
                    <span class="hero-meta-sep">·</span>
                    <span class="hero-meta-chip"><i class="fas fa-location-dot"></i>{loc_name}</span>
                    <span class="hero-meta-sep">·</span>
                    <span class="hero-meta-chip"><i class="fas fa-clock"></i> 5 min read</span>
                </div>
                <h1 class="sp-title" style="margin-bottom:14px">{name} <span class="text-accent">in {loc_name}</span></h1>
                <p class="sp-subtitle" style="margin-bottom:28px">{short_desc} Serving {loc_area}. Licensed &amp; insured. Same-day available.</p>
                <div class="sp-actions">
                    <a href="tel:+15551234567" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                    <a href="../../#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Estimate</a>
                </div>
            </div>
        </div>
    </section>

    <!-- ===== ARTICLE BODY ===== -->
    <div class="blog-page-wrap">
        <div class="blog-layout">

            <!-- MAIN ARTICLE -->
            <article class="blog-article">
                {blog_sections_html(slug, clean_name, loc_name, includes)}

                <div class="related-section">
                    <span class="blog-section-title" style="margin-bottom:20px">More {cat_name} Services in {loc_name}</span>
                    <div class="related-grid">
                        {related_html}
                    </div>
                </div>
            </article>

            <!-- SIDEBAR -->
            <aside class="blog-sidebar">

                <!-- Book -->
                <div class="sb-book">
                    <p class="sb-book-label">Free Estimate</p>
                    <p class="sb-book-title">Book {name}</p>
                    <p class="sb-book-sub">No obligation · Response within 2 hours</p>
                    <div class="sb-book-btns">
                        <a href="tel:+15551234567" class="btn btn-primary btn-full"><i class="fas fa-phone"></i> (555) 123-4567</a>
                        <a href="../../#contact" class="btn btn-outline-white btn-full"><i class="fas fa-paper-plane"></i> Send a Message</a>
                    </div>
                    <div class="sb-book-footer">
                        <span class="sb-book-badge"><i class="fas fa-shield-halved"></i> Licensed &amp; Insured</span>
                        <span class="sb-book-badge"><i class="fas fa-clock"></i> Same Day</span>
                    </div>
                </div>

                <!-- Includes -->
                <div class="sb-card">
                    <div class="sb-card-header">
                        <div class="sb-card-icon"><i class="fas fa-list-check"></i></div>
                        <span class="sb-card-title">What's Included</span>
                    </div>
                    {includes_html}
                    <a href="../../#contact" class="btn btn-primary btn-full" style="margin-top:16px"><i class="fas fa-calendar-alt"></i> Book This Service</a>
                </div>

                <!-- Nav links -->
                <a href="{hub_url}" class="sb-nav-link">
                    <div class="sb-nav-icon"><i class="fas {icon}"></i></div>
                    <div class="sb-nav-body">
                        <div class="sb-nav-title">{hub_label}</div>
                        <div class="sb-nav-sub">See all services →</div>
                    </div>
                </a>
                <a href="../" class="sb-nav-link">
                    <div class="sb-nav-icon grey"><i class="fas fa-location-dot"></i></div>
                    <div class="sb-nav-body">
                        <div class="sb-nav-title">{loc_name} Services</div>
                        <div class="sb-nav-sub">All services in your area →</div>
                    </div>
                </a>

            </aside>

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
                <a href="../../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Free Quote</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="../../" class="logo"><img src="../../assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="logo-img footer-logo-img" width="199" height="110"></a>
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
                    <li><a href="../../chimney-services/">Chimney &amp; Masonry</a></li>
                    <li><a href="../../handyman-services/">Handyman Services</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Service Areas</h4>
                <ul>
                    <li><a href="../../new-jersey/">New Jersey</a></li>
                    <li><a href="../../cleveland-ohio/">Cleveland, Ohio</a></li>
                    <li><a href="../../locations/">All Locations</a></li>
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

    <script type="module" src="../../js/service-page.js"></script>
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
                out_dir = os.path.join(ROOT, loc['url'], slug)
                os.makedirs(out_dir, exist_ok=True)
                html = page_html(svc, loc, svc_type, cat_svcs, cat_name)
                with open(os.path.join(out_dir, "index.html"), "w") as f:
                    f.write(html)
                count += 1
    print(f"  ✓  {count} service detail pages generated")
