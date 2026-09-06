#!/usr/bin/env python3
"""
Generates:
  1. /locations/index.html  — hub page with all 21 NJ county cards
  2. /[service]-in-[county]-nj/index.html  — 168 service-area pages (21 × 8)
     Each page contains 13–15 H3 sub-service headings targeting long-tail keywords.
  3. Patches Locations nav link into all existing service pages and blog posts
"""

import os
from services_data import (
    CHIMNEY_CATS as SD_CHIMNEY_CATS, HANDYMAN_CATS as SD_HANDYMAN_CATS,
    CHIMNEY_SERVICES_FULL, HANDYMAN_SERVICES_FULL, build_service_lookup,
)

ROOT = os.path.dirname(os.path.abspath(__file__))

# ─── Data ──────────────────────────────────────────────────────────────────────

COUNTIES = [
    {"name": "Bergen County",    "slug": "bergen-county-nj",    "towns": "Hackensack, Paramus, Fort Lee, Englewood",             "desc": "NJ's most populous county — dense suburban neighborhoods with aging homes in need of expert repair."},
    {"name": "Essex County",     "slug": "essex-county-nj",     "towns": "Newark, Montclair, Bloomfield, Maplewood",             "desc": "From Newark's urban housing to Montclair's Victorian homes — skilled repairs for every property type."},
    {"name": "Middlesex County", "slug": "middlesex-county-nj", "towns": "Edison, New Brunswick, Woodbridge, Piscataway",        "desc": "Fast-growing county with diverse housing stock, from ranch homes to newer developments."},
    {"name": "Monmouth County",  "slug": "monmouth-county-nj",  "towns": "Red Bank, Freehold, Asbury Park, Middletown",          "desc": "Shore county with coastal homes, salt-air wear, and a mix of historic and modern properties."},
    {"name": "Morris County",    "slug": "morris-county-nj",    "towns": "Morristown, Parsippany, Madison, Rockaway",            "desc": "Wooded suburbs with colonial and split-level homes common across northern New Jersey."},
    {"name": "Hudson County",    "slug": "hudson-county-nj",    "towns": "Jersey City, Hoboken, Bayonne, Union City",            "desc": "Densely packed brownstones, townhouses, and multi-family buildings in one of NJ's busiest counties."},
    {"name": "Union County",     "slug": "union-county-nj",     "towns": "Elizabeth, Westfield, Summit, Plainfield",             "desc": "Central NJ county blending affluent suburbs with working-class neighborhoods — we serve them all."},
    {"name": "Ocean County",     "slug": "ocean-county-nj",     "towns": "Toms River, Lakewood, Brick, Jackson",                 "desc": "Shore and inland county where storm damage repairs and coastal home maintenance are a year-round need."},
    {"name": "Somerset County",  "slug": "somerset-county-nj",  "towns": "Bridgewater, Somerville, Bound Brook, Raritan",        "desc": "Upscale suburban county with well-maintained homes that still benefit from expert professional repair."},
    {"name": "Passaic County",   "slug": "passaic-county-nj",   "towns": "Paterson, Clifton, Wayne, Pompton Lakes",              "desc": "Busy northern county with dense residential neighborhoods and older building stock requiring skilled upkeep."},
    {"name": "Camden County",    "slug": "camden-county-nj",    "towns": "Cherry Hill, Voorhees, Haddonfield, Camden",           "desc": "South Jersey's most populous county — rowhouses, ranches, and suburban homes served with care."},
    {"name": "Burlington County","slug": "burlington-county-nj","towns": "Moorestown, Medford, Evesham, Mount Holly",            "desc": "Large central county with historic towns and newer suburban developments throughout the Pinelands."},
    {"name": "Mercer County",    "slug": "mercer-county-nj",    "towns": "Trenton, Princeton, Hamilton, Lawrence",               "desc": "From Trenton's urban housing to Princeton's prestigious estates — expert repairs across the board."},
    {"name": "Atlantic County",  "slug": "atlantic-county-nj",  "towns": "Atlantic City, Egg Harbor, Galloway, Absecon",         "desc": "Shore and casino country with aging properties and high demand for reliable home repair services."},
    {"name": "Gloucester County","slug": "gloucester-county-nj","towns": "Woodbury, Deptford, Washington Twp, Glassboro",        "desc": "Growing suburb of Philadelphia with a range of home styles and steady demand for quality repairs."},
    {"name": "Cumberland County","slug": "cumberland-county-nj","towns": "Vineland, Bridgeton, Millville, Commercial Twp",       "desc": "South Jersey's rural county with older housing stock and unique repair needs we're equipped to handle."},
    {"name": "Cape May County",  "slug": "cape-may-county-nj",  "towns": "Cape May City, Wildwood, Ocean City, Avalon",          "desc": "Vacation homes, Victorian properties, and shore houses — seasonal and year-round maintenance covered."},
    {"name": "Warren County",    "slug": "warren-county-nj",    "towns": "Hackettstown, Washington, Phillipsburg, Belvidere",    "desc": "Rural-suburban mix with older farmhouses and modest residential neighborhoods throughout the valley."},
    {"name": "Sussex County",    "slug": "sussex-county-nj",    "towns": "Newton, Sparta, Vernon, Hardyston",                    "desc": "NJ's northernmost county — mountain-area homes with weather-related wear and older construction."},
    {"name": "Hunterdon County", "slug": "hunterdon-county-nj", "towns": "Flemington, Clinton, Lambertville, Raritan",           "desc": "Scenic rural county with historic farmhouses, horse properties, and charming older homes."},
    {"name": "Salem County",     "slug": "salem-county-nj",     "towns": "Salem City, Woodstown, Carneys Point, Penns Grove",   "desc": "South Jersey's smallest county — older housing requiring skilled, attentive home repair professionals."},
]

SERVICES = [
    {"name": "Chimney Repair",      "slug_prefix": "chimney-repair-in",      "icon": "fa-fire",                "parent": "new-jersey/chimney",   "parent_label": "Chimney & Masonry in NJ",  "cats_key": "chimney"},
    {"name": "Handyman Services",   "slug_prefix": "handyman-services-in",   "icon": "fa-screwdriver-wrench",  "parent": "new-jersey/handyman",  "parent_label": "Handyman Services in NJ",  "cats_key": "handyman"},
]

