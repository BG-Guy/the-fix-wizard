'use strict';
const fs   = require('fs');
const path = require('path');
const ROOT = __dirname;

// ── Location data ─────────────────────────────────────────────────────────────

const LOCATIONS = [
  {
    city: 'Cherry Hill', state: 'NJ', stateFull: 'New Jersey',
    county: 'Camden County', slug: 'cherry-hill',
    tagline: 'Our South Jersey Home Base',
    heroParagraph: 'The Fix Wizard is based right here in Cherry Hill — your neighbors in Camden County. We bring licensed chimney repair, masonry restoration, and handyman services to your door, often the same day.',
    chimneyParagraph: 'Our chimney specialists serve Cherry Hill and all of Camden County. From annual sweeping and safety inspections to full tuckpointing, crown repair, and liner installation — every job is done right the first time.',
    handymanParagraph: 'From Voorhees to Haddonfield, our Cherry Hill handyman team handles drywall, painting, plumbing, electrical, furniture assembly, TV mounting, and any general repair on your list.',
    nearby: 'Haddonfield · Voorhees · Merchantville · Pennsauken',
  },
  {
    city: 'Philadelphia', state: 'PA', stateFull: 'Pennsylvania',
    county: 'Philadelphia County', slug: 'philadelphia',
    tagline: 'City of Brotherly Love Coverage',
    heroParagraph: 'From Fishtown to South Philly, Manayunk to Northeast Philly — The Fix Wizard brings licensed chimney repair, masonry, and handyman services throughout Philadelphia and its neighborhoods.',
    chimneyParagraph: 'Philadelphia\'s row homes and older construction demand skilled chimney and masonry work. We service Philly\'s brick chimneys, fireplaces, and masonry with precision — sweeping, tuckpointing, liner install, and full rebuilds.',
    handymanParagraph: 'Philly apartments and row homes need reliable handyman help. We handle drywall repairs, bathroom fixes, fixture installation, furniture assembly, TV mounting, and general maintenance throughout Philadelphia.',
    nearby: 'Fishtown · South Philly · Manayunk · Northeast Philadelphia',
  },
  {
    city: 'Moorestown', state: 'NJ', stateFull: 'New Jersey',
    county: 'Burlington County', slug: 'moorestown',
    tagline: 'Burlington County\'s Trusted Team',
    heroParagraph: 'Moorestown homeowners trust The Fix Wizard for licensed chimney repair, masonry restoration, and full-service handyman work. Burlington County\'s top-rated home repair team, ready same-day.',
    chimneyParagraph: 'Our chimney technicians serve Moorestown and Burlington County with expert sweeping, tuckpointing, crown repair, liner installation, and complete masonry restoration — protecting your home year-round.',
    handymanParagraph: 'Whether you need drywall patching, a new bathroom fixture, furniture assembled, or a TV mounted, our Moorestown handyman team gets it done cleanly and on time.',
    nearby: 'Evesham · Medford · Mount Holly · Marlton',
  },
  {
    city: 'Princeton', state: 'NJ', stateFull: 'New Jersey',
    county: 'Mercer County', slug: 'princeton',
    tagline: 'Serving Mercer County',
    heroParagraph: 'Princeton homeowners rely on The Fix Wizard for licensed chimney repair, masonry, and handyman services. We serve Princeton and all of Mercer County with precision and care.',
    chimneyParagraph: 'Our Princeton chimney team handles everything from routine sweeping and inspections to tuckpointing, damper repair, liner installation, and full masonry restoration for Mercer County homes.',
    handymanParagraph: 'The Fix Wizard\'s Princeton handymen tackle drywall, painting, plumbing, electrical, door repair, furniture assembly, and any home repair task you need handled professionally.',
    nearby: 'Lawrenceville · Hamilton · Pennington · West Windsor',
  },
  {
    city: 'West Chester', state: 'PA', stateFull: 'Pennsylvania',
    county: 'Chester County', slug: 'west-chester',
    tagline: 'Chester County Coverage',
    heroParagraph: 'West Chester homeowners choose The Fix Wizard for licensed chimney repair, masonry, and reliable handyman services. We serve West Chester and Chester County with same-day availability.',
    chimneyParagraph: 'Our chimney specialists serve West Chester and Chester County — sweeping, tuckpointing, crown repair, liner installation, flashing repair, and complete chimney rebuilds done right.',
    handymanParagraph: 'From West Chester to Exton, our handyman team handles drywall repairs, plumbing fixes, light electrical, door installations, furniture assembly, TV mounting, and general repairs.',
    nearby: 'Exton · Malvern · Phoenixville · Downingtown',
  },
  {
    city: 'Wilmington', state: 'DE', stateFull: 'Delaware',
    county: 'New Castle County', slug: 'wilmington',
    tagline: 'Delaware Valley Coverage',
    heroParagraph: 'The Fix Wizard serves Wilmington and New Castle County with the same licensed, insured chimney repair, masonry, and handyman expertise that South Jersey homeowners trust.',
    chimneyParagraph: 'Our Wilmington chimney team provides expert sweeping, safety inspections, tuckpointing, crown repair, liner installation, and masonry restoration throughout New Castle County, DE.',
    handymanParagraph: 'Our handymen serve Wilmington and surrounding Delaware communities with drywall repair, painting, plumbing, electrical, furniture assembly, TV mounting, and complete home maintenance.',
    nearby: 'Newark · Bear · Hockessin · Pike Creek',
  },
  {
    city: 'Haddonfield', state: 'NJ', stateFull: 'New Jersey',
    county: 'Camden County', slug: 'haddonfield',
    tagline: 'Serving Historic Haddonfield',
    heroParagraph: 'Haddonfield\'s historic homes deserve expert care. The Fix Wizard provides licensed chimney repair, masonry restoration, and handyman services tailored to Camden County\'s most beloved borough.',
    chimneyParagraph: 'Haddonfield\'s older homes often need careful chimney attention. Our specialists handle tuckpointing, crown repair, liner installation, waterproofing, and full masonry restoration with precision.',
    handymanParagraph: 'From historic repairs to modern upgrades, our Haddonfield handyman team handles drywall, painting, plumbing, electrical, fixture installation, furniture assembly, and general repairs.',
    nearby: 'Cherry Hill · Collingswood · Westmont · Lawnside',
  },
  {
    city: 'Mount Laurel', state: 'NJ', stateFull: 'New Jersey',
    county: 'Burlington County', slug: 'mount-laurel',
    tagline: 'Burlington County Service',
    heroParagraph: 'Mount Laurel homeowners trust The Fix Wizard for licensed chimney repair, masonry, and handyman services. Serving Burlington County\'s fastest-growing township with same-day availability.',
    chimneyParagraph: 'Our chimney technicians serve Mount Laurel and Burlington County — from routine sweeping and inspections to tuckpointing, liner installation, cap replacement, and complete chimney repair.',
    handymanParagraph: 'The Fix Wizard\'s Mount Laurel team handles drywall, painting, plumbing, electrical, furniture assembly, TV mounting, and all the general repairs your home needs.',
    nearby: 'Moorestown · Marlton · Evesham · Maple Shade',
  },
  {
    city: 'Marlton', state: 'NJ', stateFull: 'New Jersey',
    county: 'Burlington County', slug: 'marlton',
    tagline: 'Evesham Township Coverage',
    heroParagraph: 'Marlton and Evesham Township homeowners turn to The Fix Wizard for licensed chimney repair, masonry, and reliable handyman services — same-day available across Burlington County.',
    chimneyParagraph: 'Our chimney specialists serve Marlton and surrounding Burlington County communities with thorough sweeping, tuckpointing, crown repair, liner installation, and full masonry restoration.',
    handymanParagraph: 'From drywall patching to bathroom upgrades, fixture installation, furniture assembly, and TV mounting — The Fix Wizard\'s Marlton team handles every home repair quickly and professionally.',
    nearby: 'Voorhees · Cherry Hill · Mount Laurel · Medford',
  },
  {
    city: 'Voorhees', state: 'NJ', stateFull: 'New Jersey',
    county: 'Camden County', slug: 'voorhees',
    tagline: 'Serving Voorhees & Camden County',
    heroParagraph: 'Voorhees homeowners rely on The Fix Wizard for licensed chimney repair, masonry restoration, and professional handyman services. Camden County\'s trusted home repair team, available same-day.',
    chimneyParagraph: 'Our Voorhees chimney team provides expert sweeping, inspections, tuckpointing, crown repair, liner installation, and masonry restoration for Camden County homes.',
    handymanParagraph: 'The Fix Wizard serves Voorhees and surrounding Camden County communities with drywall, painting, plumbing, electrical, assembly, TV mounting, and any general repair task.',
    nearby: 'Cherry Hill · Marlton · Gibbsboro · Lawnside',
  },
  {
    city: 'Trenton', state: 'NJ', stateFull: 'New Jersey',
    county: 'Mercer County', slug: 'trenton',
    tagline: 'Mercer County Coverage',
    heroParagraph: 'The Fix Wizard serves Trenton and Mercer County with licensed chimney repair, masonry, and handyman services. Trusted by homeowners across the capital region.',
    chimneyParagraph: 'Our Trenton chimney specialists handle sweeping, safety inspections, tuckpointing, crown repair, liner installation, and complete masonry restoration throughout Mercer County.',
    handymanParagraph: 'From Trenton to Hamilton, our handyman team handles drywall, painting, plumbing, electrical, doors, furniture assembly, TV mounting, and the full range of home repairs.',
    nearby: 'Hamilton · Lawrence · Ewing · Bordentown',
  },
  {
    city: 'Wayne', state: 'PA', stateFull: 'Pennsylvania',
    county: 'Delaware County', slug: 'wayne',
    tagline: 'Main Line & Delaware County',
    heroParagraph: 'Wayne and the Main Line corridor trust The Fix Wizard for licensed chimney repair, masonry restoration, and professional handyman services — the same quality South Jersey relies on.',
    chimneyParagraph: 'Our chimney technicians serve Wayne and Delaware County with expert sweeping, tuckpointing, crown repair, liner installation, flashing repair, and complete masonry restoration.',
    handymanParagraph: 'The Fix Wizard\'s Wayne team handles drywall repair, painting, plumbing, electrical, door installation, furniture assembly, TV mounting, and general home repairs on the Main Line.',
    nearby: 'Radnor · Bryn Mawr · Villanova · Paoli',
  },
  {
    city: 'King of Prussia', state: 'PA', stateFull: 'Pennsylvania',
    county: 'Montgomery County', slug: 'king-of-prussia',
    tagline: 'Montgomery County Coverage',
    heroParagraph: 'King of Prussia and Montgomery County homeowners trust The Fix Wizard for licensed chimney repair, masonry, and handyman services. Same-day availability, free estimates.',
    chimneyParagraph: 'Our chimney specialists serve King of Prussia and surrounding Montgomery County — thorough sweeping, tuckpointing, crown repair, liner installation, and full masonry restoration.',
    handymanParagraph: 'From KOP to Upper Merion Township, our handyman team handles drywall, painting, plumbing, electrical, furniture assembly, TV mounting, and all home repair needs.',
    nearby: 'Upper Merion · Norristown · Collegeville · Phoenixville',
  },
  {
    city: 'Atlantic City', state: 'NJ', stateFull: 'New Jersey',
    county: 'Atlantic County', slug: 'atlantic-city',
    tagline: 'Atlantic County Coverage',
    heroParagraph: 'Atlantic City and Atlantic County homeowners turn to The Fix Wizard for licensed chimney repair, masonry, and handyman services. Coastal homes need extra care — we deliver it.',
    chimneyParagraph: 'Coastal climates accelerate chimney wear. Our Atlantic City chimney team handles sweeping, tuckpointing, crown repair, waterproofing, liner installation, and full masonry restoration.',
    handymanParagraph: 'From Atlantic City to Egg Harbor, our handyman team handles drywall, painting, plumbing, electrical, fixture installation, furniture assembly, and coastal home repairs of all kinds.',
    nearby: 'Galloway · Egg Harbor · Absecon · Brigantine',
  },
];

