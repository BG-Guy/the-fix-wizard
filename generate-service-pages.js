'use strict';
const fs   = require('fs');
const path = require('path');
const ROOT = __dirname;
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, 'services-data.json'), 'utf8'));

const LOCATIONS = [
  { city:'Cherry Hill',    state:'NJ', stateFull:'New Jersey',    county:'Camden County',      slug:'cherry-hill',     nearby:'Haddonfield · Voorhees · Merchantville · Pennsauken' },
  { city:'Philadelphia',   state:'PA', stateFull:'Pennsylvania',  county:'Philadelphia County', slug:'philadelphia',    nearby:'Fishtown · South Philly · Manayunk · Northeast Philadelphia' },
  { city:'Moorestown',     state:'NJ', stateFull:'New Jersey',    county:'Burlington County',  slug:'moorestown',      nearby:'Evesham · Medford · Mount Holly · Marlton' },
  { city:'Princeton',      state:'NJ', stateFull:'New Jersey',    county:'Mercer County',      slug:'princeton',       nearby:'Lawrenceville · Hamilton · Pennington · West Windsor' },
  { city:'West Chester',   state:'PA', stateFull:'Pennsylvania',  county:'Chester County',     slug:'west-chester',    nearby:'Exton · Malvern · Phoenixville · Downingtown' },
  { city:'Wilmington',     state:'DE', stateFull:'Delaware',      county:'New Castle County',  slug:'wilmington',      nearby:'Newark · Bear · Hockessin · Pike Creek' },
  { city:'Haddonfield',    state:'NJ', stateFull:'New Jersey',    county:'Camden County',      slug:'haddonfield',     nearby:'Cherry Hill · Collingswood · Westmont · Lawnside' },
  { city:'Mount Laurel',   state:'NJ', stateFull:'New Jersey',    county:'Burlington County',  slug:'mount-laurel',    nearby:'Moorestown · Marlton · Evesham · Maple Shade' },
  { city:'Marlton',        state:'NJ', stateFull:'New Jersey',    county:'Burlington County',  slug:'marlton',         nearby:'Voorhees · Cherry Hill · Mount Laurel · Medford' },
  { city:'Voorhees',       state:'NJ', stateFull:'New Jersey',    county:'Camden County',      slug:'voorhees',        nearby:'Cherry Hill · Marlton · Gibbsboro · Lawnside' },
  { city:'Trenton',        state:'NJ', stateFull:'New Jersey',    county:'Mercer County',      slug:'trenton',         nearby:'Hamilton · Lawrence · Ewing · Bordentown' },
  { city:'Wayne',          state:'PA', stateFull:'Pennsylvania',  county:'Delaware County',    slug:'wayne',           nearby:'Radnor · Bryn Mawr · Villanova · Paoli' },
  { city:'King of Prussia',state:'PA', stateFull:'Pennsylvania',  county:'Montgomery County',  slug:'king-of-prussia', nearby:'Upper Merion · Norristown · Collegeville · Phoenixville' },
  { city:'Atlantic City',  state:'NJ', stateFull:'New Jersey',    county:'Atlantic County',    slug:'atlantic-city',   nearby:'Galloway · Egg Harbor · Absecon · Brigantine' },
];

// ── Shared HTML ───────────────────────────────────────────────────────────────

const FAVICON = `<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">`;

const HEAD_STYLES = `<style>:root{--nav-h:150px}*,*::before,*::after{box-sizing:border-box}body{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}body.no-scroll{overflow:hidden}a{text-decoration:none;color:inherit}.reveal{opacity:0;transform:translateY(28px)}.hero{background-color:#091236;color:#fff}.mobile-menu{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}.mobile-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}.faq-answer{max-height:0;overflow:hidden}#navbar{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}@media(max-width:768px){:root{--nav-h:96px}}</style>`;

const FONTS = `<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"></noscript>
    <link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"></noscript>
    <link rel="stylesheet" href="/css/tw.css">
    <link rel="stylesheet" href="/css/custom.css">`;