# Sub-services: (heading_suffix, body_text_template)
# {cn} = county name
SUB_SERVICES = {
    "Drywall Repair": [
        ("Drywall Hole Repair",
         "Small or large holes in drywall are one of the most common repair calls we get across {cn}. Whether it's from a doorknob, an anchor that pulled through, or accidental damage, we patch it cleanly and blend the surrounding texture so the repair is invisible."),
        ("Drywall Crack Repair",
         "Cracks in drywall — whether hairline or wider settlement cracks — are especially common in older {cn} homes. We reinforce the crack with mesh tape and joint compound, then feather it out and texture-match so it won't reappear."),
        ("Water Damage Drywall Repair",
         "Water-stained or bubbled drywall in {cn} homes often signals a past or ongoing leak. We assess the moisture source, dry the area, cut out the damaged section, replace it cleanly, and prime to prevent stain bleed-through before finishing."),
        ("Drywall Patch & Texture Matching",
         "Invisible patching requires matching the original texture — orange peel, knockdown, skip trowel, or smooth. We test-spray on a sample area first to dial in the match before applying the final finish across your {cn} home."),
        ("Ceiling Drywall Repair",
         "Ceiling repairs in {cn} are trickier than wall repairs — gravity works against you, and sanding overhead creates dust throughout the room. We use the right tools and protect your floors and furniture so the job is as clean as the result."),
        ("Drywall Joint & Tape Repair",
         "Bubbling or cracking tape along seams is a sign that the original installation used too little compound or the tape was applied incorrectly. We re-bed the tape, feather new compound, and finish it correctly so it holds for years."),
        ("Drywall Corner Bead Repair",
         "Dented or cracked corner beads are common in high-traffic areas of {cn} homes. We replace damaged metal or vinyl bead, apply compound, and sand to a sharp, clean corner that can handle daily contact."),
        ("Popcorn Ceiling Removal",
         "Popcorn ceilings in many {cn} homes were applied decades ago and are often outdated or damaged. We wet-scrape, smooth, and prime the ceiling — leaving a clean, modern surface ready for paint."),
        ("Drywall Skim Coat",
         "A skim coat gives walls a perfectly smooth, paint-ready surface — ideal for {cn} homeowners who want to eliminate texture or prep walls after wallpaper removal. We apply two thin coats of compound, sand between coats, and finish to a level-5 surface."),
        ("Drywall Mold Damage Repair",
         "Mold on drywall is common in {cn} bathrooms, basements, and laundry rooms. We safely remove affected drywall, treat the framing, and install new moisture-resistant board before finishing and painting."),
        ("Drywall Installation",
         "For additions, renovations, or full room replacement, we hang, tape, mud, and finish new drywall in {cn} homes to a smooth, paint-ready surface. We work clean, protect your floors, and haul away all scrap."),
    ],
    "Garage Door Repair": [
        ("Garage Door Spring Repair",
         "Broken torsion or extension springs are the most common garage door emergency in {cn}. A snapped spring leaves the door impossible to open safely. We carry springs for all door sizes and weights and replace them the same day, fully balanced and tensioned."),
        ("Garage Door Cable Repair",
         "Frayed or snapped lift cables are a safety hazard that can cause the door to drop unexpectedly. We replace both cables at once on {cn} garage doors — replacing only one creates uneven wear and early failure on the other side."),
        ("Garage Door Opener Repair",
         "If your opener hums but the door won't move, or responds inconsistently, we diagnose the issue and repair or replace the drive mechanism, gears, logic board, or motor unit. We service all major brands common in {cn} homes."),
        ("Garage Door Opener Installation",
         "Upgrading to a belt-drive or smart opener in your {cn} home dramatically reduces noise and adds smartphone control. We install, program, and set the travel limits and force settings — then walk you through the app setup."),
        ("Garage Door Panel Replacement",
         "A single dented or cracked panel doesn't always mean replacing the whole door. We source matching replacement panels for {cn} homeowners and install them so the repair blends with the existing sections."),
        ("Garage Door Track Repair & Alignment",
         "Bent or misaligned tracks cause the door to bind, scrape, or jump the rollers. We realign or replace the damaged section, check the entire track system, and test through several full cycles before leaving your {cn} home."),
        ("Garage Door Roller Replacement",
         "Worn, cracked, or broken rollers are often the cause of a noisy, jerky garage door. We replace all rollers at once with nylon or steel rollers rated for the door's weight, restoring smooth, quiet operation across {cn}."),
        ("Garage Door Sensor Repair",
         "Misaligned or dirty safety sensors prevent the door from closing and flash the opener light as a warning. We realign, clean, and test both sensors on your {cn} garage door until the door reverses consistently at a 2-inch obstruction."),
        ("Emergency Garage Door Repair",
         "A garage door stuck open is a security risk — especially overnight. We offer same-day emergency service across {cn} for broken springs, snapped cables, or any failure that leaves your door inoperable."),
        ("Garage Door Tune-Up & Maintenance",
         "An annual tune-up extends the life of every component. We lubricate rollers, hinges, springs, and tracks; test balance, auto-reverse, and force settings; and catch worn parts before they fail — keeping your {cn} garage door running quietly for years."),
        ("Garage Door Weatherstripping Replacement",
         "Cracked or missing weatherstripping lets drafts, water, pests, and road dust into your garage. We replace the bottom seal and side seals on your {cn} garage door — improving insulation and keeping the elements out year-round."),
        ("New Garage Door Installation",
         "Whether you're replacing an aging door or upgrading the curb appeal of your {cn} home, we install new single or double garage doors in steel, wood composite, aluminum, or carriage-house styles — with full hardware, spring, and opener setup."),
    ],
    "Painting": [
        ("Interior Wall Painting",
         "Interior painting in {cn} homes requires proper prep — patching nail holes, sanding, priming, and taping — before a single drop of paint goes on. We use low-VOC paints, protect all floors and furniture, and roll two full coats for even coverage."),
        ("Exterior House Painting",
         "Exterior painting in {cn} requires paint rated for NJ's humidity, temperature swings, and coastal salt air (especially in shore-adjacent areas). We power-wash, scrape, prime bare wood, and caulk all gaps before applying finish coats."),
        ("Ceiling Painting",
         "Ceiling paint is flat, has to cover evenly without lap marks, and needs the right nap thickness to avoid stippling. We mask walls, protect floors, and roll in a consistent pattern for a uniform, bright white finish across your {cn} home."),
        ("Trim & Baseboard Painting",
         "Clean, crisp trim makes a room look finished and professional. We sand, prime, and apply semi-gloss paint to all baseboards, door casings, and window trim in your {cn} home with tight, tape-free lines where trim meets wall."),
        ("Door & Window Frame Painting",
         "Interior and exterior door and window frames take daily wear and are the first thing to chip or fade. We sand to bare wood where needed, prime, and finish with two coats of durable semi-gloss to protect your {cn} home's most-touched surfaces."),
        ("Cabinet Painting & Refinishing",
         "Kitchen cabinet painting is the highest-impact, lowest-cost renovation available to {cn} homeowners. We de-grease, sand, prime with a bonding primer, and apply a durable cabinet-specific finish — leaving hardware-ready doors and boxes."),
        ("Deck & Fence Staining",
         "Untreated or faded wood decking and fencing in {cn}'s wet climate deteriorates quickly. We power-wash, let dry fully, sand rough spots, and apply a penetrating stain or solid deck paint — protecting the wood from moisture, UV, and foot traffic."),
        ("Paint Touch-Up & Blending",
         "Whether you have scuff marks, dings, or areas where a previous repair was patched, we match the existing color and sheen and blend the touch-up invisibly into the surrounding wall — eliminating the patchy look common after drywall repairs in {cn} homes."),
        ("Wallpaper Removal & Painting",
         "Removing wallpaper in {cn} homes — especially older properties with multiple layers — requires patience and the right tools to avoid tearing the drywall face paper. We steam or score-and-soak, skim-coat the wall, prime, and paint."),
        ("Garage Floor Epoxy Coating",
         "Epoxy-coated garage floors are easier to clean, more resistant to stains and impact, and transform the look of any garage in {cn}. We acid-etch or diamond-grind the slab, apply primer, and roll a two-part epoxy topcoat with broadcast flake if desired."),
    ],
    "Door Repair": [
        ("Door Frame Repair",
         "Damaged door frames — from forced entry, rot, or settling — compromise security and insulation. We sister new framing material alongside the damaged section, apply wood filler for minor damage, and refinish to match your {cn} home's existing trim."),
        ("Door Hinge Repair & Replacement",
         "Loose, stripped, or squeaking hinges are one of the most common door complaints in {cn} homes. We reset stripped screws with longer fasteners or epoxy fill, replace worn hinge plates, and adjust the hinge mortise for a perfectly hung door."),
        ("Door Lock Repair & Rekeying",
         "A faulty lock or one that requires force to turn is both frustrating and a security liability. We adjust, repair, or replace locksets and deadbolts on all door types in {cn} homes — and rekey existing locks when you've moved in or lost a key."),
        ("Sliding Door Repair",
         "Sliding glass or patio doors in {cn} homes often develop track buildup, worn rollers, or bent frames that make them difficult to open. We clean and lubricate or replace the roller assembly, realign the door in its track, and adjust the latch for smooth, secure operation."),
        ("French Door Repair",
         "French doors require careful alignment — both leaves must meet squarely at the astragal or they'll bind, rattle, or let drafts through. We adjust hinges, plane the door edge, replace the astragal, and restore weathertight closure across {cn} homes."),
        ("Screen Door Repair & Replacement",
         "Torn screen mesh, broken closers, or bent frames are common wear items on screen doors throughout {cn}. We re-screen on-site, replace the closer spring or pneumatic unit, and realign the door so it closes gently and latches every time."),
        ("Pocket Door Repair",
         "Pocket doors that jump the track or refuse to slide smoothly are a common frustration in older {cn} homes. We access the door through the existing opening, re-hang the rollers on the overhead track, and lubricate the system — no wall demolition required in most cases."),
        ("Door Weatherstripping Replacement",
         "Failed weatherstripping around exterior doors is the single most common source of drafts and energy loss in {cn} homes. We remove the old material, clean the door stop, and install compression-fit or adhesive-back weatherstripping that seals fully when the door is closed."),
        ("Exterior Door Installation",
         "A properly installed exterior door is plumb, level, and shimmed tightly in the rough opening before any trim is applied. We install prehung or slab exterior doors in {cn} homes with full flashing, caulking, and weatherstripping for an airtight, secure fit."),
        ("Interior Door Installation",
         "New interior doors change the feel of a room and improve privacy and noise control. We hang prehung or slab interior doors in {cn} homes, mortise the hinges and latch strike, and trim out the opening so the door swings cleanly and latches on the first try."),
        ("Bi-Fold Door Repair",
         "Bi-fold doors that sag, drag, or pop off the top track are fixable in most cases without replacement. We adjust the pivot pins, reset the top guide, and align the panels so they fold smoothly and stay on track in your {cn} home."),
        ("Storm Door Installation",
         "A quality storm door adds a layer of insulation and keeps insects out of your {cn} home's entryway. We install full-view or ventilating storm doors with proper shimming, screw-secured frames, and a correctly tensioned hydraulic closer."),
    ],
    "Chimney Repair": [
        ("Chimney Sweeping & Cleaning",
         "Annual chimney sweeping removes creosote buildup — the primary cause of chimney fires — from fireplaces across {cn}. We use rotary brushes and a HEPA vacuum to clean the flue from top to bottom, leaving no soot or debris in your home."),
        ("Chimney Tuckpointing",
         "Crumbling mortar joints are common in {cn}'s older brick chimneys, especially after freeze-thaw cycles. We grind out the deteriorated mortar and pack new mortar to the correct depth and profile, stopping water infiltration before it damages the flue liner."),
        ("Chimney Crown Repair & Sealing",
         "The chimney crown is the concrete cap that sheds water away from the flue opening. Cracked or spalled crowns in {cn} allow water to enter the masonry and accelerate deterioration. We repair cracks with crown-specific elastomeric sealant or pour a new crown for severe damage."),
        ("Chimney Cap Installation",
         "A stainless steel chimney cap prevents rain, animals, and debris from entering the flue while allowing exhaust to escape freely. We measure the flue tile dimensions and install the correctly sized cap on your {cn} chimney with stainless screws."),
        ("Chimney Flashing Repair",
         "Failed step flashing or counterflashing at the roof-chimney junction is one of the most common sources of attic and ceiling water damage in {cn} homes. We remove the old flashing, install new step and counterflashing, and seal with appropriate roofing caulk."),
        ("Firebox Repair",
         "Cracked or spalled firebrick in the firebox is a fire safety issue — damaged brick can allow combustion gases to reach the framing. We re-mortar loose joints with refractory mortar and replace spalled or cracked firebrick to restore a safe combustion chamber for your {cn} fireplace."),
        ("Chimney Liner Installation",
         "A properly sized and installed flue liner is required by code in NJ and ensures combustion gases exhaust safely. We install stainless steel liner systems in {cn} chimneys for oil, gas, and wood appliances — including insulation wrap for proper draft."),
        ("Chimney Waterproofing",
         "Unpainted or unsealed masonry in {cn}'s wet climate absorbs water through the brick face, causing spalling and freeze-thaw damage over time. We apply penetrating, vapor-permeable masonry waterproofer to the entire chimney exterior — blocking water entry while allowing moisture to escape from inside."),
        ("Chimney Draft Repair",
         "Smoke backing into the room when you light a fire signals a draft problem — often a blockage, an undersized flue, or negative house pressure. We diagnose the cause and correct it in {cn} homes whether the fix is a cap change, damper repair, or air-sealing the attic."),
        ("Fireplace Damper Repair",
         "A stuck or missing fireplace damper wastes energy year-round by allowing conditioned air to escape up the flue. We repair throat dampers or install top-mount dampers on {cn} fireplaces — sealing the flue when not in use and providing reliable control when firing."),
        ("Brick & Mortar Restoration",
         "Spalling brick faces and deteriorated mortar are common across {cn}'s older housing stock. We clean, tuckpoint, and apply consolidant to stabilize aging masonry — restoring the chimney's structural integrity and preventing further weathering."),
        ("Chimney Inspection",
         "A Level 1 chimney inspection is recommended annually and before each heating season for {cn} homeowners. We inspect the accessible interior and exterior of the flue and firebox, checking for obstructions, deterioration, and code compliance, and provide a written report."),
    ],
    "Electrical Repair": [
        ("Electrical Outlet Repair & Replacement",
         "Dead or sparking outlets are one of the most common light electrical calls in {cn} homes. We diagnose whether the fault is a tripped GFCI upstream, a loose wire connection, or a failed device — and repair or replace the outlet correctly."),
        ("Light Switch Replacement",
         "Switches that click without turning on, feel warm, or produce a slight buzz are failing and should be replaced. We swap single-pole, 3-way, and timer switches in {cn} homes safely, matching the existing wiring configuration every time."),
        ("Ceiling Fan Installation",
         "Ceiling fan installation in {cn} homes requires a fan-rated box in the ceiling, which we install or verify before mounting the bracket and fan. We connect and tuck all wiring, hang the blades, and balance the unit so it runs smoothly at all speeds."),
        ("Light Fixture Installation",
         "Replacing a fixture — from a simple flush-mount to a heavy chandelier — requires matching the wiring and ensuring the junction box can support the weight. We install all fixture types in {cn} homes, handle the wiring correctly, and clean up when done."),
        ("GFCI Outlet Installation",
         "GFCI protection is required by NJ code in kitchens, bathrooms, garages, and outdoor areas. We install GFCI outlets in the correct locations throughout your {cn} home and test each one for proper trip and reset function before we leave."),
        ("Dimmer Switch Installation",
         "Dimmer switches must be matched to the load — incandescent, CFL, or LED — or they'll flicker, hum, or fail early. We install dimmer switches in {cn} homes using the correct dimmer type for your bulbs and set the low-trim to eliminate flicker."),
        ("Recessed Lighting Installation",
         "Adding recessed cans to a {cn} home requires the right IC-rated fixtures, proper insulation contact clearance, and careful drilling to avoid framing. We install, wire, and trim recessed lighting in new or existing ceilings — including the switch and dimmer setup."),
        ("Outdoor Lighting Installation",
         "Outdoor fixtures in {cn} must be rated for wet or damp locations and properly sealed against NJ's precipitation. We install post lights, wall sconces, floodlights, and step lights — running new wire from the nearest junction box when needed."),
        ("USB Outlet Installation",
         "USB-A and USB-C charging outlets are a quick, popular upgrade in {cn} homes. We replace a standard outlet with a USB combo device, ensuring the outlet is on a circuit with adequate amperage for both the USB ports and the standard plugs."),
        ("Smart Switch Installation",
         "Smart switches in {cn} homes require a neutral wire — which most homes have, but some older wiring does not. We verify compatibility, install the smart switch, connect it to your WiFi network, and test voice and app control before leaving."),
        ("Smoke & Carbon Monoxide Detector Installation",
         "NJ law requires working smoke and CO detectors on every level of the home. We install interconnected hardwired detectors in {cn} homes — ensuring proper placement per NJ code, correct wiring of the interconnect, and a full test of each unit."),
        ("TV & Cable Outlet Installation",
         "Mounting a TV without a wall outlet behind it means unsightly cords running down the wall. We install an in-wall power and HDMI kit in your {cn} home — routing cables behind the drywall so the finished result looks like it was planned during construction."),
    ],
    "Plumbing Repair": [
        ("Faucet Repair & Replacement",
         "A dripping faucet in a {cn} home wastes thousands of gallons per year and signals a worn cartridge, O-ring, or seat. We repair or replace the cartridge on most faucets — and if the valve body is corroded, we install a new fixture of your choice."),
        ("Leaky Pipe Repair",
         "Leaks at joints, supply line fittings, and shutoff valves are common in {cn}'s older housing stock where original copper has corroded or galvanized pipe has rusted. We cut out the damaged section and solder or press a new fitting into place — stopping the leak permanently."),
        ("Toilet Repair & Replacement",
         "A running toilet wastes up to 200 gallons per day. Whether it's a worn flapper, failed fill valve, or cracked tank, we diagnose and repair the issue in {cn} homes on the first visit. When the toilet is beyond repair, we supply and install a new unit."),
        ("Drain Cleaning & Unclogging",
         "Slow or completely blocked drains in {cn} kitchens and bathrooms are typically caused by grease buildup, hair, or soap scum. We clear the blockage with a hand snake or power auger and flush the drain — without damaging the pipe or the drain finish."),
        ("Garbage Disposal Repair & Installation",
         "A humming garbage disposal that won't spin usually has a jammed impeller — fixable in minutes. A completely dead unit typically needs replacement. We repair or replace disposals in {cn} kitchens and reconnect the drain plumbing correctly."),
        ("Showerhead Replacement",
         "A low-flow or clogged showerhead is an easy fix that makes a big difference in daily comfort. We replace showerheads in {cn} homes — including removing mineral-locked old heads and applying thread tape and sealant correctly to prevent drips."),
        ("Under-Sink Plumbing Repair",
         "Supply line leaks, drain P-trap clogs, and corroded shut-off valves under kitchen and bathroom sinks are among the most common plumbing calls in {cn}. We replace supply lines, reset or replace the P-trap, and install new angle stops when valves fail to close fully."),
        ("Kitchen Faucet Installation",
         "Installing a kitchen faucet in a {cn} home involves removing the old fixture, cleaning the deck surface, installing the new faucet body, connecting supply lines, and testing for leaks at every connection. We handle all three-hole, single-hole, and pull-down configurations."),
        ("Water Valve Replacement",
         "Shut-off valves that won't fully close — common in {cn} homes with older plumbing — need to be replaced before they fail completely and leave you without a way to stop a leak. We replace ball valves, gate valves, and angle stops throughout your home."),
        ("Toilet Flapper & Fill Valve Replacement",
         "The flapper and fill valve are the two components that wear out in almost every toilet over time. Replacing both at once in your {cn} home takes about 30 minutes and stops the phantom flushing and running water that signal they've failed."),
        ("Bathtub Drain Repair",
         "Slow tub drains in {cn} homes are typically caused by hair clogs in the crosshair or stopper mechanism. We remove the drain cover, clear the blockage, and test drainage rate — and replace the drain stopper or overflow plate if the mechanism is corroded or broken."),
        ("P-Trap Replacement",
         "Leaking or corroded P-traps under sinks and tubs allow sewer gas into the home and drip onto cabinet shelves. We replace chrome, PVC, or ABS P-traps in {cn} homes with correctly sized fittings, checking for level and testing all joints before reassembling the cabinet."),
    ],
    "Handyman Services": [
        ("Drywall Repair & Patching",
         "Holes, cracks, water damage, and texture matching are among the most common handyman calls in {cn}. We patch drywall invisibly — blending the repair with your existing wall texture so you'd never know anything happened."),
        ("Interior Painting",
         "Interior painting in {cn} starts with proper prep: patching, sanding, priming, and taping before a single drop of paint goes on. We use low-VOC paints, protect all floors and furniture, and apply two full coats for lasting, even coverage."),
        ("Door Repair & Installation",
         "Sticking doors, broken hinges, damaged frames, and squeaking hardware are everyday handyman repairs in {cn} homes. We adjust, repair, or replace interior and exterior doors — leaving every door opening, closing, and latching cleanly."),
        ("Furniture Assembly",
         "Flat-pack furniture from IKEA, Wayfair, or Amazon assembled correctly in your {cn} home — beds, desks, wardrobes, shelving, and TV stands. We bring the tools and handle pieces of any size or complexity."),
        ("TV Mounting & Installation",
         "We mount TVs on all wall types in {cn} homes — drywall over studs, concrete, tile, and brick. We locate studs or use correct toggle anchors, level the mount, and route cables in-wall when requested."),
        ("Light Electrical Repairs",
         "Dead outlets, flickering lights, or switches that need replacing are routine handyman fixes throughout {cn}. We replace outlets, switches, ceiling fans, and light fixtures — all code-compliant work done safely."),
        ("Light Plumbing Repairs",
         "Dripping faucets, running toilets, slow drains, and under-sink leaks are common calls across {cn} homes. We repair or replace faucets, flappers, P-traps, showerheads, and garbage disposals on the same visit."),
        ("Shelf & Storage Installation",
         "Floating shelves, wall-mounted storage units, and closet organizers installed level and anchored to studs in {cn} homes. We locate framing, use correct anchors for the load, and leave shelves that are genuinely horizontal and secure."),
        ("Weatherstripping & Door Seals",
         "Drafty exterior doors are one of the biggest sources of energy loss in {cn} homes. We replace door weatherstripping, bottom seals, and threshold gaskets — stopping drafts and reducing heating and cooling costs."),
        ("Caulking & Sealing",
         "Failed caulk around bathtubs, sinks, windows, and exterior trim lets water infiltrate and causes mold, rot, and energy loss. We remove old caulk completely, clean the substrate, and apply fresh sealant with clean tooled lines throughout your {cn} home."),
        ("Tile Repair & Grout",
         "Cracked or loose tiles and failed grout in bathrooms and kitchens are common in older {cn} homes. We replace individual tiles, re-grout deteriorated joints, and re-caulk tub and shower transitions to restore a clean, waterproof surface."),
        ("Handyman Home Inspection",
         "Not sure what needs fixing? We'll walk through your {cn} home room by room, identify deferred maintenance items, prioritize them by urgency, and give you a written list with honest cost estimates — so you can plan repairs before small problems become expensive ones."),
    ],
    "Furniture Assembly": [
        ("IKEA Furniture Assembly",
         "IKEA flat-pack furniture requires careful alignment of cam locks, dowels, and confirmat screws — and the instructions leave room for costly errors. We assemble all IKEA product lines in {cn} homes correctly the first time, including pre-drilling for wall-mounted anti-tip brackets."),
        ("Wayfair Furniture Assembly",
         "Wayfair ships from dozens of manufacturers, each with different fastener systems and instruction quality. We assemble Wayfair furniture across all categories in {cn} homes — beds, sofas, dining sets, desks, and storage units — regardless of the instruction quality."),
        ("Amazon Furniture Assembly",
         "Amazon furniture ranges from simple bookshelves to complex storage systems. We unbox, sort hardware, and assemble Amazon furniture orders in {cn} homes — handling missing hardware issues and construction quirks that trip up DIY assemblers."),
        ("Bed Frame Assembly",
         "Bed frame assembly in {cn} homes — from simple metal frames to complex upholstered platforms with built-in storage — requires patience and the right tools. We assemble all frame types, attach the headboard, and verify the frame is square and stable before leaving."),
        ("Desk & Office Furniture Assembly",
         "Home office setups in {cn} often involve L-shaped desks, standing desk converters, monitor arms, and cable management systems that require precise assembly. We build desks correctly so drawers slide smoothly, the surface is level, and adjustable components move freely."),
        ("Wardrobe & Closet Assembly",
         "Large wardrobe systems — PAX, KALLAX, or custom closet kits — require plumb walls and level floors to assemble correctly. In {cn} homes where walls aren't always perfectly straight, we shim and adjust during assembly so doors hang true and drawers slide without binding."),
        ("Bookshelf & Storage Assembly",
         "From small floating shelves to full-wall storage units, we assemble and — where required — anchor shelving to the wall stud for safety. This is especially important in {cn} homes with small children, where tip-over hazards are a serious concern."),
        ("TV Stand & Entertainment Center Assembly",
         "TV stands and entertainment centers in {cn} homes require precise assembly so the surface is level and the cable management cutouts align correctly. We assemble the unit, route cables cleanly through the designated channels, and position it where you want it."),
        ("TV Mounting & Installation",
         "We mount TVs on all wall types in {cn} homes — drywall over studs, concrete, tile, and brick. We locate studs or use toggle anchors for the correct load, level the mount, route cables in-wall where requested, and connect all sources before leaving."),
        ("Dining Table & Chair Assembly",
         "Dining table assembly — especially extension tables with leaf mechanisms — requires careful alignment so the surface is flat and the leaf inserts and removes smoothly. We assemble dining tables and chairs in {cn} homes and verify everything is level and tight before leaving."),
        ("Wall Shelving Installation",
         "Floating shelves and wall-mounted storage in {cn} homes must hit studs or use the correct drywall anchors for the anticipated load. We locate studs with a stud finder, level and mark the bracket positions, and install shelves that are genuinely horizontal and rated for the weight."),
        ("Exercise Equipment Assembly",
         "Treadmills, bikes, weight benches, and squat racks arrive in heavy, awkward boxes with complex assembly. We assemble fitness equipment in {cn} homes and garages — verifying that all pivot points, adjustment pins, and cable systems are correctly installed and safe before the first use."),
    ],
}