// ── Shared elements ───────────────────────────────────────────────────────────

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
                        <a href="/philadelphia-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Philadelphia</a>
                        <a href="/moorestown-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Moorestown</a>
                        <a href="/princeton-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Princeton</a>
                        <a href="/west-chester-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> West Chester</a>
                        <a href="/wilmington-repair/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Wilmington</a>
                        <div class="nav-dropdown-divider"></div>
                        <a href="/locations/" class="nav-dropdown-item" style="color:rgba(255,255,255,.45)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
                    </div>
                </li>
            </ul>
            <div class="hidden md:flex items-center gap-4 shrink-0 nav-actions">
                <a href="tel:+15513504951" class="flex items-center gap-2 text-white/75 text-sm font-medium hover:text-orange transition-colors">
                    <i class="fas fa-phone text-orange"></i>
                    <span>(551) 350-4951</span>
                </a>
                <a href="${contactHref}" class="btn btn-primary nav-cta relative overflow-hidden">
                    Free Quote
                    <svg class="btn-spark bs-1" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                    <svg class="btn-spark bs-2" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                    <svg class="btn-spark bs-3" viewBox="0 0 24 24"><path d="M12 2L13.8 10.2L22 12L13.8 13.8L12 22L10.2 13.8L2 12L10.2 10.2Z" fill="currentColor"/></svg>
                </a>
            </div>
            <button class="hamburger md:hidden flex flex-col gap-[5px] cursor-pointer bg-transparent border-none p-2 order-first" id="hamburger" aria-label="Toggle menu">
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
                <span class="block w-6 h-0.5 bg-white rounded-sm transition-all"></span>
            </button>
        </div>
    </nav>
    <div class="mobile-menu fixed top-0 z-[101] w-[min(320px,88vw)] h-screen bg-navy-900 pt-[76px] px-7 pb-9 flex flex-col gap-1.5 overflow-y-auto" id="mobileMenu">
        <button class="absolute top-[18px] right-[18px] bg-white/10 border-none text-white w-[38px] h-[38px] rounded-full flex items-center justify-center cursor-pointer text-[15px] transition-all hover:bg-orange mobile-menu-close" id="mobileClose" aria-label="Close menu">
            <i class="fas fa-times"></i>
        </button>
        <ul class="flex flex-col gap-0.5 mb-5 mobile-nav-links">
            <li><a href="/" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Home</a></li>
            <li><a href="/#services" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Services</a></li>
            <li><a href="/#why-us" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">About</a></li>
            <li><a href="${contactHref}" class="mobile-link block text-white/80 text-[17px] font-semibold px-3.5 py-3 rounded-lg transition-all hover:text-white hover:bg-white/[.08]">Contact</a></li>
            <li>
                <span class="mobile-loc-label">South Jersey &amp; Delaware Valley</span>
                <a href="/cherry-hill-repair/"  class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Cherry Hill</a>
                <a href="/philadelphia-repair/" class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Philadelphia</a>
                <a href="/moorestown-repair/"   class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Moorestown</a>
                <a href="/princeton-repair/"    class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Princeton</a>
                <a href="/west-chester-repair/" class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> West Chester</a>
                <a href="/wilmington-repair/"   class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Wilmington</a>
                <a href="/locations/" class="mobile-link mobile-loc-sub" style="color:rgba(255,255,255,.4)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
            </li>
        </ul>
        <a href="tel:+15513504951" class="mobile-phone flex items-center gap-2.5 text-white/65 text-sm mb-3.5 px-3.5">
            <i class="fas fa-phone text-orange"></i>(551) 350-4951
        </a>
        <a href="${contactHref}" class="btn btn-primary mobile-cta mobile-link mt-1.5">Get Free Quote</a>
    </div>
    <div class="mobile-overlay fixed inset-0 bg-black/50 z-[100] opacity-0 invisible transition-all backdrop-blur-sm" id="mobileOverlay"></div>`;
}

function footer() {
  return `    <footer class="pt-20 pb-0" style="background-color:#091236;background-image:url(\\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Cpath d='M20 16L21.5 18.5L24 20L21.5 21.5L20 24L18.5 21.5L16 20L18.5 18.5Z' fill='rgba(255,255,255,.03)'/%3E%3C/svg%3E\\");background-size:80px 80px">
        <div class="max-w-site mx-auto px-6 pb-[60px]">
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-[2fr_1fr_1fr_1fr] gap-12">
                <div class="md:col-span-3 lg:col-span-1 flex flex-col items-center md:items-start text-center md:text-left">
                    <a href="/" class="inline-block mb-[18px]">
                        <img src="/assets/images/the-fix-wizard-logo.webp" alt="The Fix Wizard" class="h-[64px] w-auto object-contain rounded-lg" width="199" height="64" loading="lazy">
                    </a>
                    <p class="text-[15px] leading-[1.7] mb-[22px]" style="color:rgba(255,255,255,.55)">The Fix Wizard handles the repairs most people dread. Quality work, honest pricing, and results that last.</p>
                    <div class="flex gap-2.5 justify-center md:justify-start">
                        <a href="#" aria-label="Facebook"  class="w-[38px] h-[38px] rounded-lg flex items-center justify-center text-[15px] transition-all hover:-translate-y-0.5 hover:bg-orange hover:border-orange hover:text-white" style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.55)"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" aria-label="Instagram" class="w-[38px] h-[38px] rounded-lg flex items-center justify-center text-[15px] transition-all hover:-translate-y-0.5 hover:bg-orange hover:border-orange hover:text-white" style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.55)"><i class="fab fa-instagram"></i></a>
                        <a href="#" aria-label="Google"    class="w-[38px] h-[38px] rounded-lg flex items-center justify-center text-[15px] transition-all hover:-translate-y-0.5 hover:bg-orange hover:border-orange hover:text-white" style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.55)"><i class="fab fa-google"></i></a>
                        <a href="#" aria-label="Yelp"      class="w-[38px] h-[38px] rounded-lg flex items-center justify-center text-[15px] transition-all hover:-translate-y-0.5 hover:bg-orange hover:border-orange hover:text-white" style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.55)"><i class="fab fa-yelp"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Services</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li><a href="/services/chimney/" class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Chimney &amp; Masonry</a></li>
                        <li><a href="/services/handyman/" class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Handyman Services</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Service Areas</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li><a href="/cherry-hill-repair/"      class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Cherry Hill, NJ</a></li>
                        <li><a href="/philadelphia-repair/"     class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Philadelphia, PA</a></li>
                        <li><a href="/moorestown-repair/"       class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Moorestown, NJ</a></li>
                        <li><a href="/princeton-repair/"        class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Princeton, NJ</a></li>
                        <li><a href="/west-chester-repair/"     class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">West Chester, PA</a></li>
                        <li><a href="/wilmington-repair/"       class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.5)">Wilmington, DE</a></li>
                        <li><a href="/locations/" class="text-[14px] transition-all hover:text-orange hover:translate-x-1" style="color:rgba(255,255,255,.35)">All Locations &rarr;</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-[14px] font-bold text-white mb-[18px] tracking-wide">Contact</h4>
                    <ul class="flex flex-col gap-[9px]">
                        <li class="flex items-center gap-2.5 text-[14px]" style="color:rgba(255,255,255,.5)"><i class="fas fa-phone text-orange w-4 shrink-0"></i><a href="tel:+15513504951" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.5)">(551) 350-4951</a></li>
                        <li class="flex items-center gap-2.5 text-[14px]" style="color:rgba(255,255,255,.5)"><i class="fas fa-envelope text-orange w-4 shrink-0"></i><a href="mailto:office@thefixwizard.com" class="hover:text-orange transition-colors" style="color:rgba(255,255,255,.5)">office@thefixwizard.com</a></li>
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