function navbar(loc, serviceParam = '') {
  const contactHref = serviceParam ? `/?service=${serviceParam}#contact` : '/#contact';
  return `    <nav id="navbar" class="navbar fixed top-0 left-0 right-0 z-[100]">
        <div class="max-w-site mx-auto px-6 flex items-center h-full gap-8 nav-container">
            <a href="/" class="flex items-center shrink-0 logo">
                <img src="/assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="h-auto max-h-[58px] md:max-h-[110px] w-auto object-contain rounded-lg logo-img" width="199" height="110">
            </a>
            <ul class="hidden md:flex items-center gap-0.5 mx-auto nav-links">
                <li><a href="/" class="nav-link text-white/80 hover:text-white text-[15px] font-medium px-3.5 py-2 rounded-lg transition-colors">Home</a></li>
                <li><a href="/#services" class="nav-link text-white/80 hover:text-white text-[15px] font-medium px-3.5 py-2 rounded-lg transition-colors">Services</a></li>
                <li><a href="/#why-us" class="nav-link text-white/80 hover:text-white text-[15px] font-medium px-3.5 py-2 rounded-lg transition-colors">About</a></li>
                <li><a href="${contactHref}" class="nav-link text-white/80 hover:text-white text-[15px] font-medium px-3.5 py-2 rounded-lg transition-colors">Contact</a></li>
                <li class="nav-dropdown">
                    <a href="/locations/" class="nav-link text-white/80 hover:text-white text-[15px] font-medium px-3.5 py-2 rounded-lg transition-colors flex items-center gap-1.5">Locations <i class="fas fa-chevron-down text-[10px] opacity-50 mt-px"></i></a>
                    <div class="nav-dropdown-menu">
                        <a href="/cherry-hill-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Cherry Hill</a>
                        <a href="/haddonfield-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Haddonfield</a>
                        <a href="/voorhees-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Voorhees</a>
                        <a href="/marlton-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Marlton</a>
                        <a href="/moorestown-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Moorestown</a>
                        <a href="/mount-laurel-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Mount Laurel</a>
                        <a href="/philadelphia-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Philadelphia</a>
                        <a href="/west-chester-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> West Chester</a>
                        <a href="/wilmington-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Wilmington</a>
                        <div class="nav-dropdown-divider"></div>
                        <a href="/locations/" class="nav-dropdown-item" style="color:rgba(255,255,255,.45)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
                    </div>
                </li>
            </ul>
            <div class="hidden md:flex items-center gap-4 shrink-0 nav-actions">
                <a href="tel:+15513504951" class="flex items-center gap-2 text-white/75 text-sm font-medium hover:text-orange transition-colors">
                    <i class="fas fa-phone text-orange"></i><span>(551) 350-4951</span>
                </a>
                <a href="${contactHref}" class="btn btn-primary nav-cta relative overflow-hidden">Free Quote</a>
            </div>
            <button class="hamburger md:hidden flex flex-col gap-[5px] cursor-pointer bg-transparent border-none p-2 order-first" id="hamburger" aria-label="Toggle menu">
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
            </button>
        </div>
    </nav>
    <div class="mobile-menu fixed top-0 z-[101] w-[min(320px,88vw)] h-screen bg-navy-900 pt-[76px] px-7 pb-9 flex flex-col gap-1.5 overflow-y-auto" id="mobileMenu">
        <button class="absolute top-[18px] right-[18px] bg-white/10 border-none text-white w-[38px] h-[38px] rounded-full flex items-center justify-center cursor-pointer text-[15px] transition-all hover:bg-orange mobile-menu-close" id="mobileClose" aria-label="Close menu"><i class="fas fa-times"></i></button>
        <ul class="flex flex-col gap-0.5 mb-5 mobile-nav-links">
            <li><a href="/" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Home</a></li>
            <li><a href="/#services" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Services</a></li>
            <li><a href="/${loc.slug}-repair/" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Locations</a></li>
            <li><a href="${contactHref}" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Contact</a></li>
        </ul>
        <a href="tel:+15513504951" class="mobile-phone flex items-center gap-2.5 text-white/65 text-sm mb-3.5 px-3.5"><i class="fas fa-phone text-orange"></i>(551) 350-4951</a>
        <a href="${contactHref}" class="btn btn-primary mobile-cta mobile-link mt-1.5">Get Free Quote</a>
    </div>
    <div class="mobile-overlay fixed inset-0 bg-black/50 z-[100] opacity-0 invisible transition-all backdrop-blur-sm" id="mobileOverlay"></div>`;
}