PIN_SVG = '<svg viewBox="0 0 24 30" fill="none" aria-hidden="true"><path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 18 12 18S24 21 24 12C24 5.4 18.6 0 12 0z" fill="#FF6B35"/><circle cx="12" cy="12" r="4.5" fill="white"/></svg>'

GFONTS = "https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"
FA     = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"

# ─── Service bubble grid (same widget as /new-jersey/<service>/ hub pages) ──────
# Reuses services_data.py so the county-page service list always matches the
# state-level hub and every bubble links to that service's existing, already-
# SEO-optimized /new-jersey/<slug>/ page — no per-county leaf pages to maintain.

def _build_cats(sd_cats, svc_full):
    lookup = build_service_lookup(svc_full)
    return [(cat_name, cat_icon, [(lookup[s][0], lookup[s][1], s) for s in slugs if s in lookup])
            for cat_name, cat_icon, slugs in sd_cats]

CHIMNEY_CATS_BUILT  = _build_cats(SD_CHIMNEY_CATS,  CHIMNEY_SERVICES_FULL)
HANDYMAN_CATS_BUILT = _build_cats(SD_HANDYMAN_CATS, HANDYMAN_SERVICES_FULL)
CATS_BY_KEY = {"chimney": CHIMNEY_CATS_BUILT, "handyman": HANDYMAN_CATS_BUILT}