function schema(loc, type, description) {
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'HomeAndConstructionBusiness',
    name: 'The Fix Wizard',
    description,
    url: `https://thefixwizard.com/${loc.slug}-repair/`,
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

function hubPage(loc) {
  const cityState = `${loc.city}, ${loc.state}`;
  const title = `Chimney &amp; Handyman Services in ${loc.city}, ${loc.state} | The Fix Wizard`;
  const metaDesc = `Licensed chimney repair and handyman services in ${cityState}. Same-day available. Free estimates. The Fix Wizard — ${loc.county}'s trusted home repair team.`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${FAVICON}
    <meta name="description" content="${metaDesc}">
    <title>${title}</title>
    <script type="application/ld+json">${schema(loc, 'hub', metaDesc)}<\/script>
    ${HEAD_STYLES}
    ${FONTS}
</head>
<body>

${navbar(loc)}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-map-marker-alt text-orange text-[11px]"></i>
                        <span>Serving ${loc.city}, ${loc.state}</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(28px,4.5vw,58px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Home Repair Services<br>
                        <span class="text-orange">in ${loc.city}, ${loc.state}</span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-8 max-w-[540px]">${loc.heroParagraph}</p>
                    <div class="flex items-center gap-3 mb-12 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="/chimney-services-near-${loc.slug}/" class="btn btn-primary btn-lg">
                            <i class="fas fa-fire"></i> Chimney Services
                        </a>
                        <a href="/handyman-services-near-${loc.slug}/" class="btn btn-outline btn-lg">
                            <i class="fas fa-screwdriver-wrench"></i> Handyman Services
                        </a>
                    </div>
                    <div class="w-full h-px bg-white/10 mb-8"></div>
                    <div class="flex items-center gap-8 flex-wrap justify-center tab:justify-start hero-stats">
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1">500+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Jobs Done</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1">10+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Years Exp</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1">98%</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Satisfaction</div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[420px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-5">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas fa-home"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">Services in ${loc.city}</div>
                                <p class="text-[13px] text-white/50">Same-day service · Free estimates</p>
                            </div>
                        </div>
                        <a href="/chimney-services-near-${loc.slug}/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-10 h-10 bg-orange/20 rounded-lg flex items-center justify-center shrink-0 group-hover:bg-orange/30 transition-colors">
                                <i class="fas fa-fire text-orange"></i>
                            </div>
                            <div class="flex-1">
                                <div class="text-[14px] font-bold text-white">Chimney &amp; Masonry</div>
                                <div class="text-[12px] text-white/50">Sweeping · Tuckpointing · Liner Install</div>
                            </div>
                            <i class="fas fa-arrow-right text-orange/60 text-[12px] group-hover:translate-x-1 transition-transform"></i>
                        </a>
                        <a href="/handyman-services-near-${loc.slug}/" class="group flex items-center gap-4 bg-white/[.07] border border-white/[.1] rounded-xl p-4 transition-all hover:bg-orange/[.15] hover:border-orange/40">
                            <div class="w-10 h-10 bg-orange/20 rounded-lg flex items-center justify-center shrink-0 group-hover:bg-orange/30 transition-colors">
                                <i class="fas fa-screwdriver-wrench text-orange"></i>
                            </div>
                            <div class="flex-1">
                                <div class="text-[14px] font-bold text-white">Handyman Services</div>
                                <div class="text-[12px] text-white/50">Drywall · Plumbing · Assembly</div>
                            </div>
                            <i class="fas fa-arrow-right text-orange/60 text-[12px] group-hover:translate-x-1 transition-transform"></i>
                        </a>
                        <a href="/#contact" class="btn btn-primary btn-full">
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
    </section>

    <!-- SERVICES -->
    <section class="relative overflow-hidden py-24" style="background-color:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="max-w-site mx-auto px-6">
            <div class="section-header reveal">
                <span class="section-tag">What We Do in ${loc.city}</span>
                <h2 class="section-title">Our <span class="text-orange">2 Specialties</span></h2>
                <p class="section-desc">Two focused services, done with precision. Chimney &amp; Masonry and Handyman Services delivered to ${cityState} homeowners.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-[860px] mx-auto">
                <div class="group relative bg-white rounded-card border border-slate-200 flex flex-col overflow-hidden cursor-pointer transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.22),0_10px_24px_-6px_rgba(255,107,53,.2)] hover:border-transparent reveal">
                    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-dark via-orange to-orange-light scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-left rounded-b-card z-10"></div>
                    <img src="/assets/images/chimney-repair-in-new-jersey.webp" alt="Chimney repair in ${cityState}" class="w-full h-[220px] object-cover object-top shrink-0 transition-transform duration-500 group-hover:scale-105" width="800" height="220" loading="lazy">
                    <div class="p-7 flex flex-col gap-3 flex-1">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-fire text-orange text-[16px]"></i></div>
                            <h3 class="text-[20px] font-bold text-navy-900 leading-snug">Chimney &amp; Masonry in ${loc.city}</h3>
                        </div>
                        <p class="text-sm text-slate-500 leading-relaxed flex-1">${loc.chimneyParagraph}</p>
                        <ul class="flex flex-col gap-1.5 text-sm text-slate-600 mb-1">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Chimney sweeping &amp; inspection</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Tuckpointing &amp; mortar repair</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Crown repair, cap &amp; liner install</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Brick &amp; masonry restoration</li>
                        </ul>
                        <a href="/chimney-services-near-${loc.slug}/" class="stretched-link inline-flex items-center gap-2 text-sm font-semibold text-orange hover:text-orange-dark transition-colors mt-auto">Chimney Services in ${loc.city} <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i></a>
                    </div>
                </div>
                <div class="group relative bg-white rounded-card border border-slate-200 flex flex-col overflow-hidden cursor-pointer transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.22),0_10px_24px_-6px_rgba(255,107,53,.2)] hover:border-transparent reveal">
                    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-dark via-orange to-orange-light scale-x-0 group-hover:scale-x-100 transition-transform duration-500 origin-left rounded-b-card z-10"></div>
                    <img src="/assets/images/tv-mounting-new-jersey.webp" alt="Handyman services in ${cityState}" class="w-full h-[220px] object-cover object-top shrink-0 transition-transform duration-500 group-hover:scale-105" width="800" height="220" loading="lazy">
                    <div class="p-7 flex flex-col gap-3 flex-1">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 bg-orange/10 rounded-lg flex items-center justify-center shrink-0"><i class="fas fa-screwdriver-wrench text-orange text-[16px]"></i></div>
                            <h3 class="text-[20px] font-bold text-navy-900 leading-snug">Handyman Services in ${loc.city}</h3>
                        </div>
                        <p class="text-sm text-slate-500 leading-relaxed flex-1">${loc.handymanParagraph}</p>
                        <ul class="flex flex-col gap-1.5 text-sm text-slate-600 mb-1">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Drywall repair &amp; painting</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Doors, plumbing &amp; light electrical</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> Furniture assembly &amp; TV mounting</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[11px]"></i> General repairs — any size job</li>
                        </ul>
                        <a href="/handyman-services-near-${loc.slug}/" class="stretched-link inline-flex items-center gap-2 text-sm font-semibold text-orange hover:text-orange-dark transition-colors mt-auto">Handyman Services in ${loc.city} <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TRUST -->
    <section class="py-20 bg-white">
        <div class="max-w-site mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 reveal">
                <div class="flex flex-col items-center text-center p-8 rounded-card border border-slate-100 hover:border-orange/20 transition-colors">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-5"><i class="fas fa-shield-halved text-orange text-2xl"></i></div>
                    <h3 class="text-[18px] font-bold text-navy-900 mb-2">Licensed &amp; Insured</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">Fully licensed and insured in ${loc.stateFull} for all chimney and handyman services. Every technician is background-checked.</p>
                </div>
                <div class="flex flex-col items-center text-center p-8 rounded-card border border-slate-100 hover:border-orange/20 transition-colors">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-5"><i class="fas fa-clock text-orange text-2xl"></i></div>
                    <h3 class="text-[18px] font-bold text-navy-900 mb-2">Same-Day Available</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">Urgent repair in ${loc.city}? Call us. We offer same-day scheduling when slots are open — Mon through Sat, 7am to 7pm.</p>
                </div>
                <div class="flex flex-col items-center text-center p-8 rounded-card border border-slate-100 hover:border-orange/20 transition-colors">
                    <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center mb-5"><i class="fas fa-file-invoice-dollar text-orange text-2xl"></i></div>
                    <h3 class="text-[18px] font-bold text-navy-900 mb-2">Free Estimates</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">No surprises. Every job in ${loc.city} starts with a free estimate so you know exactly what to expect before we begin.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 text-center">
            <h2 class="font-cinzel text-[clamp(26px,4vw,44px)] font-black text-white mb-4">Ready to Fix Something in ${loc.city}?</h2>
            <p class="text-[17px] text-white/60 mb-10 max-w-[520px] mx-auto">Call now or request a free estimate online. We serve ${loc.city} and nearby ${loc.nearby}.</p>
            <div class="flex items-center justify-center gap-4 flex-wrap">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="/#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote Online</a>
            </div>
        </div>
    </section>

${footer()}

    <script type="module" src="/js/service-page.js"><\/script>
    <script>document.getElementById('year').textContent = new Date().getFullYear();<\/script>
</body>
</html>`;
}

// ── Chimney child page ────────────────────────────────────────────────────────

function chimneyPage(loc) {
  const cityState = `${loc.city}, ${loc.state}`;
  const title = `Chimney Repair in ${loc.city}, ${loc.state} | The Fix Wizard`;
  const metaDesc = `Expert chimney repair and masonry in ${cityState} — sweeping, tuckpointing, crown repair, liner installation. Licensed &amp; insured. Same-day available. Free estimates.`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${FAVICON}
    <meta name="description" content="${metaDesc}">
    <title>${title}</title>
    <script type="application/ld+json">${schema(loc, 'chimney', metaDesc)}<\/script>
    ${HEAD_STYLES}
    ${FONTS}
</head>
<body>

${navbar(loc, 'Chimney+%26+Masonry')}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-[80vh] pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_380px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <a href="/${loc.slug}-repair/" class="inline-flex items-center gap-2 text-orange/80 hover:text-orange text-[13px] font-semibold mb-5 transition-colors">
                        <i class="fas fa-arrow-left text-[11px]"></i> All Services in ${loc.city}
                    </a>
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-fire text-orange text-[11px]"></i>
                        <span>Chimney &amp; Masonry Specialists</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(28px,4.5vw,58px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Chimney Repair<br>
                        <span class="text-orange">in ${loc.city}, ${loc.state}</span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-8 max-w-[540px]">${loc.chimneyParagraph}</p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-broom text-orange text-[12px]"></i> Sweeping</div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-trowel-bricks text-orange text-[12px]"></i> Tuckpointing</div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-pipe text-orange text-[12px]"></i> Liner Install</div>
                    </div>
                    <div class="flex items-center gap-3 mb-10 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                        <a href="/?service=Chimney+%26+Masonry#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote</a>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[380px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-7 flex flex-col gap-4">
                        <div class="text-[15px] font-semibold text-white mb-1">Chimney Services in ${loc.city}</div>
                        <ul class="flex flex-col gap-3">
                            ${['Chimney sweeping &amp; inspection','Tuckpointing &amp; mortar repair','Crown repair &amp; replacement','Chimney liner installation','Cap &amp; damper installation','Flashing repair &amp; waterproofing','Brick &amp; masonry restoration','Full chimney rebuilds'].map(s =>
                              `<li class="flex items-center gap-2.5 text-[13px] text-white/70"><i class="fas fa-check text-orange text-[11px] shrink-0"></i>${s}</li>`
                            ).join('\n                            ')}
                        </ul>
                        <a href="/?service=Chimney+%26+Masonry#contact" class="btn btn-primary btn-full mt-2">
                            <i class="fas fa-paper-plane"></i> Get a Free Estimate
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SERVICES DETAIL -->
    <section class="py-24" style="background-color:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="max-w-site mx-auto px-6">
            <div class="section-header reveal">
                <span class="section-tag">Chimney Services in ${loc.city}</span>
                <h2 class="section-title">What We <span class="text-orange">Repair &amp; Restore</span></h2>
                <p class="section-desc">From routine maintenance to emergency repairs — complete chimney and masonry services for ${cityState} homeowners.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 reveal">
                ${[
                  ['fa-broom','Chimney Sweeping & Inspection','Annual sweeping removes creosote and debris. Our thorough inspection checks the firebox, flue, crown, cap, and flashing — catching issues before they become costly.'],
                  ['fa-trowel-bricks','Tuckpointing & Mortar Repair','Deteriorating mortar joints let water into your chimney structure. We repoint with matched mortar to restore strength and protect against water damage.'],
                  ['fa-helmet-safety','Crown & Cap Repair','The chimney crown and cap are your first defense against water. We repair cracked crowns and install or replace caps to keep the flue dry.'],
                  ['fa-pipe','Liner Installation','A damaged or missing liner is a fire and CO hazard. We install stainless steel or clay tile liners to restore safe, efficient operation.'],
                  ['fa-water','Waterproofing & Flashing','Chimney flashing leaks cause serious water damage. We seal, reseal, or replace flashing and apply waterproofing treatments to protect the entire system.'],
                  ['fa-bricks','Brick & Masonry Restoration','Spalling brick, crumbling mortar, and structural damage all get addressed with expert masonry restoration that matches your home\'s existing material.'],
                ].map(([icon, title, desc]) => `
                <div class="bg-white rounded-card p-7 border border-slate-100 hover:border-orange/20 hover:shadow-card transition-all">
                    <div class="w-11 h-11 bg-orange/10 rounded-lg flex items-center justify-center mb-4"><i class="fas ${icon} text-orange text-[16px]"></i></div>
                    <h3 class="text-[17px] font-bold text-navy-900 mb-2">${title}</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">${desc}</p>
                </div>`).join('')}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 text-center">
            <h2 class="font-cinzel text-[clamp(24px,3.5vw,40px)] font-black text-white mb-4">Chimney Problem in ${loc.city}?</h2>
            <p class="text-[17px] text-white/60 mb-10 max-w-[500px] mx-auto">Call now for same-day chimney repair in ${loc.county}. Free estimates, no obligation.</p>
            <div class="flex items-center justify-center gap-4 flex-wrap">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="/?service=Chimney+%26+Masonry#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote Online</a>
            </div>
            <p class="text-[13px] text-white/35 mt-6">Also serving: ${loc.nearby}</p>
        </div>
    </section>

${footer()}

    <script type="module" src="/js/service-page.js"><\/script>
    <script>document.getElementById('year').textContent = new Date().getFullYear();<\/script>
</body>
</html>`;
}

// ── Handyman child page ───────────────────────────────────────────────────────

function handymanPage(loc) {
  const cityState = `${loc.city}, ${loc.state}`;
  const title = `Handyman Services in ${loc.city}, ${loc.state} | The Fix Wizard`;
  const metaDesc = `Professional handyman services in ${cityState} — drywall, painting, plumbing, electrical, TV mounting, furniture assembly. Same-day available. Free estimates.`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${FAVICON}
    <meta name="description" content="${metaDesc}">
    <title>${title}</title>
    <script type="application/ld+json">${schema(loc, 'handyman', metaDesc)}<\/script>
    ${HEAD_STYLES}
    ${FONTS}
</head>
<body>

${navbar(loc, 'Handyman+Services')}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-[80vh] pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_380px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <a href="/${loc.slug}-repair/" class="inline-flex items-center gap-2 text-orange/80 hover:text-orange text-[13px] font-semibold mb-5 transition-colors">
                        <i class="fas fa-arrow-left text-[11px]"></i> All Services in ${loc.city}
                    </a>
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-screwdriver-wrench text-orange text-[11px]"></i>
                        <span>Handyman Specialists</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(28px,4.5vw,58px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Handyman Services<br>
                        <span class="text-orange">in ${loc.city}, ${loc.state}</span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-8 max-w-[540px]">${loc.handymanParagraph}</p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-paint-roller text-orange text-[12px]"></i> Drywall</div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-faucet text-orange text-[12px]"></i> Plumbing</div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80"><i class="fas fa-tv text-orange text-[12px]"></i> TV Mounting</div>
                    </div>
                    <div class="flex items-center gap-3 mb-10 flex-wrap justify-center tab:justify-start hero-actions">
                        <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                        <a href="/?service=Handyman+Services#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote</a>
                    </div>
                </div>
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[380px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-7 flex flex-col gap-4">
                        <div class="text-[15px] font-semibold text-white mb-1">Handyman Services in ${loc.city}</div>
                        <ul class="flex flex-col gap-3">
                            ${['Drywall repair &amp; patching','Interior painting','Door installation &amp; repair','Light plumbing','Light electrical','Furniture assembly','TV mounting &amp; cable management','Bathroom fixture installation','General repairs — any size'].map(s =>
                              `<li class="flex items-center gap-2.5 text-[13px] text-white/70"><i class="fas fa-check text-orange text-[11px] shrink-0"></i>${s}</li>`
                            ).join('\n                            ')}
                        </ul>
                        <a href="/?service=Handyman+Services#contact" class="btn btn-primary btn-full mt-2">
                            <i class="fas fa-paper-plane"></i> Get a Free Estimate
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SERVICES DETAIL -->
    <section class="py-24" style="background-color:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="max-w-site mx-auto px-6">
            <div class="section-header reveal">
                <span class="section-tag">Handyman Services in ${loc.city}</span>
                <h2 class="section-title">One Call <span class="text-orange">Covers It All</span></h2>
                <p class="section-desc">From quick fixes to full-day projects — professional handyman services for ${cityState} homeowners, done right the first time.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 reveal">
                ${[
                  ['fa-layer-group','Drywall Repair','Holes, cracks, water damage, and texture matching — our drywall repairs are seamless and ready to paint in most cases the same day.'],
                  ['fa-paint-roller','Painting','Interior painting done clean and precise. We prep surfaces properly so the finish lasts — walls, trim, ceilings, doors.'],
                  ['fa-door-open','Door Installation & Repair','Interior and exterior door hanging, adjustment, weatherstripping, and hardware installation. We make sure every door opens and closes smoothly.'],
                  ['fa-faucet','Light Plumbing','Faucet replacement, toilet installation, garbage disposal swap, supply line replacement, under-sink repairs — no major pipe work needed.'],
                  ['fa-bolt','Light Electrical','Outlet replacement, switch installation, ceiling fan hanging, light fixture swap, and GFCI installation. Licensed for code-compliant work.'],
                  ['fa-tv','TV Mounting & Assembly','Full-service TV mounting with concealed cables, plus furniture assembly for flat-pack and ready-to-assemble items of any complexity.'],
                ].map(([icon, title, desc]) => `
                <div class="bg-white rounded-card p-7 border border-slate-100 hover:border-orange/20 hover:shadow-card transition-all">
                    <div class="w-11 h-11 bg-orange/10 rounded-lg flex items-center justify-center mb-4"><i class="fas ${icon} text-orange text-[16px]"></i></div>
                    <h3 class="text-[17px] font-bold text-navy-900 mb-2">${title}</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">${desc}</p>
                </div>`).join('')}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20" style="background-color:#091236">
        <div class="max-w-site mx-auto px-6 text-center">
            <h2 class="font-cinzel text-[clamp(24px,3.5vw,40px)] font-black text-white mb-4">Need a Handyman in ${loc.city}?</h2>
            <p class="text-[17px] text-white/60 mb-10 max-w-[500px] mx-auto">Call now or request a free estimate online. Same-day available in ${loc.county}.</p>
            <div class="flex items-center justify-center gap-4 flex-wrap">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="/?service=Handyman+Services#contact" class="btn btn-outline btn-lg"><i class="fas fa-paper-plane"></i> Free Quote Online</a>
            </div>
            <p class="text-[13px] text-white/35 mt-6">Also serving: ${loc.nearby}</p>
        </div>
    </section>

${footer()}

    <script type="module" src="/js/service-page.js"><\/script>
    <script>document.getElementById('year').textContent = new Date().getFullYear();<\/script>
</body>
</html>`;
}

// ── Runner ────────────────────────────────────────────────────────────────────

function generate() {
  let count = 0;
  for (const loc of LOCATIONS) {
    const dirs = [
      { dir: `${loc.slug}-repair`,              html: hubPage(loc) },
      { dir: `chimney-services-${loc.slug}`,    html: chimneyPage(loc) },
      { dir: `handyman-services-${loc.slug}`,   html: handymanPage(loc) },
    ];
    for (const { dir, html } of dirs) {
      fs.mkdirSync(path.join(ROOT, dir), { recursive: true });
      fs.writeFileSync(path.join(ROOT, dir, 'index.html'), html, 'utf8');
      count++;
    }
  }
  console.log(`✓ ${count} location pages generated (${LOCATIONS.length} cities × 3 page types)`);
}

module.exports = { generate };