function footer() {
  return `    <footer class="pt-20 pb-0" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 pb-[60px]">
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-[2fr_1fr_1fr_1fr] gap-12">
                <div class="md:col-span-3 lg:col-span-1">
                    <a href="/" class="inline-block mb-[18px]"><img src="/assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="h-[64px] w-auto object-contain rounded-lg" width="199" height="64" loading="lazy"></a>
                    <p class="text-[15px] leading-[1.7] mb-[22px]" style="color:rgba(255,255,255,.55)">The Fix Wizard handles the repairs most people dread. Quality work, honest pricing, and results that last.</p>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Services</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li><a href="/services/chimney/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Chimney &amp; Masonry</a></li>
                        <li><a href="/services/handyman/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Handyman Services</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Service Areas</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li><a href="/cherry-hill-repair/"  class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Cherry Hill, NJ</a></li>
                        <li><a href="/haddonfield-repair/"  class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Haddonfield, NJ</a></li>
                        <li><a href="/moorestown-repair/"   class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Moorestown, NJ</a></li>
                        <li><a href="/mount-laurel-repair/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Mount Laurel, NJ</a></li>
                        <li><a href="/philadelphia-repair/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Philadelphia, PA</a></li>
                        <li><a href="/west-chester-repair/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">West Chester, PA</a></li>
                        <li><a href="/wilmington-repair/"   class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.5)">Wilmington, DE</a></li>
                        <li><a href="/locations/" class="text-[14px] transition-all hover:text-orange" style="color:rgba(255,255,255,.35)">All Locations &rarr;</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Contact</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li class="flex items-center gap-2.5 text-[14px]" style="color:rgba(255,255,255,.5)"><i class="fas fa-phone text-orange w-4 shrink-0"></i><a href="tel:+15513504951" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.5)">(551) 350-4951</a></li>
                        <li class="flex items-center gap-2.5 text-[14px]" style="color:rgba(255,255,255,.5)"><i class="fas fa-envelope text-orange w-4 shrink-0"></i><a href="mailto:office@thefixwizard.com" style="color:rgba(255,255,255,.5)">office@thefixwizard.com</a></li>
                        <li class="flex items-center gap-2.5 text-[14px]" style="color:rgba(255,255,255,.5)"><i class="fas fa-clock text-orange w-4 shrink-0"></i><span>Mon–Sat: 7am – 7pm</span></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="py-[22px] border-t border-transparent" style="background:linear-gradient(#091236,#091236) padding-box,linear-gradient(90deg,transparent,rgba(255,107,53,.35),transparent) border-box">
            <div class="max-w-site mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-2 flex-wrap">
                <p class="text-[13px]" style="color:rgba(255,255,255,.35)">&copy; <span id="year"></span> The Fix Wizard. All rights reserved.</p>
                <p class="text-[13px]" style="color:rgba(255,255,255,.35)">Made with <i class="fas fa-heart text-orange"></i> for homeowners everywhere</p>
            </div>
        </div>
    </footer>`;
}

function schema(loc, type, pageSlug, desc) {
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'HomeAndConstructionBusiness',
    name: 'The Fix Wizard',
    description: desc,
    url: `https://thefixwizard.com/${pageSlug}/`,
    telephone: '(551) 350-4951',
    email: 'office@thefixwizard.com',
    logo: 'https://thefixwizard.com/assets/images/the-fix-wizard-logo.webp',
    priceRange: '$$',
    areaServed: { '@type': 'City', name: `${loc.city}, ${loc.state}` },
    openingHoursSpecification: {
      '@type': 'OpeningHoursSpecification',
      dayOfWeek: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
      opens: '07:00', closes: '19:00',
    },
  });
}

// ── Hub page ──────────────────────────────────────────────────────────────────
// URL: /handyman-services-near-[city]/ or /chimney-services-near-[city]/