BUBBLE_CSS = """
<style id="bubble-styles">
@keyframes bubble-float {
  0%,100% { transform: translateY(0px); }
  50%      { transform: translateY(-6px); }
}
.svc-bubble {
  display: inline-flex; align-items: center; gap: 8px;
  background: #fff; border: 2px solid #e8edf5; border-radius: 100px;
  padding: 10px 18px 10px 13px; font-size: 13.5px; font-weight: 500;
  color: #1e2d5a; cursor: pointer; user-select: none;
  animation: bubble-float var(--dur,3.8s) ease-in-out var(--delay,0s) infinite;
  transition: transform .28s cubic-bezier(.34,1.56,.64,1),
              opacity .2s ease, border-color .15s ease,
              box-shadow .15s ease, background .15s ease;
  will-change: transform, opacity;
}
.svc-bubble:hover {
  border-color: #FF6B35; background: #fff7f4;
  box-shadow: 0 8px 24px rgba(255,107,53,.18);
  animation-play-state: paused;
  transform: translateY(-4px) scale(1.05) !important;
}
.svc-bubble.b-hide {
  transform: scale(0) !important; opacity: 0 !important;
  pointer-events: none; animation: none !important;
}
.svc-bubble .b-icon { font-size: 11px; color: #FF6B35; flex-shrink: 0; }
.svc-category.c-hide { display: none; }
.bubbles-row { display: flex; flex-wrap: wrap; gap: 10px; }
.cat-hdr { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.cat-hdr-icon {
  width: 30px; height: 30px; background: rgba(255,107,53,.1);
  border-radius: 9px; display: flex; align-items: center;
  justify-content: center; flex-shrink: 0;
}
.cat-hdr-icon i { color: #FF6B35; font-size: 12px; }
.cat-hdr-label {
  font-size: 11px; font-weight: 800; color: #0d1b4b;
  text-transform: uppercase; letter-spacing: .1em; white-space: nowrap;
}
.cat-hdr-line { flex: 1; height: 1px; background: #eef1f7; }
.srch-wrap { position: relative; display: flex; align-items: center; }
.srch-icon { position: absolute; left: 17px; color: #94a3b8; font-size: 15px; pointer-events: none; }
.srch-input {
  width: 100%; padding: 15px 50px 15px 46px;
  border: 2px solid #e2e8f0; border-radius: 18px;
  font-size: 15px; font-weight: 500; color: #0d1b4b;
  font-family: Inter, sans-serif; outline: none; background: #fff;
  transition: border-color .2s, box-shadow .2s;
}
.srch-input:focus { border-color: #FF6B35; box-shadow: 0 0 0 4px rgba(255,107,53,.1); }
.srch-input::placeholder { color: #94a3b8; }
.srch-clear {
  position: absolute; right: 16px; width: 26px; height: 26px;
  background: #f1f5f9; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #64748b; font-size: 11px; cursor: pointer;
  opacity: 0; pointer-events: none; transition: opacity .15s, background .15s;
}
.srch-clear.show { opacity: 1; pointer-events: all; }
.srch-clear:hover { background: #FF6B35; color: #fff; }
.srch-hint { text-align: center; font-size: 13px; color: #94a3b8; margin-top: 10px; min-height: 18px; }
.srch-none { text-align: center; font-size: 15px; color: #64748b; padding: 40px 0; display: none; }
.srch-none button { color: #FF6B35; font-weight: 600; background: none; border: none; cursor: pointer; margin-left: 4px; }
</style>"""

BUBBLE_JS = """
<script id="bubble-search">
(function() {
  var inp  = document.getElementById('srch');
  var clr  = document.getElementById('srch-clr');
  var hint = document.getElementById('srch-hint');
  var none = document.getElementById('srch-none');
  var bubbles = document.querySelectorAll('.svc-bubble');
  var cats    = document.querySelectorAll('.svc-category');
  if (!inp) return;
  function run(q) {
    q = q.toLowerCase().trim();
    var shown = 0;
    bubbles.forEach(function(b) {
      var match = !q || b.dataset.s.includes(q);
      b.classList.toggle('b-hide', !match);
      if (match) shown++;
    });
    cats.forEach(function(c) {
      var any = Array.from(c.querySelectorAll('.svc-bubble')).some(function(b) { return !b.classList.contains('b-hide'); });
      c.classList.toggle('c-hide', !any);
    });
    clr.classList.toggle('show', q.length > 0);
    hint.textContent = q ? (shown + ' service' + (shown !== 1 ? 's' : '') + ' found') : '';
    none.style.display = (q && shown === 0) ? 'block' : 'none';
  }
  inp.addEventListener('input', function() { run(inp.value); });
  clr.addEventListener('click', function() { inp.value = ''; run(''); inp.focus(); });
  document.getElementById('srch-none-clr').addEventListener('click', function() { inp.value = ''; run(''); inp.focus(); });
})();
</script>"""

BUBBLE_DURATIONS = [3.6, 4.1, 3.9, 4.4, 3.7, 4.2, 3.8, 4.5]
BUBBLE_DELAYS    = [0, 0.4, 0.8, 1.2, 0.2, 0.6, 1.0, 1.4]

def bubble_grid_html(cats, location_name, loc_url="new-jersey", href_prefix="../../"):
    """Searchable service bubble grid, same widget as /new-jersey/<service>/, but
    linking back up to those state-level pages instead of duplicating them."""
    total = sum(len(items) for _, _, items in cats)
    idx = 0
    cats_html = ""
    for cat_name, cat_icon, items in cats:
        bubbles_html = ""
        for icon, name, slug in items:
            dur   = BUBBLE_DURATIONS[idx % len(BUBBLE_DURATIONS)]
            delay = BUBBLE_DELAYS[idx % len(BUBBLE_DELAYS)]
            s_key = name.lower().replace("&amp;", "and").replace("/", " ").replace("(", "").replace(")", "")
            href  = f'{href_prefix}{loc_url}/{slug}/'
            bubbles_html += f"""
                    <a class="svc-bubble" href="{href}" data-s="{s_key}" style="--dur:{dur}s;--delay:{delay}s"><i class="fas {icon} b-icon"></i><span>{name}</span></a>"""
            idx += 1
        cats_html += f"""
            <div class="svc-category">
                <div class="cat-hdr">
                    <div class="cat-hdr-icon"><i class="fas {cat_icon}"></i></div>
                    <span class="cat-hdr-label">{cat_name}</span>
                    <div class="cat-hdr-line"></div>
                </div>
                <div class="bubbles-row">{bubbles_html}
                </div>
            </div>"""

    return f"""
    <section class="sp-work-section services">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Services</span>
                <h2 class="section-title">Every Service We <span class="text-accent">Offer in {location_name}</span></h2>
                <p class="section-desc">All {total} services — search to find yours instantly. Same-day available, free estimates.</p>
            </div>

            <div class="max-w-[580px] mx-auto mb-12 reveal">
                <div class="srch-wrap">
                    <i class="fas fa-search srch-icon"></i>
                    <input id="srch" type="text" class="srch-input" placeholder="Search services…" autocomplete="off" spellcheck="false">
                    <div id="srch-clr" class="srch-clear" role="button" aria-label="Clear search"><i class="fas fa-times"></i></div>
                </div>
                <p id="srch-hint" class="srch-hint"></p>
            </div>

            <div class="flex flex-col gap-10 max-w-[960px] mx-auto">{cats_html}
            </div>
            <div id="srch-none" class="srch-none">No services match your search.<button id="srch-none-clr">Clear search</button></div>
        </div>
    </section>"""


COMMON_HEAD = f"""\
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="{GFONTS}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{GFONTS}"></noscript>
    <link rel="preload" href="{FA}" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="{FA}"></noscript>"""


# ─── Shared templates ──────────────────────────────────────────────────────────

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
                <li class="nav-dropdown">
                    <a href="{prefix}locations/" class="nav-link flex items-center gap-1.5"{loc_active}>Locations <i class="fas fa-chevron-down text-[10px] opacity-50 mt-px"></i></a>
                    <div class="nav-dropdown-menu">
                        <a href="{prefix}new-jersey/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> New Jersey</a>
                        <a href="{prefix}cleveland-ohio/" class="nav-dropdown-item"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                        <div class="nav-dropdown-divider"></div>
                        <a href="{prefix}locations/" class="nav-dropdown-item" style="color:rgba(255,255,255,.45)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
                    </div>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="tel:+15513504951" class="nav-phone"><i class="fas fa-phone"></i><span>(551) 350-4951</span></a>
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
            <li>
                <span class="mobile-loc-label">Locations</span>
                <a href="{prefix}new-jersey/"     class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> New Jersey</a>
                <a href="{prefix}cleveland-ohio/" class="mobile-link mobile-loc-sub"><i class="fas fa-location-dot"></i> Cleveland, Ohio</a>
                <a href="{prefix}locations/"      class="mobile-link mobile-loc-sub" style="color:rgba(255,255,255,.4)"><i class="fas fa-map-marker-alt"></i> All Locations</a>
            </li>
        </ul>
        <a href="tel:+15513504951" class="mobile-phone"><i class="fas fa-phone"></i>(551) 350-4951</a>
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
                    <li><a href="{p}chimney-masonry-new-jersey/">Chimney &amp; Masonry</a></li>
                    <li><a href="{p}handyman-services-new-jersey/">Handyman Services</a></li>
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
                    <li><i class="fas fa-phone"></i><a href="tel:+15513504951">(551) 350-4951</a></li>
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
    towns_display = county["towns"].replace(", ", " · ")
    lines = [
        f'                <div class="loc-card">',
        f'                    <div class="loc-card__header">',
        f'                        <div class="loc-pin-icon">{PIN_SVG}</div>',
        f'                        <div>',
        f'                            <h2 class="loc-card__name">{county["name"]}</h2>',
        f'                            <p class="loc-card__towns">{towns_display}</p>',
        f'                        </div>',
        f'                    </div>',
        f'                    <p class="loc-card__desc">{county["desc"]}</p>',
        f'                    <div class="loc-card__divider"></div>',
        f'                    <div class="loc-services-grid">',
    ]
    for svc in SERVICES:
        url = f'{svc["slug_prefix"]}-{slug}/'   # same-dir: locations/index.html → locations/slug/
        lines.append(f'                        <a href="{url}" class="loc-svc-btn"><i class="fas {svc["icon"]}"></i> {svc["name"]}</a>')
    lines += ['                    </div>', '                </div>']
    return "\n".join(lines)


def build_locations_page():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
    <meta name="description" content="The Fix Wizard offers expert chimney repair, masonry, and handyman services across New Jersey (all 21 counties) and the greater Cleveland, Ohio area. Licensed & insured. Same-day available. Free estimates.">
    <title>Service Locations — New Jersey &amp; Cleveland, Ohio | The Fix Wizard</title>
    <link rel="stylesheet" href="../css/tw.css">
    <link rel="stylesheet" href="../css/custom.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "HomeAndConstructionBusiness",
      "name": "The Fix Wizard",
      "description": "Expert chimney repair, masonry, and handyman services across New Jersey and the greater Cleveland, Ohio area.",
      "url": "https://thefixwizard.com/locations/",
      "telephone": "(551) 350-4951",
      "areaServed": [
        {{"@type": "State", "name": "New Jersey"}},
        {{"@type": "City", "name": "Cleveland", "containedInPlace": {{"@type": "State", "name": "Ohio"}}}}
      ]
    }}
    </script>
</head>
<body>