function hubPage(loc, type) {
  const services  = DATA[type];
  const cats      = DATA[`${type}_cats`];
  const svcMap    = {};
  services.forEach(s => { svcMap[s.slug] = s; });

  const hubSlug     = `${type}-services-near-${loc.slug}`;
  const cityState   = `${loc.city}, ${loc.state}`;
  const typeLabel   = type === 'chimney' ? 'Chimney & Masonry' : 'Handyman';
  const typeIcon    = type === 'chimney' ? 'fa-fire' : 'fa-screwdriver-wrench';
  const svcParam    = type === 'chimney' ? 'Chimney+%26+Masonry' : 'Handyman+Services';
  const otherType   = type === 'chimney' ? 'handyman' : 'chimney';
  const otherLabel  = type === 'chimney' ? 'Handyman Services' : 'Chimney & Masonry';
  const otherIcon   = type === 'chimney' ? 'fa-screwdriver-wrench' : 'fa-fire';
  const otherSlug   = `${otherType}-services-near-${loc.slug}`;

  const title    = `${typeLabel} Services Near ${loc.city}, ${loc.state} | The Fix Wizard`;
  const metaDesc = `Licensed ${typeLabel.toLowerCase()} services near ${cityState} — ${services.length} services available. Same-day scheduling, free estimates. The Fix Wizard — ${loc.county}'s trusted home repair team.`;

  // Pill browser sections
  const pillsHtml = cats.map(cat => {
    const catSvcs = cat.slugs.map(s => svcMap[s]).filter(Boolean);
    if (!catSvcs.length) return '';
    const pills = catSvcs.map(s => {
      const searchName = s.name.toLowerCase();
      const searchDesc = s.desc.toLowerCase().slice(0, 80);
      return `<a href="/${s.slug}-near-${loc.slug}/" class="svc-pill inline-flex items-center gap-2 px-4 py-2 rounded-full border border-slate-200 bg-white text-[13px] font-semibold text-slate-600 hover:border-orange hover:text-orange hover:bg-orange/5 transition-all" data-name="${searchName}" data-desc="${searchDesc}">
                <i class="fas ${s.icon} text-orange text-[11px]"></i>${s.name}
            </a>`;
    }).join('\n            ');
    return `
        <div class="pill-cat mb-10">
            <div class="flex items-center gap-3 mb-5">
                <div class="w-8 h-8 bg-orange/10 rounded-lg flex items-center justify-center shrink-0">
                    <i class="fas ${cat.icon} text-orange text-[13px]"></i>
                </div>
                <span class="text-[11px] font-bold text-slate-400 tracking-[0.15em] uppercase">${cat.name}</span>
            </div>
            <div class="flex flex-wrap gap-2.5">
            ${pills}
            </div>
        </div>`;
  }).join('');

  // Card grid
  const cardsHtml = services.map(s => {
    const searchName = s.name.toLowerCase();
    const searchDesc = s.desc.toLowerCase().slice(0, 100);
    return `<a href="/${s.slug}-near-${loc.slug}/" class="svc-card group bg-white rounded-card p-7 border border-slate-100 hover:border-orange/20 hover:-translate-y-1 hover:shadow-card-xl transition-all duration-300 flex flex-col gap-4" data-name="${searchName}" data-desc="${searchDesc}">
                <div class="w-12 h-12 bg-orange/10 rounded-xl flex items-center justify-center shrink-0 group-hover:bg-orange/20 transition-colors">
                    <i class="fas ${s.icon} text-orange text-lg"></i>
                </div>
                <div class="flex-1">
                    <h3 class="text-[17px] font-bold text-navy-900 mb-1.5 leading-snug group-hover:text-orange transition-colors">${s.name}</h3>
                    <p class="text-[14px] text-slate-500 leading-relaxed">${s.desc}</p>
                </div>
                <span class="inline-flex items-center gap-1.5 text-[13px] font-semibold text-orange group-hover:gap-2.5 transition-all">
                    Learn More <i class="fas fa-arrow-right text-[10px] group-hover:translate-x-1 transition-transform"></i>
                </span>
            </a>`;
  }).join('\n            ');

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${FAVICON}
    <meta name="description" content="${metaDesc}">
    <link rel="canonical" href="https://thefixwizard.com/${hubSlug}/">
    <title>${title}</title>
    <script type="application/ld+json">${schema(loc, type, hubSlug, metaDesc)}<\/script>
    ${HEAD_STYLES}
    ${FONTS}
    <style>
        .svc-pill.hidden,.svc-card.hidden,.pill-cat.hidden{display:none}
        #search-wrap{position:sticky;top:var(--nav-h);z-index:50;background:#fff;border-bottom:1px solid #e2e8f0;box-shadow:0 1px 8px rgba(13,27,75,.06)}
    </style>
</head>
<body>

${navbar(loc, svcParam)}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden pt-[var(--nav-h)] pb-16 rounded-b-[48px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_380px] gap-12 items-center pt-10">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <nav class="flex items-center gap-2 text-[13px] mb-6 flex-wrap" style="color:rgba(255,255,255,.45)">
                        <a href="/" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.45)">Home</a>
                        <i class="fas fa-chevron-right text-[9px]"></i>
                        <a href="/${loc.slug}-repair/" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.45)">${loc.city}</a>
                        <i class="fas fa-chevron-right text-[9px]"></i>
                        <span style="color:rgba(255,255,255,.75)">${typeLabel}</span>
                    </nav>
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-6 tracking-wide">
                        <i class="fas ${typeIcon} text-orange text-[11px]"></i>
                        <span>${services.length} Services Available Near ${loc.city}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(26px,4vw,52px)] font-black leading-[1.1] tracking-tight text-white mb-5">
                        ${typeLabel} Services<br>
                        <span class="text-orange">Near ${loc.city}, ${loc.state}</span>
                    </h1>
                    <p class="text-[17px] leading-[1.75] mb-8 max-w-[540px]" style="color:rgba(255,255,255,.65)">Licensed, insured, and same-day available in ${loc.county}. Browse all ${services.length} services below — click any service to see details and pricing.</p>
                    <div class="flex items-center gap-3 flex-wrap justify-center tab:justify-start">
                        <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                        <a href="/?service=${svcParam}#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote</a>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[360px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-7 flex flex-col gap-4">
                        <div class="text-[14px] font-semibold text-white mb-1">Quick Links</div>
                        <a href="/${loc.slug}-repair/" class="group flex items-center gap-3 bg-white/[.07] border border-white/[.1] rounded-xl p-3.5 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-9 h-9 bg-orange/20 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-home text-orange text-[13px]"></i></div>
                            <div class="flex-1"><div class="text-[13px] font-bold text-white">All Services in ${loc.city}</div><div class="text-[11px]" style="color:rgba(255,255,255,.45)">Hub page — chimney + handyman</div></div>
                            <i class="fas fa-arrow-right text-orange/60 text-[11px] group-hover:translate-x-1 transition-transform"></i>
                        </a>
                        <a href="/${otherSlug}/" class="group flex items-center gap-3 bg-white/[.07] border border-white/[.1] rounded-xl p-3.5 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-9 h-9 bg-orange/20 rounded-lg flex items-center justify-center shrink-0"><i class="fas ${otherIcon} text-orange text-[13px]"></i></div>
                            <div class="flex-1"><div class="text-[13px] font-bold text-white">${otherLabel}</div><div class="text-[11px]" style="color:rgba(255,255,255,.45)">Near ${loc.city}</div></div>
                            <i class="fas fa-arrow-right text-orange/60 text-[11px] group-hover:translate-x-1 transition-transform"></i>
                        </a>
                        <div class="flex gap-3 pt-1 border-t border-white/[.08]">
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold" style="color:rgba(255,255,255,.55)"><i class="fas fa-shield-halved text-orange text-[12px]"></i>Licensed &amp; Insured</div>
                            <div class="flex items-center gap-1.5 text-[12px] font-semibold" style="color:rgba(255,255,255,.55)"><i class="fas fa-clock text-orange text-[12px]"></i>Same-Day</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- STICKY SEARCH -->
    <div id="search-wrap" class="py-5">
        <div class="max-w-site mx-auto px-6">
            <div class="relative max-w-[560px] mx-auto">
                <i class="fas fa-search absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-[14px] pointer-events-none"></i>
                <input id="svc-search" type="search" autocomplete="off" placeholder="Search ${services.length} services — e.g. drywall, faucet, ceiling fan…"
                    class="w-full pl-10 pr-10 py-3.5 rounded-full border border-slate-200 bg-slate-50 text-slate-700 text-[14px] focus:outline-none focus:ring-2 focus:ring-orange/30 focus:border-orange/50 focus:bg-white transition-all">
                <button id="svc-clear" class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 hidden" aria-label="Clear search">
                    <i class="fas fa-times text-[13px]"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- PILL BROWSER -->
    <section class="py-14 bg-white">
        <div class="max-w-site mx-auto px-6">
            <div class="mb-10 reveal">
                <span class="section-tag">Browse by Category</span>
                <h2 class="text-[26px] font-bold text-navy-900 mt-2">All ${typeLabel} Services Near ${loc.city}</h2>
            </div>
            <div id="pill-browser">
            ${pillsHtml}
            </div>
            <div id="no-pill-results" class="hidden text-center py-14">
                <i class="fas fa-search text-5xl text-slate-200 block mb-4"></i>
                <p class="text-slate-400 text-[16px]">No services match — try a different keyword.</p>
            </div>
        </div>
    </section>

    <!-- CARD GRID -->
    <section class="py-20" style="background-color:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="max-w-site mx-auto px-6">
            <div class="section-header reveal">
                <span class="section-tag">${typeLabel} Near ${loc.city}</span>
                <h2 class="section-title">Every Service <span class="text-orange">at a Glance</span></h2>
                <p class="section-desc">Click any service card to see full details, what's included, and what to expect from our ${loc.city} team.</p>
            </div>
            <div id="cards-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${cardsHtml}
            </div>
            <div id="no-card-results" class="hidden text-center py-14">
                <i class="fas fa-screwdriver-wrench text-5xl text-slate-200 block mb-4"></i>
                <p class="text-slate-400 text-[16px]">No services match your search.</p>
            </div>
        </div>
    </section>

    <!-- TRUST STRIP -->
    <section class="py-16 bg-white border-t border-slate-100">
        <div class="max-w-site mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="flex flex-col items-center text-center p-7 rounded-card border border-slate-100 hover:border-orange/20 transition-colors reveal">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-4"><i class="fas fa-shield-halved text-orange text-2xl"></i></div>
                    <h3 class="text-[17px] font-bold text-navy-900 mb-2">Licensed &amp; Insured</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">Fully licensed in ${loc.stateFull}. Every technician is background-checked and insured.</p>
                </div>
                <div class="flex flex-col items-center text-center p-7 rounded-card border border-slate-100 hover:border-orange/20 transition-colors reveal">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-4"><i class="fas fa-clock text-orange text-2xl"></i></div>
                    <h3 class="text-[17px] font-bold text-navy-900 mb-2">Same-Day Available</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">Need it today? Call us. We offer same-day slots in ${loc.county} Mon–Sat, 7am–7pm.</p>
                </div>
                <div class="flex flex-col items-center text-center p-7 rounded-card border border-slate-100 hover:border-orange/20 transition-colors reveal">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-4"><i class="fas fa-file-invoice-dollar text-orange text-2xl"></i></div>
                    <h3 class="text-[17px] font-bold text-navy-900 mb-2">Free Estimates</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">Every job in ${loc.city} starts with a free estimate — no surprises, no obligation.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 text-center">
            <h2 class="font-cinzel text-[clamp(24px,3.5vw,40px)] font-black text-white mb-4">Ready to Book in ${loc.city}?</h2>
            <p class="text-[17px] mb-10 max-w-[500px] mx-auto" style="color:rgba(255,255,255,.6)">Call now or request a free estimate. We also serve ${loc.nearby}.</p>
            <div class="flex items-center justify-center gap-4 flex-wrap">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="/?service=${svcParam}#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote Online</a>
            </div>
        </div>
    </section>