{navbar_html(1, active="locations")}

    <!-- HERO -->
    <section class="hero relative flex items-center overflow-hidden min-h-screen pt-[var(--nav-h)] rounded-b-[56px]">
        <div class="max-w-site mx-auto px-6 relative z-[2] w-full">
            <div class="grid grid-cols-1 tab:grid-cols-[1fr_420px] gap-14 items-center pt-12 pb-20 md:pt-8 md:pb-12">

                <!-- LEFT -->
                <div class="flex flex-col items-center tab:items-start text-center tab:text-left">
                    <div class="inline-flex items-center gap-2 bg-orange/[.14] border border-orange/30 text-orange-light px-4 py-1.5 rounded-full text-[13px] font-semibold mb-7 tracking-wide">
                        <i class="fas fa-map-marker-alt text-orange text-[11px]"></i>
                        <span>2 Service Locations &amp; Growing</span>
                    </div>
                    <h1 class="font-cinzel text-[clamp(32px,5vw,64px)] font-black leading-[1.1] tracking-tight text-white mb-6">
                        Chimney &amp; Handyman<br>
                        <span class="text-orange">Services <span class="lightning-word">Near You</span></span>
                    </h1>
                    <p class="text-[18px] text-white/65 leading-[1.75] mb-6 max-w-[560px]">
                        The Fix Wizard brings licensed chimney repair, masonry restoration, and handyman services to homeowners across <strong class="text-white/90">New Jersey</strong> and <strong class="text-white/90">Cleveland, Ohio</strong>. Same-day available. Free estimates. No obligation.
                    </p>
                    <div class="flex items-center gap-3 mb-8 flex-wrap justify-center tab:justify-start">
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-location-dot text-orange text-[12px]"></i> New Jersey — All 21 Counties
                        </div>
                        <div class="flex items-center gap-2 bg-white/[.07] border border-white/[.1] rounded-full px-4 py-2 text-[13px] font-semibold text-white/80">
                            <i class="fas fa-location-dot text-orange text-[12px]"></i> Cleveland, Ohio
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
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="nj_counties">0</span></div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">NJ Counties</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="cle_areas">0</span></div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">CLE Areas</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="projects">0</span>+</div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Jobs Done</div>
                        </div>
                        <div class="w-px h-10 bg-white/12 hidden tab:block"></div>
                        <div class="text-left">
                            <div class="text-[28px] font-black text-orange leading-none mb-1"><span class="counter" data-stat="specialties">0</span></div>
                            <div class="text-[12px] text-white/50 font-medium tracking-wider">Specialties</div>
                        </div>
                    </div>
                </div>

                <!-- RIGHT -->
                <div class="flex items-center justify-center tab:justify-end">
                    <div class="w-full max-w-[520px] bg-white/[.07] backdrop-blur-xl border border-white/[.13] rounded-xl2 p-8 flex flex-col gap-6">
                        <div class="flex items-center gap-3.5">
                            <div class="w-[52px] h-[52px] shrink-0 bg-orange rounded-md2 flex items-center justify-center text-[22px] text-white">
                                <i class="fas fa-map-location-dot"></i>
                            </div>
                            <div>
                                <div class="text-[16px] font-semibold text-white leading-tight mb-1">Choose Your Location</div>
                                <p class="text-[13px] text-white/50">Same-day service · Free estimates</p>
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

    <!-- LOCATION SHOWCASE -->
    <section class="py-20" style="background:#f7f8fc;background-image:radial-gradient(circle,rgba(13,27,75,.07) 1px,transparent 1px);background-size:28px 28px;">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Where We Work</span>
                <h2 class="section-title">Two Locations, <span class="text-accent">One Standard</span></h2>
                <p class="section-desc">Whether you need a chimney swept in Bergen County or a drywall patch in Lakewood, Ohio — the same licensed technicians, transparent pricing, and satisfaction guarantee follow you everywhere.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-[1000px] mx-auto">

                <!-- NJ Card -->
                <div class="group bg-white rounded-card border border-slate-200 overflow-hidden flex flex-col transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.18)] hover:border-transparent reveal">
                    <div class="h-3 bg-gradient-to-r from-orange-dark via-orange to-orange-light"></div>
                    <div class="p-8 flex flex-col gap-5 flex-1">
                        <div class="flex items-center gap-4">
                            <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center shrink-0">
                                <i class="fas fa-location-dot text-orange text-[24px]"></i>
                            </div>
                            <div>
                                <h2 class="text-[22px] font-bold text-navy-900 leading-tight">New Jersey</h2>
                                <p class="text-[13px] text-slate-500 mt-0.5">All 21 Counties · Statewide Coverage</p>
                            </div>
                        </div>
                        <p class="text-[15px] text-slate-600 leading-relaxed">From the brownstones of <strong class="text-navy-900">Hudson County</strong> to the Victorian shore homes of <strong class="text-navy-900">Cape May</strong>, New Jersey's diverse housing stock demands skilled, licensed repair specialists. The Fix Wizard serves every NJ county — chimney sweeping and tuckpointing in <strong class="text-navy-900">Bergen, Morris, and Essex</strong>; handyman services throughout <strong class="text-navy-900">Monmouth, Ocean, and Middlesex</strong>. Same-day dispatching statewide.</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Chimney Repair NJ</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Handyman NJ</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Tuckpointing NJ</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">All 21 Counties</span>
                        </div>
                        <ul class="flex flex-col gap-2 text-[14px] text-slate-600">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Bergen, Essex, Middlesex, Monmouth, Morris</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Hudson, Union, Ocean, Somerset, Passaic</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Camden, Burlington, Mercer, Atlantic + 7 more</li>
                        </ul>
                        <a href="../new-jersey/" class="inline-flex items-center gap-2 text-[14px] font-bold text-orange hover:text-orange-dark transition-colors mt-auto">
                            View New Jersey Services <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Cleveland Card -->
                <div class="group bg-white rounded-card border border-slate-200 overflow-hidden flex flex-col transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_60px_rgba(13,27,75,.18)] hover:border-transparent reveal">
                    <div class="h-3 bg-gradient-to-r from-orange-dark via-orange to-orange-light"></div>
                    <div class="p-8 flex flex-col gap-5 flex-1">
                        <div class="flex items-center gap-4">
                            <div class="w-14 h-14 bg-orange/10 rounded-xl flex items-center justify-center shrink-0">
                                <i class="fas fa-location-dot text-orange text-[24px]"></i>
                            </div>
                            <div>
                                <h2 class="text-[22px] font-bold text-navy-900 leading-tight">Cleveland, Ohio</h2>
                                <p class="text-[13px] text-slate-500 mt-0.5">Greater Cleveland · 20 Suburbs Covered</p>
                            </div>
                        </div>
                        <p class="text-[15px] text-slate-600 leading-relaxed">Cleveland's harsh lake-effect winters and century-old housing stock create relentless demand for expert chimney and home repair. The Fix Wizard serves the greater Cleveland area — chimney repair and masonry in <strong class="text-navy-900">Lakewood, Cleveland Heights, and Shaker Heights</strong>; handyman services in <strong class="text-navy-900">Parma, Strongsville, Westlake, and Beachwood</strong>. Freeze-thaw specialists on every job.</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Chimney Repair Cleveland</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Handyman Cleveland</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Tuckpointing Ohio</span>
                            <span class="text-[12px] bg-orange/[.08] text-orange font-semibold px-3 py-1 rounded-full">Greater Cleveland</span>
                        </div>
                        <ul class="flex flex-col gap-2 text-[14px] text-slate-600">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Cleveland, Lakewood, Cleveland Heights, Parma</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Strongsville, Westlake, Beachwood, Solon</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-orange text-[10px]"></i> Shaker Heights, Rocky River, Mentor + 9 more</li>
                        </ul>
                        <a href="../cleveland-ohio/" class="inline-flex items-center gap-2 text-[14px] font-bold text-orange hover:text-orange-dark transition-colors mt-auto">
                            View Cleveland Services <i class="fas fa-arrow-right transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>Chimney Repair or Handyman Services — Wherever You Are</h2>
                <p>Free estimates in New Jersey &amp; Cleveland. Licensed &amp; insured. Same-day available.</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15513504951" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Free Quote</a>
            </div>
        </div>
    </section>

{footer_html(1)}

    <script type="module" src="../js/service-page.js"></script>
</body>
</html>"""

    out_dir = os.path.join(ROOT, "locations")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    print("  ✓  locations/index.html")


# ─── 2. SERVICE AREA PAGES ──────────────────────────────────────────────────────

def sub_service_sections(svc_name, county_name):
    """Return HTML for all H3 sub-service sections for this service × county."""
    subs = SUB_SERVICES.get(svc_name, [])
    blocks = []
    for (heading_suffix, body_template) in subs:
        body = body_template.replace("{cn}", county_name)
        heading = f"{heading_suffix} in {county_name}, NJ"
        blocks.append(f"""\
                    <h3>{heading}</h3>
                    <p>{body}</p>""")
    return "\n\n".join(blocks)


def area_faqs(cats_key, cn, towns):
    if cats_key == "chimney":
        return [
            (f"How often should I have my chimney swept in {cn}?",
             "Most chimney safety organizations recommend annual sweeping and inspection before each heating season. Homes that burn wood regularly may need sweeping twice a year, and even gas appliances need an annual check."),
            ("What is tuckpointing and do I need it?",
             f"Tuckpointing is grinding out deteriorated mortar joints and packing in fresh mortar. If you see gaps, crumbling, or missing mortar between bricks — common in {cn}'s older homes — tuckpointing is overdue."),
            (f"What towns in {cn} do you serve for chimney repair?",
             f"We serve every town, township, and borough across {cn}, including {towns}. If you're unsure whether we cover your specific area, call us — we almost certainly do."),
        ]
    return [
        (f"What handyman services do you offer in {cn}?",
         "Drywall patching, painting, door repair, furniture assembly, TV mounting, light electrical and plumbing, and general home maintenance — one call covers your whole repair list."),
        ("Can you handle multiple jobs in one visit?",
         "Yes — combining tasks like drywall patching with paint touch-ups, or outlet replacement with fan installation, is the most efficient way to use one appointment."),
        (f"What towns in {cn} do you serve for handyman services?",
         f"We serve every town, township, and borough across {cn}, including {towns}. If you're unsure whether we cover your specific area, call us — we almost certainly do."),
    ]


def area_page_html(svc, county):
    sn = svc["name"]
    cn = county["name"]
    slug = county["slug"]
    towns = county["towns"]
    parent_url = f'../../{svc["parent"]}/'
    parent_label = svc["parent_label"]
    cats = CATS_BY_KEY[svc["cats_key"]]
    meta_desc = f'Expert {sn.lower()} in {cn}, NJ. Licensed & insured technicians serving {towns} and surrounding areas. Free estimate — same-day available.'
    faqs = area_faqs(svc["cats_key"], cn, towns)
    faq_schema_items = ",\n".join(
        f'''          {{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}'''
        for q, a in faqs
    )
    schema = f"""[
      {{
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "{sn}",
        "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard"}},
        "areaServed": {{"@type": "AdministrativeArea", "name": "{cn}, New Jersey"}},
        "description": "{meta_desc}"
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{faq_schema_items}
        ]
      }}
    ]"""
    faqs_html = "".join(f"""
                <div class="faq-item reveal">
                    <button class="faq-question" aria-expanded="false"><span>{q}</span><i class="fas fa-plus"></i></button>
                    <div class="faq-answer" aria-hidden="true"><p>{a}</p></div>
                </div>""" for q, a in faqs)
    other_svcs = "\n".join(
        f'                        <a href="../{s["slug_prefix"]}-{slug}/"><i class="fas {s["icon"]}"></i> {s["name"]}</a>'
        for s in SERVICES if s["name"] != sn
    )
    sub_sections = sub_service_sections(sn, cn)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
    <meta name="description" content="{meta_desc}">
    <title>{sn} in {cn}, NJ | The Fix Wizard</title>
    <link rel="stylesheet" href="../../css/tw.css">
    <link rel="stylesheet" href="../../css/custom.css">
    <script type="application/ld+json">{schema}</script>
{BUBBLE_CSS}
</head>
<body>

{navbar_html(2)}

    <section class="sp-hero" style="padding-bottom:52px;">
        <div class="container">
            <nav class="area-hero-breadcrumb">
                <a href="../../">Home</a>
                <span class="sep"><i class="fas fa-chevron-right"></i></span>
                <a href="../../locations/">Locations</a>
                <span class="sep"><i class="fas fa-chevron-right"></i></span>
                <a href="../../locations/#{slug}">{cn}</a>
                <span class="sep"><i class="fas fa-chevron-right"></i></span>
                <span class="current">{sn}</span>
            </nav>
            <div class="area-hero-badge">
                <i class="fas {svc['icon']}"></i>
                <span>{sn}</span>
            </div>
            <h1 class="area-hero-h1">Expert {sn} in <em>{cn}</em>, New Jersey</h1>
            <div class="area-hero-pills">
                <span class="area-hero-pill"><i class="fas fa-map-marker-alt"></i> {cn}, NJ</span>
                <span class="area-hero-pill"><i class="fas fa-calendar-check"></i> Same-Day Available</span>
                <span class="area-hero-pill"><i class="fas fa-tag"></i> Free Estimates</span>
                <span class="area-hero-pill"><i class="fas fa-shield-halved"></i> Licensed &amp; Insured</span>
            </div>
            <div class="area-hero-ctas">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="../../#contact" class="btn btn-outline-white">Get Free Quote</a>
            </div>
        </div>
    </section>
{bubble_grid_html(cats, cn, loc_url="new-jersey", href_prefix="../../")}
    <section class="area-content">
        <div class="container">
            <div class="area-layout">

                <div class="area-body">
                    <h2>Our {sn} Services in {cn}, NJ</h2>
                    <p>The Fix Wizard provides professional {sn.lower()} throughout {cn}. Whether you're in {towns}, or anywhere else in the county, we bring licensed technicians, transparent pricing, and same-day availability directly to your door. Below is a full breakdown of every {sn.lower()} we handle in {cn}.</p>

{sub_sections}

                    <h2>Why {cn} Homeowners Choose The Fix Wizard</h2>
                    <p>We've worked in hundreds of {cn} homes across all property types — older colonials, postwar ranches, shore properties, and newer construction. Our technicians understand the specific challenges that {cn}'s housing stock, climate, and building codes present, and we bring the right tools and materials to every job.</p>
                    <ul>
                        <li>Licensed &amp; insured in New Jersey</li>
                        <li>Free estimates — no commitment required</li>
                        <li>Same-day appointments available across {cn}</li>
                        <li>Transparent, itemized pricing before we start</li>
                        <li>All work backed by a satisfaction guarantee</li>
                    </ul>

                    <h2>Service Areas Within {cn}</h2>
                    <p>We serve all towns, townships, and boroughs across {cn}: {towns}, and every community in between. If you're unsure whether we cover your specific area, call us — we almost certainly do.</p>
                </div>

                <aside class="area-sidebar">
                    <div class="area-cta-box">
                        <h3>Get a Free Estimate</h3>
                        <p>Available same-day across {cn}. Licensed &amp; insured. No obligation.</p>
                        <a href="tel:+15513504951" class="btn btn-primary"><i class="fas fa-phone"></i> (551) 350-4951</a>
                        <a href="../../#contact" class="btn btn-outline-white">Send a Message</a>
                    </div>

                    <div class="area-trust-box">
                        <h3>Why Trust Us</h3>
                        <ul class="area-trust-list">
                            <li><i class="fas fa-shield-halved"></i> Licensed &amp; Insured in NJ</li>
                            <li><i class="fas fa-calendar-check"></i> Same-Day Available</li>
                            <li><i class="fas fa-tag"></i> Free Estimates</li>
                            <li><i class="fas fa-star"></i> 4.9&#x2605; Google Rating</li>
                            <li><i class="fas fa-clock"></i> Mon–Sat 7am–7pm</li>
                        </ul>
                    </div>

                    <div class="area-services-box">
                        <h3>More Services in {cn}</h3>
                        <div class="area-svc-list">
{other_svcs}
                        </div>
                    </div>

                    <div class="area-services-box">
                        <h3>All NJ Pages</h3>
                        <div class="area-svc-list">
                            <a href="{parent_url}"><i class="fas {svc['icon']}"></i> {parent_label}</a>
                            <a href="../../locations/"><i class="fas fa-map-marker-alt"></i> All Service Areas</a>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </section>

    <section id="faq" class="faq">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Q&amp;A</span>
                <h2 class="section-title">{sn} <span class="text-accent">Questions</span></h2>
                <p class="section-desc">What {cn} homeowners ask most before booking {sn.lower()}.</p>
            </div>
            <div class="faq-accordion">{faqs_html}
            </div>
        </div>
    </section>

    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>{sn} in {cn}? We've Got You.</h2>
                <p>Free estimates across all of {cn}. Licensed &amp; insured. Same-day available.</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15513504951" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Quote</a>
            </div>
        </div>
    </section>

{footer_html(2)}

    <script type="module" src="../../js/service-page.js"></script>
{BUBBLE_JS}
</body>
</html>"""


def build_area_pages():
    count = 0
    for county in COUNTIES:
        for svc in SERVICES:
            dir_name = f'{svc["slug_prefix"]}-{county["slug"]}'
            out_dir = os.path.join(ROOT, "locations", dir_name)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w") as f:
                f.write(area_page_html(svc, county))
            count += 1
    print(f"  ✓  {count} service-area pages generated")


# ─── 3. PATCH EXISTING NAVBARS ──────────────────────────────────────────────────

def patch_navbar(filepath, depth):
    with open(filepath, "r") as f:
        content = f.read()
    if "locations/" in content and "Locations" in content:
        return False
    prefix = "../" * depth
    for contact_variant in [
        f'<li><a href="{prefix}#contact" class="nav-link">Contact</a></li>',
        f'<li><a href="{prefix}#contact" class="nav-link active">Contact</a></li>',
    ]:
        if contact_variant in content:
            content = content.replace(
                contact_variant,
                contact_variant + f'\n                <li><a href="{prefix}locations/" class="nav-link">Locations</a></li>',
                1
            )
            break
    mobile_contact = f'<li><a href="{prefix}#contact" class="mobile-link">Contact</a></li>'
    if mobile_contact in content:
        content = content.replace(
            mobile_contact,
            mobile_contact + f'\n            <li><a href="{prefix}locations/" class="mobile-link">Locations</a></li>',
            1
        )
    with open(filepath, "w") as f:
        f.write(content)
    return True


def patch_all_navbars():
    patched = 0
    service_dirs = [
        "drywall-repair-new-jersey", "garage-door-repair-new-jersey",
        "furniture-assembly-new-jersey", "painting-new-jersey",
        "door-repair-new-jersey", "chimney-masonry-new-jersey",
        "electrical-repair-new-jersey", "plumbing-repair-new-jersey",
        "mounting-installation-new-jersey",
    ]
    for d in service_dirs:
        path = os.path.join(ROOT, d, "index.html")
        if os.path.exists(path) and patch_navbar(path, 1):
            patched += 1
        sub_dir = os.path.join(ROOT, d)
        if os.path.isdir(sub_dir):
            for sub in os.listdir(sub_dir):
                blog = os.path.join(sub_dir, sub, "index.html")
                if os.path.exists(blog) and patch_navbar(blog, 2):
                    patched += 1
    print(f"  ✓  {patched} existing pages patched with Locations nav link")


# ─── 4. CLEVELAND SUBURBS ────────────────────────────────────────────────────────

CLEVELAND_SUBURBS = [
    {"name": "Cleveland",          "slug": "cleveland-oh",          "towns": "Downtown, Ohio City, Tremont, Lakewood border", "desc": "Ohio's second-largest city — dense urban housing stock with century-old properties and high demand for chimney and handyman work."},
    {"name": "Cleveland Heights",  "slug": "cleveland-heights-oh",  "towns": "Cedar Lee, Coventry, Noble, Taylor",            "desc": "Historic inner-ring suburb with Tudor Revivals and Colonials built in the 1920s–1940s — aging masonry and older home systems."},
    {"name": "Lakewood",           "slug": "lakewood-oh",           "towns": "Downtown Lakewood, Gold Coast, Birdtown",       "desc": "Dense west-side suburb with craftsman bungalows and brick Colonials — one of Ohio's most repair-active communities."},
    {"name": "Parma",              "slug": "parma-oh",              "towns": "Parma Center, Ridgewood, Greenbriar",           "desc": "Ohio's seventh-largest city with postwar ranches and cape cods that need regular upkeep and skilled trade work."},
    {"name": "Mentor",             "slug": "mentor-oh",             "towns": "Mentor-on-the-Lake, Mentor City Center",        "desc": "Growing northeastern suburb with diverse housing stock from mid-century builds to newer developments."},
    {"name": "Strongsville",       "slug": "strongsville-oh",       "towns": "Old Town, SouthPark area, Northwood",           "desc": "Upscale southwestern suburb with established neighborhoods and growing demand for premium home services."},
    {"name": "Westlake",           "slug": "westlake-oh",           "towns": "Crocker Park area, Bradley, Dover Center",      "desc": "Affluent western suburb with well-established neighborhoods, older chimneys, and active home improvement market."},
    {"name": "Beachwood",          "slug": "beachwood-oh",          "towns": "Chagrin Highlands, Cedar Center, Richmond Hts border", "desc": "Prosperous eastern suburb known for custom homes, well-maintained properties, and high expectations for service quality."},
    {"name": "Solon",              "slug": "solon-oh",              "towns": "Solon Square, Miles Road, Aurora Road corridor",  "desc": "High-income southeastern suburb with a mix of newer construction and older custom homes needing expert attention."},
    {"name": "North Olmsted",      "slug": "north-olmsted-oh",      "towns": "Butternut Ridge, Great Northern area",           "desc": "Western suburb with postwar housing stock and strong demand for chimney cleaning and handyman services."},
    {"name": "Rocky River",        "slug": "rocky-river-oh",        "towns": "Detroit Road, Wooster Road, Lake Road",         "desc": "Charming lakefront suburb with historic homes, older masonry, and waterfront properties requiring specialized care."},
    {"name": "Euclid",             "slug": "euclid-oh",             "towns": "Euclid Beach, Nottingham, Shore Cultural Centre","desc": "Eastern suburb with industrial-era housing that demands skilled masonry and handyman repair work."},
    {"name": "Shaker Heights",     "slug": "shaker-heights-oh",     "towns": "Van Aken, Ludlow, Onaway, Moreland",            "desc": "Architecturally significant planned community with Tudor Revivals and Colonials — premium masonry and handyman demand."},
    {"name": "Bay Village",        "slug": "bay-village-oh",        "towns": "Bay Square, Wolf Road, Porter Creek area",      "desc": "Lakefront suburb with distinctive vintage properties and coastal exposure that accelerates wear on masonry."},
    {"name": "Avon Lake",          "slug": "avon-lake-oh",          "towns": "Walker Road, Moore Road, Lake Road corridor",   "desc": "Growing western suburb with a mix of established lakeshore homes and newer residential developments."},
    {"name": "Fairview Park",      "slug": "fairview-park-oh",      "towns": "Lorain Road, Mastick Road, Fairview Park Center","desc": "Established mid-century suburb with active home renovation and strong community investment in property upkeep."},
    {"name": "Broadview Heights",  "slug": "broadview-heights-oh",  "towns": "Royalton Road, Broadview Road, SOM Center",     "desc": "Upscale southern suburb with custom builds and growing families investing in quality home services."},
    {"name": "North Royalton",     "slug": "north-royalton-oh",     "towns": "Royalton Road, State Road, York Road",          "desc": "Suburban community with a range of housing types and consistent demand for chimney and handyman repairs."},
    {"name": "Brunswick",          "slug": "brunswick-oh",          "towns": "Center Road, Pearl Road, Grafton Road",         "desc": "Growing suburban community with older and newer residential properties and a strong handyman service market."},
    {"name": "Chardon",            "slug": "chardon-oh",            "towns": "Chardon Square, South Street, Water Street",    "desc": "Small-town Geauga County community with older housing and severe winter conditions that accelerate chimney wear."},
]