${footer()}

    <script type="module" src="/js/service-page.js"><\/script>
    <script>
        (function(){
            const inp   = document.getElementById('svc-search');
            const clrBtn= document.getElementById('svc-clear');
            const pills = Array.from(document.querySelectorAll('.svc-pill'));
            const cards = Array.from(document.querySelectorAll('.svc-card'));
            const cats  = Array.from(document.querySelectorAll('.pill-cat'));
            const noP   = document.getElementById('no-pill-results');
            const noC   = document.getElementById('no-card-results');

            function filter(raw){
                const q = raw.toLowerCase().trim();
                clrBtn.classList.toggle('hidden', !q);
                let anyP=0, anyC=0;
                pills.forEach(p => {
                    const m = !q || p.dataset.name.includes(q) || p.dataset.desc.includes(q);
                    p.classList.toggle('hidden', !m);
                    if(m) anyP++;
                });
                cats.forEach(c => {
                    const vis = c.querySelectorAll('.svc-pill:not(.hidden)').length>0;
                    c.classList.toggle('hidden', !vis);
                });
                cards.forEach(c => {
                    const m = !q || c.dataset.name.includes(q) || c.dataset.desc.includes(q);
                    c.classList.toggle('hidden', !m);
                    if(m) anyC++;
                });
                noP.classList.toggle('hidden', anyP>0||!q);
                noC.classList.toggle('hidden', anyC>0||!q);
            }

            inp.addEventListener('input', e => filter(e.target.value));
            clrBtn.addEventListener('click', () => { inp.value=''; filter(''); inp.focus(); });
            document.getElementById('year').textContent = new Date().getFullYear();
        })();
    <\/script>