CLEVELAND_SERVICES = [
    {"name": "Chimney Repair",     "slug_prefix": "chimney-repair-in",     "icon": "fa-fire",               "parent": "chimney-masonry-new-jersey",     "parent_label": "Chimney & Masonry"},
    {"name": "Handyman Services",  "slug_prefix": "handyman-services-in",  "icon": "fa-screwdriver-wrench", "parent": "handyman-services-new-jersey",   "parent_label": "Handyman Services"},
]


def cleveland_area_page_html(svc, suburb):
    sn = svc["name"]
    cn = suburb["name"]
    slug = suburb["slug"]
    towns = suburb["towns"]
    parent_url = f'../../{svc["parent"]}/'
    parent_label = svc["parent_label"]
    meta_desc = f'Expert {sn.lower()} in {cn}, Ohio. Licensed & insured technicians serving {cn} and the greater Cleveland area. Free estimate — same-day available.'
    schema = f"""{{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "{sn}",
      "provider": {{"@type": "LocalBusiness", "name": "The Fix Wizard"}},
      "areaServed": {{"@type": "City", "name": "{cn}", "containedInPlace": {{"@type": "State", "name": "Ohio"}}}},
      "description": "{meta_desc}"
    }}"""
    sub_sections = sub_service_sections(sn, cn)
    other_svcs = "\n".join(
        f'                        <a href="../{s["slug_prefix"]}-{slug}/"><i class="fas {s["icon"]}"></i> {s["name"]}</a>'
        for s in CLEVELAND_SERVICES if s["name"] != sn
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD}
    <meta name="description" content="{meta_desc}">
    <title>{sn} in {cn}, Ohio | The Fix Wizard</title>
    <link rel="stylesheet" href="../../css/tw.css">
    <link rel="stylesheet" href="../../css/custom.css">
    <script type="application/ld+json">{schema}</script>
</head>
<body>

{navbar_html(2)}

    <section class="sp-hero" style="padding-bottom:52px;">
        <div class="container">
            <nav class="area-hero-breadcrumb">
                <a href="../../">Home</a>
                <span class="sep"><i class="fas fa-chevron-right"></i></span>
                <a href="../../cleveland-ohio/">Cleveland, Ohio</a>
                <span class="sep"><i class="fas fa-chevron-right"></i></span>
                <span class="current">{sn}</span>
            </nav>
            <div class="area-hero-badge">
                <i class="fas {svc['icon']}"></i>
                <span>{sn}</span>
            </div>
            <h1 class="area-hero-h1">Expert {sn} in <em>{cn}</em>, Ohio</h1>
            <div class="area-hero-pills">
                <span class="area-hero-pill"><i class="fas fa-map-marker-alt"></i> {cn}, Ohio</span>
                <span class="area-hero-pill"><i class="fas fa-calendar-check"></i> Same-Day Available</span>
                <span class="area-hero-pill"><i class="fas fa-tag"></i> Free Estimates</span>
                <span class="area-hero-pill"><i class="fas fa-shield-halved"></i> Licensed &amp; Insured</span>
            </div>
            <div class="area-hero-ctas">
                <a href="tel:+15513504951" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> (551) 350-4951</a>
                <a href="../../#contact" class="btn btn-outline-white">Get Free Quote</a>
            </div>
        </div>
    </section>

    <section class="area-content">
        <div class="container">
            <div class="area-layout">
                <div class="area-body">
                    <h2>Our {sn} Services in {cn}, Ohio</h2>
                    <p>The Fix Wizard provides professional {sn.lower()} throughout {cn} and the greater Cleveland area. Whether you're near {towns}, we bring licensed technicians, transparent pricing, and same-day availability to your door.</p>

{sub_sections}

                    <h2>Why {cn} Homeowners Choose The Fix Wizard</h2>
                    <p>Cleveland's climate — harsh winters, freeze-thaw cycles, and lake-effect weather — puts unique demands on homes. Our technicians understand the specific challenges that {cn}'s housing stock presents and bring the right materials and methods to every job.</p>
                    <ul>
                        <li>Licensed &amp; insured in Ohio</li>
                        <li>Free estimates — no commitment required</li>
                        <li>Same-day appointments available in {cn}</li>
                        <li>Transparent, itemized pricing before we start</li>
                        <li>All work backed by a satisfaction guarantee</li>
                    </ul>

                    <h2>Service Areas Near {cn}</h2>
                    <p>We serve {cn} and the surrounding communities throughout the greater Cleveland area. Call us at (551) 350-4951 to confirm same-day availability in your neighborhood.</p>
                </div>

                <aside class="area-sidebar">
                    <div class="area-cta-box">
                        <h3>Get a Free Estimate</h3>
                        <p>Available same-day in {cn}, Ohio. Licensed &amp; insured. No obligation.</p>
                        <a href="tel:+15513504951" class="btn btn-primary"><i class="fas fa-phone"></i> (551) 350-4951</a>
                        <a href="../../#contact" class="btn btn-outline-white">Send a Message</a>
                    </div>
                    <div class="area-trust-box">
                        <h3>Why Trust Us</h3>
                        <ul class="area-trust-list">
                            <li><i class="fas fa-shield-halved"></i> Licensed &amp; Insured in Ohio</li>
                            <li><i class="fas fa-calendar-check"></i> Same-Day Available</li>
                            <li><i class="fas fa-tag"></i> Free Estimates</li>
                            <li><i class="fas fa-star"></i> 4.9&#x2605; Google Rating</li>
                            <li><i class="fas fa-clock"></i> Mon–Sat 7am–7pm</li>
                        </ul>
                    </div>
                    <div class="area-services-box">
                        <h3>More Services in {cn}</h3>
                        <div class="area-svc-list">
{other_svcs}
                        </div>
                    </div>
                    <div class="area-services-box">
                        <h3>Back to Cleveland</h3>
                        <div class="area-svc-list">
                            <a href="../../cleveland-ohio/"><i class="fas fa-location-dot"></i> Cleveland, Ohio Hub</a>
                            <a href="{parent_url}"><i class="fas {svc['icon']}"></i> {parent_label}</a>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </section>

    <section class="cta-banner">
        <div class="container cta-inner reveal">
            <div class="cta-text">
                <h2>{sn} in {cn}, Ohio? We've Got You.</h2>
                <p>Free estimates across the greater Cleveland area. Licensed &amp; insured. Same-day available.</p>
            </div>
            <div class="cta-btns">
                <a href="tel:+15513504951" class="btn btn-white btn-lg"><i class="fas fa-phone"></i> Call Now</a>
                <a href="../../#contact" class="btn btn-outline-white btn-lg"><i class="fas fa-envelope"></i> Get a Quote</a>
            </div>
        </div>
    </section>

{footer_html(2)}

    <script type="module" src="../../js/service-page.js"></script>
</body>
</html>"""


def build_cleveland_area_pages():
    count = 0
    for suburb in CLEVELAND_SUBURBS:
        for svc in CLEVELAND_SERVICES:
            dir_name = f'{svc["slug_prefix"]}-{suburb["slug"]}'
            out_dir = os.path.join(ROOT, "locations", dir_name)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w") as f:
                f.write(cleveland_area_page_html(svc, suburb))
            count += 1
    print(f"  ✓  {count} Cleveland area pages generated")


# ─── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building locations hub page...")
    build_locations_page()
    print("Generating NJ service area pages...")
    build_area_pages()
    print("Generating Cleveland area pages...")
    build_cleveland_area_pages()
    print("Patching existing navbars...")
    patch_all_navbars()
    print("\nDone. Run: ./node_modules/.bin/tailwind -i css/input.css -o css/tw.css --minify")