</body>
</html>`;
}

// ── Service detail page ───────────────────────────────────────────────────────
// URL: /[service-slug]-near-[city]/

function detailPage(loc, svc, type) {
  const content    = DATA.content[svc.slug] || null;
  const hubSlug    = `${type}-services-near-${loc.slug}`;
  const detailSlug = `${svc.slug}-near-${loc.slug}`;
  const cityState  = `${loc.city}, ${loc.state}`;
  const typeLabel  = type === 'chimney' ? 'Chimney & Masonry' : 'Handyman Services';
  const typeIcon   = type === 'chimney' ? 'fa-fire' : 'fa-screwdriver-wrench';
  const svcParam   = type === 'chimney' ? 'Chimney+%26+Masonry' : 'Handyman+Services';

  const title    = `${svc.name} Near ${loc.city}, ${loc.state} | The Fix Wizard`;
  const metaDesc = content.meta_desc
    ? content.meta_desc.replace('{city}', loc.city).replace('{state}', loc.state).replace('{cityState}', cityState)
    : `Professional ${svc.name.toLowerCase()} near ${cityState}. ${svc.desc.slice(0, 100)} Licensed & insured. Free estimates. Same-day available.`;

  const includesList = svc.includes.map(item =>
    `<li class="flex items-start gap-3 py-2.5 border-b border-white/[.08] last:border-0">
                            <i class="fas fa-check-circle text-orange shrink-0 mt-0.5 text-[14px]"></i>
                            <span class="text-[13px] font-medium" style="color:rgba(255,255,255,.78)">${item}</span>
                        </li>`
  ).join('\n                            ');

  const sidebarIncludes = svc.includes.map(item =>
    `<li class="flex items-start gap-2.5 py-2 border-b border-slate-100 last:border-0">
                        <i class="fas fa-check text-orange shrink-0 mt-1 text-[11px]"></i>
                        <span class="text-[13px] text-slate-600">${item}</span>
                    </li>`
  ).join('\n                        ');

  const r = s => s ? s.replace(/\{cityState\}/g, cityState).replace(/\{city\}/g, loc.city).replace(/\{state\}/g, loc.state) : s;
  const contentHtml = content ? `
                <div class="space-y-10">
                    <div>
                        <h2 class="text-[22px] font-bold text-navy-900 mb-4 flex items-center gap-3">
                            <span class="w-8 h-8 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-circle-question text-orange text-[14px]"></i></span>
                            ${r(content.h2_why_need) || `Why You Need It in ${loc.city}`}
                        </h2>
                        <p class="text-slate-600 leading-relaxed text-[15px]">${r(content.why_need)}</p>
                    </div>
                    <div>
                        <h2 class="text-[22px] font-bold text-navy-900 mb-4 flex items-center gap-3">
                            <span class="w-8 h-8 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-star text-orange text-[14px]"></i></span>
                            ${r(content.h2_benefits) || 'What to Expect'}
                        </h2>
                        <p class="text-slate-600 leading-relaxed text-[15px]">${r(content.benefits)}</p>
                    </div>
                    <div>
                        <h2 class="text-[22px] font-bold text-navy-900 mb-4 flex items-center gap-3">
                            <span class="w-8 h-8 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-calendar-check text-orange text-[14px]"></i></span>
                            ${r(content.h2_longevity) || 'How Long Does It Last?'}
                        </h2>
                        <p class="text-slate-600 leading-relaxed text-[15px]">${r(content.longevity)}</p>
                    </div>
                    <div class="rounded-xl p-6 border-l-4 border-orange" style="background:#fff8f5">
                        <h2 class="text-[20px] font-bold text-navy-900 mb-3 flex items-center gap-3">
                            <i class="fas fa-triangle-exclamation text-orange"></i> ${r(content.h2_consequences) || 'The Cost of Waiting'}
                        </h2>
                        <p class="text-slate-600 leading-relaxed text-[15px]">${r(content.consequences)}</p>
                    </div>
                </div>` : `
                <p class="text-slate-600 leading-relaxed text-[15px]">${svc.desc}</p>`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${FAVICON}
    <meta name="description" content="${metaDesc}">
    <link rel="canonical" href="https://thefixwizard.com/${detailSlug}/">
    <title>${title}</title>
    <script type="application/ld+json">${schema(loc, type, detailSlug, metaDesc)}<\/script>
    ${HEAD_STYLES}
    ${FONTS}
</head>
<body>

${navbar(loc, svcParam)}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden pt-[var(--nav-h)] pb-14 rounded-b-[48px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full pt-8">
            <!-- Breadcrumb -->
            <nav class="flex items-center gap-2 text-[12px] mb-8 flex-wrap" style="color:rgba(255,255,255,.4)">
                <a href="/" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.4)">Home</a>
                <i class="fas fa-chevron-right text-[9px]"></i>
                <a href="/${loc.slug}-repair/" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.4)">${loc.city}</a>
                <i class="fas fa-chevron-right text-[9px]"></i>
                <a href="/${hubSlug}/" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.4)">${typeLabel}</a>
                <i class="fas fa-chevron-right text-[9px]"></i>
                <span style="color:rgba(255,255,255,.75)">${svc.name}</span>
            </nav>

            <div class="grid grid-cols-1 tab:grid-cols-[1fr_360px] gap-12 items-start">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-6 tracking-wide">
                        <i class="fas ${typeIcon} text-orange text-[11px]"></i>
                        <span>${typeLabel} · ${loc.city}, ${loc.state}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(24px,3.8vw,50px)] font-black leading-[1.1] tracking-tight text-white mb-5">
                        ${svc.name}<br>
                        <span class="text-orange">Near ${loc.city}, ${loc.state}</span>
                    </h1>
                    <p class="text-[17px] leading-[1.75] mb-8 max-w-[540px]" style="color:rgba(255,255,255,.65)">${svc.desc}</p>
                    <div class="flex items-center gap-3 flex-wrap justify-center tab:justify-start">
                        <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                        <a href="/?service=${svcParam}#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote</a>
                    </div>
                </div>

                <!-- Hero sidebar: includes list -->
                <div class="w-full max-w-[360px] mx-auto tab:mx-0 bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-7">
                    <div class="flex items-center gap-3 mb-5">
                        <div class="w-10 h-10 bg-orange/20 rounded-lg flex items-center justify-center shrink-0">
                            <i class="fas ${svc.icon} text-orange text-[16px]"></i>
                        </div>
                        <div class="text-[15px] font-bold text-white">What's Included</div>
                    </div>
                    <ul class="flex flex-col divide-y divide-white/[.06]">
                        ${includesList}
                    </ul>
                    <a href="/?service=${svcParam}#contact" class="btn btn-primary btn-full mt-6">
                        <i class="fas fa-paper-plane"></i> Get a Free Estimate
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- MAIN CONTENT -->
    <section class="py-20 bg-white">
        <div class="max-w-site mx-auto px-6">
            <div class="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-12 items-start">

                <!-- Article -->
                <article class="reveal">
                ${contentHtml}
                </article>

                <!-- Sidebar -->
                <aside class="flex flex-col gap-6 sticky top-[calc(var(--nav-h)+80px)]">

                    <!-- Back link -->
                    <a href="/${hubSlug}/" class="flex items-center gap-2.5 text-[13px] font-semibold text-orange hover:text-orange-dark transition-colors group">
                        <i class="fas fa-arrow-left text-[11px] group-hover:-translate-x-1 transition-transform"></i>
                        All ${typeLabel} Near ${loc.city}
                    </a>

                    <!-- Quick CTA -->
                    <div class="rounded-card p-6 text-white" style="background:#091236">
                        <div class="text-[16px] font-bold mb-1">Book in ${loc.city}</div>
                        <p class="text-[13px] mb-5" style="color:rgba(255,255,255,.55)">Same-day available · Free estimate · Licensed &amp; insured</p>
                        <a href="tel:+15513504951" class="btn btn-primary btn-full mb-3"><i class="fas fa-phone"></i> (551) 350-4951</a>
                        <a href="/?service=${svcParam}#contact" class="btn btn-outline btn-full text-[13px]"><i class="fas fa-paper-plane"></i> Request Online</a>
                    </div>

                    <!-- Includes list -->
                    <div class="rounded-card border border-slate-100 p-6">
                        <div class="text-[14px] font-bold text-navy-900 mb-3 flex items-center gap-2">
                            <i class="fas fa-list-check text-orange text-[13px]"></i> What's Included
                        </div>
                        <ul class="flex flex-col divide-y divide-slate-100">
                        ${sidebarIncludes}
                        </ul>
                    </div>

                    <!-- Hub links -->
                    <div class="rounded-card border border-slate-100 p-6">
                        <div class="text-[14px] font-bold text-navy-900 mb-3">More in ${loc.city}</div>
                        <div class="flex flex-col gap-2">
                            <a href="/${loc.slug}-repair/" class="text-[13px] text-slate-500 hover:text-orange transition-colors flex items-center gap-2"><i class="fas fa-home text-orange text-[11px]"></i> All Services in ${loc.city}</a>
                            <a href="/handyman-services-near-${loc.slug}/" class="text-[13px] text-slate-500 hover:text-orange transition-colors flex items-center gap-2"><i class="fas fa-screwdriver-wrench text-orange text-[11px]"></i> Handyman Near ${loc.city}</a>
                            <a href="/chimney-services-near-${loc.slug}/" class="text-[13px] text-slate-500 hover:text-orange transition-colors flex items-center gap-2"><i class="fas fa-fire text-orange text-[11px]"></i> Chimney Near ${loc.city}</a>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </section>

    <!-- CTA BANNER -->
    <section class="py-20" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 text-center">
            <h2 class="font-cinzel text-[clamp(22px,3vw,38px)] font-black text-white mb-4">Need ${svc.name} Near ${loc.city}?</h2>
            <p class="text-[16px] mb-10 max-w-[480px] mx-auto" style="color:rgba(255,255,255,.6)">Call now for same-day service in ${loc.county}. Free estimates, no obligation.</p>
            <div class="flex items-center justify-center gap-4 flex-wrap">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="/?service=${svcParam}#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote Online</a>
            </div>
            <p class="text-[13px] mt-6" style="color:rgba(255,255,255,.3)">Also serving: ${loc.nearby}</p>
        </div>
    </section>

${footer()}

    <script type="module" src="/js/service-page.js"><\/script>
    <script>document.getElementById('year').textContent = new Date().getFullYear();<\/script>
</body>
</html>`;
}

// ── Generator ─────────────────────────────────────────────────────────────────

function generate(outDir = ROOT) {
  let count = 0;
  for (const loc of LOCATIONS) {
    for (const type of ['handyman', 'chimney']) {
      const hubDir = path.join(outDir, `${type}-services-near-${loc.slug}`);
      fs.mkdirSync(hubDir, { recursive: true });
      fs.writeFileSync(path.join(hubDir, 'index.html'), hubPage(loc, type), 'utf8');
      count++;

      const services = DATA[type];
      for (const svc of services) {
        const detailDir = path.join(outDir, `${svc.slug}-near-${loc.slug}`);
        fs.mkdirSync(detailDir, { recursive: true });
        fs.writeFileSync(path.join(detailDir, 'index.html'), detailPage(loc, svc, type), 'utf8');
        count++;
      }
    }
  }
  const hubs    = LOCATIONS.length * 2;
  const details = LOCATIONS.length * (DATA.handyman.length + DATA.chimney.length);
  console.log(`✓ ${count} service pages generated (${hubs} hubs + ${details} detail pages across ${LOCATIONS.length} cities)`);
}

module.exports = { generate };
