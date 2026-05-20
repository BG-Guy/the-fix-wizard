"""
Central service definitions used by generate_service_hubs.py,
patch_service_pages.py, and generate_service_detail_pages.py.
"""

# Each service: (icon, display_name, url_slug, short_desc, includes_list)
CHIMNEY_SERVICES_FULL = [
    # Inspections & Sweep
    ("fa-magnifying-glass", "Level 1 Inspection &amp; Standard Sweep", "chimney-inspection-standard-sweep",
     "Annual sweep removes creosote and checks for obstructions, cracks, and code issues. Written report included.",
     ["Full flue sweep with rotary brushes", "HEPA vacuum containment — no mess", "Visual inspection of accessible surfaces", "Written condition report", "Creosote level classification"]),

    ("fa-camera", "Level 2 Inspection (Camera Scan)", "chimney-level-2-inspection",
     "Video camera scanning of the entire flue — required for real estate transactions and after any chimney fire.",
     ["HD camera scan of full flue length", "Documentation for real estate transfer", "Structural integrity assessment", "Written report with still images"]),

    ("fa-broom", "Heavy Creosote Rotary Cleaning", "creosote-rotary-cleaning",
     "Stage 2 and 3 glazed creosote requires mechanical rotary systems beyond standard brushing to remove safely.",
     ["Rotary drill and brush system", "Stage 2/3 creosote breakdown", "Post-clean inspection and report", "HEPA vacuum containment"]),

    # Caps, Covers & Maintenance
    ("fa-circle-dot", "Single-Flue Stainless Steel Cap", "chimney-cap-installation",
     "A properly sized stainless steel cap keeps rain, animals, and debris out while allowing exhaust to escape.",
     ["Flue measurement and sizing", "Stainless steel cap installation", "Stainless screw fastening", "Fit and draft verification"]),

    ("fa-layer-group", "Multi-Flue / Custom Top-Mount Cap", "custom-chimney-cap-installation",
     "Covers the entire chimney top for complete protection across all openings. Custom-fitted to your dimensions.",
     ["Multi-flue coverage measurement", "Custom or standard top-mount cap", "Full chimney crown coverage", "Stainless steel construction"]),

    ("fa-square", "Chase Cover Replacement", "chase-cover-replacement",
     "Rusted galvanized chase covers are replaced with stainless or aluminum covers that won't rot or stain masonry.",
     ["Remove and dispose of rusted cover", "Custom-fit new stainless or aluminum cover", "Perimeter seal to prevent leaks", "Water diversion test"]),

    ("fa-droplet-slash", "Chimney Water Repellent Application", "chimney-waterproofing",
     "Penetrating waterproofer blocks moisture entry while allowing vapor to escape — prevents freeze-thaw spalling.",
     ["Clean chimney surface before treatment", "Penetrating vapor-permeable waterproofer", "Full brick and mortar coverage", "10-year protection"]),

    ("fa-wrench", "Flashing Repair &amp; Installation", "chimney-flashing-repair",
     "Failed step and counter flashing at the chimney-roof junction is a leading cause of attic water damage.",
     ["Remove and dispose of old flashing", "Step flashing woven into shingles", "Counter flashing secured to chimney", "Sealant at all joints", "Water test verification"]),

    ("fa-droplet", "Chimney Leak Repair", "chimney-leak-repair",
     "We trace the leak to its source — crown, flashing, cap, mortar, or liner — and fix the root cause, not the symptom.",
     ["Systematic leak source diagnosis", "Crown, flashing, and mortar inspection", "Repair at root cause", "Interior water damage assessment", "Written report"]),

    ("fa-paw", "Animal Removal", "chimney-animal-removal",
     "Raccoons, squirrels, birds, and bats nest in uncapped chimneys. We remove animals, clean the flue, and cap to prevent return.",
     ["Humane animal removal", "Nest and debris removal", "Full flue sweep after removal", "Chimney cap installation", "Entry point identification"]),

    # Masonry & Crown Repairs
    ("fa-helmet-safety", "Crown Repair (Elastomeric Coating)", "chimney-crown-repair",
     "Cracked crowns let water into the masonry. We fill cracks and coat the entire surface with flexible elastomeric sealant.",
     ["Crack routing and cleaning", "Elastomeric sealant application", "Full crown surface coverage", "Flexible bond for freeze-thaw movement"]),

    ("fa-hat-hard", "Full Chimney Crown Rebuild", "chimney-crown-rebuild",
     "Severely deteriorated crowns need a full rebuild. We pour a new overhanging concrete crown to proper slope and thickness.",
     ["Remove deteriorated crown", "Form and pour new concrete crown", "Correct slope for water diversion", "Overhang drip edge", "Final elastomeric seal"]),

    ("fa-trowel-bricks", "Tuckpointing &amp; Mortar Repair", "chimney-tuckpointing",
     "Crumbling mortar joints ground out to depth and packed with fresh mortar — matched to original profile and color.",
     ["Angle grinder removal of deteriorated mortar", "Type S mortar packing and tooling", "Color-matched mortar", "Full brush-clean finish"]),

    ("fa-fire-flame-curved", "Firebox Re-bricking / Refractory Panel Swap", "firebox-rebricking",
     "Cracked firebrick lets combustion gases reach framing — a fire hazard. Replaced with refractory materials rated for firebox heat.",
     ["Firebrick removal and inspection", "Refractory brick and mortar replacement", "Temperature-rated materials only", "Safety inspection on completion"]),

    ("fa-fire", "Firebox Rebuild", "firebox-rebuild",
     "A full firebox rebuild replaces all damaged firebrick, rebuilds deteriorated walls, and restores the firebox to safe operating condition.",
     ["Complete firebrick demolition and removal", "New refractory brick installation", "Refractory mortar throughout", "Proper firebox geometry maintained", "Smoke shelf inspection"]),

    ("fa-cloud", "Smoke Chamber Parge", "smoke-chamber-parge",
     "The smoke chamber above the firebox is often rough corbeled brick. Parging smooths and seals it — improving draft and stopping gas seepage.",
     ["Firebox access and preparation", "Refractory parge coat application", "Smooth interior for improved draft", "All gaps and cracks sealed", "Heat-cure before use"]),

    # Components & Liners
    ("fa-toggle-on", "Top-Damper Installation", "chimney-damper-installation",
     "Top-mount dampers seal the flue at the chimney top — far more energy-efficient than throat dampers and doubles as a rain cap.",
     ["Remove old throat damper if applicable", "Top-mount damper sizing and installation", "Seal to flue tile", "Control cable run to fireplace"]),

    ("fa-pipe", "Stainless Steel Flue Liner Installation", "chimney-liner-installation",
     "A correctly sized and installed liner is required by code for most appliances and prevents combustion gases from reaching structural framing.",
     ["Size calculation for appliance and BTUs", "Liner installation from top down", "Insulation wrap for proper draft", "Top plate and connector fitting", "Draft test and code verification"]),
]

HANDYMAN_SERVICES_FULL = [
    # Mounting & Hanging
    ("fa-tv", "TV Wall Mounting", "tv-wall-mounting",
     "Mounted securely on any wall type — drywall, concrete, brick, or tile. Stud-located, level-checked, cables routed in-wall on request.",
     ["Stud location or masonry anchor", "Mount level and secured", "TV hung and adjusted", "Cable concealment in-wall (optional)", "All connections made"]),

    ("fa-image", "Heavy Mirror / Large Artwork Hanging", "mirror-artwork-hanging",
     "Heavy mirrors and large framed artwork hung with the correct anchors, toggle bolts, or stud mounting for the weight and wall type.",
     ["Weight assessment and anchor selection", "Wall type identification", "Level hanging with proper anchors", "Anti-tip security for large pieces"]),

    ("fa-image", "Picture &amp; Mirror Hanging", "picture-mirror-hanging",
     "Standard picture frames, groupings, and mirrors hung level with the right fastener for every wall type — no guesswork.",
     ["Level and spacing layout", "Correct fastener for wall type", "Gallery wall arrangement", "Clean finish with no visible hardware damage"]),

    ("fa-window-restore", "Blinds / Shades / Curtain Rod Installation", "blinds-curtain-rod-installation",
     "Blinds, shades, and curtain rods installed level — inside or outside mount — with the correct hardware for your window frame material.",
     ["Level measurement and marking", "Inside or outside mount", "Correct anchors for window material", "Operation test and adjustment"]),

    ("fa-layer-group", "Floating Shelves Installation", "floating-shelves-installation",
     "Floating shelves and wall-mounted storage anchored to studs or correct drywall anchors, genuinely level and rated for the load.",
     ["Stud finding and load assessment", "Level marking and bracket install", "Shelf secured and tested", "Clean finish with no visible hardware"]),

    # Minor Plumbing & Bath
    ("fa-faucet", "Kitchen or Bathroom Faucet Replacement", "faucet-replacement",
     "Old faucet removed, new fixture installed correctly — supply lines connected, shutoff valves tested, no drips.",
     ["Shutoff and disconnect old faucet", "Install new faucet body and supply lines", "Test for leaks at all connections", "Drain reassembly and test"]),

    ("fa-trash-can", "Garbage Disposal Replacement", "garbage-disposal-replacement",
     "Old disposal removed and new unit installed — wiring reconnected, drain plumbing sealed, reset button tested.",
     ["Disconnect and remove old disposal", "Mount and wire new unit", "Reconnect drain plumbing correctly", "Reset and operation test"]),

    ("fa-toilet", "Toilet Reset / Flange Repair / Inner Components Swap", "toilet-repair",
     "Running toilet, rocking toilet, or failed flange — diagnosed and fixed on the first visit.",
     ["Diagnose root cause (flapper, fill valve, flange, wax ring)", "Replace necessary components", "Anchor and level toilet if reset", "Flush test and leak check"]),

    ("fa-fan", "Bathroom Exhaust Fan Replacement", "bathroom-exhaust-fan",
     "Noisy or failed exhaust fan swapped for a new quiet unit — wiring reconnected, duct connection verified.",
     ["Remove old fan and housing", "Install new fan unit", "Reconnect wiring", "Duct connection verified", "Operation test"]),

    ("fa-shower", "Shower Head &amp; Grab Bar Installation", "shower-head-grab-bar",
     "Shower head upgraded and grab bars anchored to studs or with the correct toggle system for tile walls.",
     ["Remove old shower head", "Install new shower head with correct sealing", "Locate studs or use appropriate anchors for grab bar", "Grab bar load test"]),

    ("fa-droplet", "Tub Caulking", "tub-caulking",
     "Failed caulk around tubs and showers removed completely, substrate cleaned, and fresh sealant applied with clean tooled lines.",
     ["Old caulk removal — full strip, no overlap", "Surface cleaning and drying", "Backer rod if needed", "Fresh sealant with clean tooled joint", "Cure time guidance"]),

    # Minor Electrical & Fixtures
    ("fa-fan", "Ceiling Fan Installation", "ceiling-fan-installation",
     "Ceiling fan installed on a fan-rated box — wiring connected, blades balanced, remote or wall switch set up.",
     ["Fan-rated box verification or installation", "Wiring connection and tuck", "Fan assembly and blade attachment", "Balance test at all speeds"]),

    ("fa-lightbulb", "Standard Light Fixture / Chandelier Swap", "light-fixture-installation",
     "Fixture removed and new one installed — wiring matched, junction box load verified for heavy chandeliers.",
     ["Remove old fixture", "Verify box capacity for new weight", "Connect wiring correctly", "Fixture mount and test"]),

    ("fa-plug", "Outlet / Switch Upgrades", "outlet-switch-upgrades",
     "Dead outlets, faulty switches, GFCI replacements, and USB combo outlets — diagnosed and replaced safely.",
     ["Diagnose outlet or switch fault", "Replace device with correct type", "GFCI protection where required by code", "Test for proper function"]),

    ("fa-bell", "Video Doorbell / Smart Lock Installation", "video-doorbell-smart-lock",
     "Video doorbell wired or battery-mounted and app-configured. Smart lock installed and paired to your phone.",
     ["Remove old doorbell or lock", "Install and wire/mount new device", "Wi-Fi pairing and app setup", "Operation test and walkthrough"]),

    # Carpentry, Drywall & Trim
    ("fa-fill-drip", "Drywall Patching", "drywall-patching",
     "Holes, cracks, and water damage patched invisibly — texture-matched so the repair blends with surrounding wall.",
     ["Damage assessment and prep", "Patch or California patch for larger holes", "Joint compound and texture match", "Sand and prime ready for paint"]),

    ("fa-ruler-horizontal", "Baseboard / Shoe Molding Installation", "baseboard-molding-installation",
     "New baseboard and shoe molding measured, cut, and installed — coped inside corners, mitered outside, caulked and painted.",
     ["Measure and cut to fit", "Coped inside corners", "Mitered outside corners", "Nail and secure to wall", "Caulk and fill nail holes"]),

    ("fa-screwdriver-wrench", "Cabinet Hinge &amp; Hardware Upgrade", "cabinet-hardware-upgrade",
     "Sagging doors re-hung, soft-close hinges installed, and new pulls and handles fitted across every cabinet.",
     ["Hinge adjustment or replacement", "Soft-close hinge installation", "Hardware pull drilling and installation", "Door alignment check"]),

    ("fa-screwdriver-wrench", "Cabinet Repair &amp; Replacement", "cabinet-repair-replacement",
     "Damaged cabinet boxes repaired or replaced, doors re-hung, drawers re-tracked, and hardware updated for a like-new result.",
     ["Damaged panel repair or replacement", "Door re-hanging and alignment", "Drawer slide replacement", "Hardware installation", "Finish touch-up"]),

    ("fa-dog", "Pet Door Installation", "pet-door-installation",
     "Pet door cut into an exterior door, wall, or sliding glass panel — correctly sized, sealed, and weather-tight.",
     ["Size selection for pet", "Cut opening in door or wall", "Frame and seal installation", "Flap and lock mechanism test", "Weatherstripping seal"]),

    # Assembly & Miscellaneous
    ("fa-couch", "Flat-Pack Furniture Assembly", "furniture-assembly",
     "IKEA, Wayfair, and Amazon flat-pack assembled correctly — beds, wardrobes, desks, shelving, and dining sets of any size.",
     ["Unbox and sort all hardware", "Correct assembly per instructions", "Anti-tip bracket installation", "Level and stable finish"]),

    ("fa-stairs", "Attic Ladder Replacement", "attic-ladder-replacement",
     "Old or failed attic ladder removed and new unit installed — framed correctly, insulated, and tested for safe operation.",
     ["Remove old ladder and frame", "Frame rough opening if needed", "Install new ladder unit", "Insulation gasket seal", "Load and operation test"]),

    ("fa-inbox", "Mailbox &amp; Post Installation", "mailbox-post-installation",
     "New mailbox and post set to proper height, plumb, and secured — concrete footing for freestanding posts.",
     ["Post hole digging and concrete footing", "Post plumb and set", "Mailbox mounting at regulation height", "Final plumb and level check"]),

    # Exterior & Roofing
    ("fa-house-chimney-crack", "Roof Leak Repair", "roof-leak-repair",
     "Roof leaks traced to their source — failed flashing, cracked shingles, or vent boots — and sealed or replaced to stop water entry.",
     ["Leak source diagnosis (interior and exterior)", "Flashing repair or replacement", "Cracked shingle or vent boot repair", "Sealant application", "Water test after repair"]),

    ("fa-border-top-left", "Fascia Repair", "fascia-repair",
     "Rotted or damaged fascia board repaired or replaced — keeping gutters properly supported and roofline looking clean.",
     ["Remove damaged fascia section", "Treat or replace underlying sheathing", "Install new primed fascia board", "Caulk and paint to match"]),

    ("fa-tint-slash", "Gutter Repair &amp; Cleaning", "gutter-repair-cleaning",
     "Gutters cleaned of debris, sagging sections re-hung, seams resealed, and downspouts cleared for proper drainage.",
     ["Full gutter debris removal", "Sagging section rehang and re-pitch", "Seam and joint resealing", "Downspout clearing and extension check", "Water flow test"]),

    ("fa-border-all", "Fence Repair &amp; Installation", "fence-repair-installation",
     "Leaning fence posts reset with concrete, damaged panels replaced, and new sections installed for privacy or boundary definition.",
     ["Post assessment and reset or replacement", "Panel replacement or repair", "Gate alignment and hardware", "New section installation with concrete footings"]),
]

LOCATIONS = [
    {"name": "New Jersey",     "slug": "new-jersey",  "short": "NJ",  "url": "new-jersey",    "area": "all 21 counties — Bergen to Cape May"},
    {"name": "Cleveland, Ohio","slug": "cleveland",   "short": "CLE", "url": "cleveland-ohio", "area": "greater Cleveland — Lakewood, Parma, Shaker Heights, and more"},
]

# Category groupings for hub bubble display
CHIMNEY_CATS = [
    ("Inspections &amp; Sweep Services", "fa-magnifying-glass",
     ["chimney-inspection-standard-sweep", "chimney-level-2-inspection", "creosote-rotary-cleaning"]),
    ("Caps, Covers &amp; Maintenance", "fa-circle-dot",
     ["chimney-cap-installation", "custom-chimney-cap-installation", "chase-cover-replacement",
      "chimney-waterproofing", "chimney-flashing-repair", "chimney-leak-repair", "chimney-animal-removal"]),
    ("Masonry &amp; Crown Repairs", "fa-trowel-bricks",
     ["chimney-crown-repair", "chimney-crown-rebuild", "chimney-tuckpointing",
      "firebox-rebricking", "firebox-rebuild", "smoke-chamber-parge"]),
    ("Components &amp; Liners", "fa-pipe",
     ["chimney-damper-installation", "chimney-liner-installation"]),
]

HANDYMAN_CATS = [
    ("Mounting &amp; Hanging", "fa-tv",
     ["tv-wall-mounting", "mirror-artwork-hanging", "picture-mirror-hanging",
      "blinds-curtain-rod-installation", "floating-shelves-installation"]),
    ("Minor Plumbing &amp; Bath", "fa-faucet",
     ["faucet-replacement", "garbage-disposal-replacement", "toilet-repair",
      "bathroom-exhaust-fan", "shower-head-grab-bar", "tub-caulking"]),
    ("Minor Electrical &amp; Fixtures", "fa-bolt",
     ["ceiling-fan-installation", "light-fixture-installation",
      "outlet-switch-upgrades", "video-doorbell-smart-lock"]),
    ("Carpentry, Drywall &amp; Trim", "fa-fill-drip",
     ["drywall-patching", "baseboard-molding-installation", "cabinet-hardware-upgrade",
      "cabinet-repair-replacement", "pet-door-installation"]),
    ("Assembly &amp; Miscellaneous", "fa-couch",
     ["furniture-assembly", "attic-ladder-replacement", "mailbox-post-installation"]),
    ("Exterior &amp; Roofing", "fa-house-chimney-crack",
     ["roof-leak-repair", "fascia-repair", "gutter-repair-cleaning", "fence-repair-installation"]),
]

def get_service_by_slug(slug, service_list):
    for s in service_list:
        if s[2] == slug:
            return s
    return None

def build_service_lookup(service_list):
    return {s[2]: s for s in service_list}


# ── Blog content per service slug ─────────────────────────────────────────────
# Each entry: intro (str), signs (list), steps (list), benefits (list of (title,desc)), price (str)

SERVICE_CONTENT = {

# ─── CHIMNEY ──────────────────────────────────────────────────────────────────

"chimney-inspection-standard-sweep": {
    "intro": "An annual chimney inspection and sweep is the single most important maintenance task for any home with a fireplace or wood-burning appliance. Creosote — the tarry byproduct of combustion — builds up inside the flue every time you burn wood. At Stage 3, glazed creosote is highly flammable and the direct cause of most chimney fires. A professional Level 1 inspection catches structural problems, blockages, and deterioration before they become emergencies.\n\nThe National Fire Protection Association (NFPA 211) recommends that chimneys be inspected at least once per year. In colder climates like New Jersey and Cleveland, where fireplaces see heavy winter use and freeze-thaw cycles stress masonry, annual service is essential — not optional.",
    "signs": [
        "You haven't had an inspection in over a year",
        "You notice a strong smoky or acrid odor from the fireplace when not in use",
        "Smoke backs into the room instead of drawing up the flue",
    ],
    "steps": [
        ("Visual exterior inspection", "We check the crown, cap, flashing, and exposed masonry for cracks, spalling, or deterioration."),
        ("Flue brush sweep", "Rotary brushes clear creosote from flue walls top to bottom while a HEPA vacuum captures every particle — your home stays clean."),
        ("Firebox and smoke shelf inspection", "We inspect the firebox, damper, and smoke shelf for cracks, blockages, and debris."),
        ("Written report", "You receive a condition report noting creosote classification, any deficiencies found, and recommended next steps."),
    ],
    "benefits": [
        ("Fire prevention", "Creosote is the #1 cause of chimney fires. Regular sweeping removes the fuel source before it can ignite."),
        ("Early problem detection", "Small cracks in the crown or liner caught during inspection cost a fraction of what they cost after a winter of water infiltration."),
        ("Code compliance", "NFPA 211 and most homeowner insurance policies require annual chimney inspection. Our written report documents compliance."),
    ],
    "price": "A standard Level 1 inspection and sweep typically costs $150–$300 depending on flue height and creosote level. Heavy Stage 2 or 3 buildup requiring rotary cleaning is priced separately.",
},

"chimney-level-2-inspection": {
    "intro": "A Level 2 chimney inspection uses a video camera to scan every inch of the flue interior — including areas completely inaccessible to visual inspection. It is required by the NFPA whenever a property changes ownership, following any chimney fire or significant event, or when a Level 1 inspection reveals potential structural issues.\n\nFor real estate transactions specifically, a Level 2 inspection provides documented proof of chimney condition for buyers, sellers, and their insurance companies. The camera reveals cracks in flue tile, gaps at joints, and deterioration hidden deep in the flue that no amount of flashlight inspection could find.",
    "signs": [
        "You are buying or selling a home with a fireplace",
        "You recently had a chimney fire, lightning strike, or seismic event",
        "A Level 1 inspection found indications of potential liner damage",
    ],
    "steps": [
        ("Camera equipment setup", "We lower a high-definition inspection camera from the chimney top, transmitting live footage to a monitor at the firebox."),
        ("Full-length flue scan", "Every joint, tile section, and transition is captured on video and reviewed in real time."),
        ("Damage documentation", "Any cracks, gaps, offsets, or deterioration are photographed and timestamped in the report."),
        ("Written report with images", "You receive a full written report with still images — suitable for real estate disclosure, insurance claims, or repair planning."),
    ],
    "benefits": [
        ("Complete flue visibility", "Camera inspection finds hidden cracks and gaps that are invisible to standard visual inspection but allow combustion gases to escape into framing."),
        ("Real estate documentation", "A Level 2 report satisfies the documentation requirements for property transfer and provides legal protection for both parties."),
        ("Accurate repair scoping", "Knowing exactly what is damaged — and where — eliminates guesswork and prevents over- or under-scoping liner and repair work."),
    ],
    "price": "Level 2 inspections typically run $250–$500. This includes the camera scan, written report, and still images. The cost is almost always recouped in repair savings or negotiating leverage during real estate transactions.",
},

"creosote-rotary-cleaning": {
    "intro": "Standard chimney brushes remove Stage 1 creosote — the powdery, flaky buildup from normal use. But Stage 2 (tar-like, crunchy) and Stage 3 (glazed, shiny) creosote cannot be removed with brushes alone. These dense deposits cling to flue walls and require mechanical rotary cleaning systems that physically grind and break down the buildup.\n\nIgnoring heavy creosote is not an option. Stage 3 glazed creosote is extremely flammable and burns at temperatures that can crack flue tiles, warp metal liners, and ignite adjacent wood framing. A chimney fire can reach 2,000°F — well beyond what most chimneys are designed to withstand.",
    "signs": [
        "Your last inspection classified creosote at Stage 2 or Stage 3",
        "You burn green or unseasoned wood regularly",
        "You notice a strong, acrid smell from the fireplace even when it is not in use",
    ],
    "steps": [
        ("Creosote classification", "We inspect and classify the buildup level before selecting the appropriate cleaning method."),
        ("Rotary drill system", "Mechanical rotary heads are lowered into the flue and spin against the deposits, breaking them free from the liner walls."),
        ("Vacuum containment", "A high-powered HEPA vacuum keeps all dislodged material contained — nothing enters your living space."),
        ("Post-clean inspection", "After cleaning, we inspect the liner for any damage revealed beneath the buildup and document the final condition."),
    ],
    "benefits": [
        ("Fire hazard elimination", "Removing Stage 2 and 3 creosote eliminates the primary fuel source for chimney fires — the most important safety step you can take."),
        ("Improved draft", "Heavy creosote restricts the flue opening, reducing draft and causing smoke to back up into the home. Cleaning restores proper airflow."),
        ("Liner preservation", "Acidic creosote accelerates corrosion of metal liners and deterioration of clay tiles. Removing it early extends liner life significantly."),
    ],
    "price": "Heavy creosote rotary cleaning typically costs $250–$500 above a standard sweep, depending on the degree of buildup and flue length. Chemical treatments for Stage 3 may add $100–$200.",
},

"chimney-cap-installation": {
    "intro": "An uncapped chimney flue is an open invitation — for rain, snow, animals, and debris. Every rainstorm sends water directly into the flue, saturating the masonry and accelerating freeze-thaw deterioration. Birds, squirrels, and raccoons find open flues irresistible nesting sites. A properly fitted stainless steel chimney cap solves all of these problems at once.\n\nChimney caps are among the best investments in chimney longevity. A $200–$300 cap can prevent thousands in water damage repairs, animal removal costs, and liner deterioration over its lifetime. Stainless steel caps are virtually maintenance-free and carry lifetime warranties.",
    "signs": [
        "Water appears in the firebox or smoke shelf after rain",
        "You hear scratching or rustling sounds inside the chimney",
        "You find leaves, twigs, or debris on the smoke shelf",
    ],
    "steps": [
        ("Flue measurement", "We measure the exterior flue tile dimensions precisely — an improperly sized cap either falls in or fails to seal the opening."),
        ("Cap selection", "We select a stainless steel cap with mesh sides to keep animals out while allowing exhaust to exit freely."),
        ("Secure installation", "The cap is fastened with stainless steel screws or a compression-fit band, depending on flue tile type."),
        ("Draft and fit verification", "We confirm the cap does not restrict draft and is correctly aligned over the flue opening."),
    ],
    "benefits": [
        ("Water exclusion", "A properly fitted cap prevents direct rainfall from entering the flue — the leading cause of liner corrosion, mortar deterioration, and masonry damage."),
        ("Animal exclusion", "Stainless mesh sides block birds, bats, squirrels, and raccoons from entering the flue and nesting."),
        ("Debris and ember protection", "Caps also catch embers traveling up the flue, reducing ember-related roof fire risk in wildfire-adjacent areas."),
    ],
    "price": "Single-flue stainless steel cap installation typically costs $150–$350 depending on flue size and accessibility. Custom-sized caps for non-standard flues run $250–$500.",
},

"custom-chimney-cap-installation": {
    "intro": "Chimneys with multiple flues — or those using a prefabricated factory-built system — require a different approach than a standard single-flue cap. A top-mount cap covers the entire chimney top, protecting every flue opening simultaneously and providing a clean, uniform appearance from the roofline.\n\nCustom top-mount caps are fabricated to fit the exact dimensions of your chimney's crown, ensuring no gaps between the cap base and the masonry surface. This eliminates the water infiltration points that individual single-flue caps leave exposed on multi-flue chimneys.",
    "signs": [
        "Your chimney has two or more flue openings",
        "You have a prefabricated factory-built chimney system with a metal chase",
        "Water enters the chimney despite having individual flue caps installed",
    ],
    "steps": [
        ("Crown measurement", "We measure the full chimney crown dimensions to fabricate or select the correctly sized top-mount cap."),
        ("Cap selection or fabrication", "Standard top-mount caps are available for common sizes; non-standard chimneys require custom fabrication."),
        ("Crown surface preparation", "Any loose mortar or debris on the crown surface is cleared to ensure full contact and seal."),
        ("Installation and sealing", "The cap is fastened at multiple points and the perimeter is sealed with an appropriate masonry sealant."),
    ],
    "benefits": [
        ("Complete top protection", "A single top-mount cap protects every flue opening, every gap in the crown, and the mortar wash in one installation."),
        ("Water diversion", "The sloped cap surface sheds water away from the crown and chimney top, significantly reducing moisture absorption."),
        ("Unified appearance", "Top-mount caps give multi-flue chimneys a clean, intentional look rather than a collection of mismatched individual caps."),
    ],
    "price": "Custom top-mount cap installation typically costs $350–$700 depending on chimney dimensions and whether the cap requires custom fabrication.",
},

"chase-cover-replacement": {
    "intro": "Prefabricated factory-built chimney systems — common in homes built after 1980 — use a metal chase (an enclosure around the flue pipe) instead of traditional masonry. These chases rely on a flat metal chase cover to protect the interior from weather. The problem: most factory-installed chase covers are galvanized steel, and in the wet climates of New Jersey and northeastern Ohio, they rust through within 10–15 years.\n\nA rusting chase cover is immediately visible as rust-colored stains streaking down the white or painted chase enclosure. More critically, a deteriorated cover allows water to pool inside the chase, accelerating corrosion of the flue pipe and damaging the chimney interior.",
    "signs": [
        "Orange or brown rust stains streaking down the sides of your chimney chase",
        "Water dripping inside the fireplace or visible water inside the chase enclosure",
        "The existing cover is visibly buckled, rusted, or has holes",
    ],
    "steps": [
        ("Old cover removal", "We safely remove the deteriorated cover and dispose of it — exposing the full chase top for inspection."),
        ("Chase top inspection", "We inspect the flue pipe, any visible interior surfaces, and the chase framing for water damage."),
        ("New cover installation", "A new stainless steel or aluminum cover is fitted precisely to the chase dimensions with a positive slope for water runoff."),
        ("Perimeter sealing", "All edges are sealed with a weatherproof sealant to prevent any water infiltration at the seam."),
    ],
    "benefits": [
        ("Rust prevention", "Stainless steel chase covers will not rust — ever. One replacement eliminates the 10–15 year replacement cycle of galvanized steel."),
        ("Interior protection", "A properly fitted cover keeps rain, snow, and ice out of the chase interior, preventing pipe corrosion and frame rot."),
        ("Curb appeal restoration", "Rust stains on chase enclosures are visible from the street. A new cover stops the staining immediately."),
    ],
    "price": "Chase cover replacement typically costs $200–$500 depending on chase dimensions and material selected. Stainless steel covers cost more upfront but eliminate future replacement.",
},

"chimney-waterproofing": {
    "intro": "Brick and mortar are porous — they absorb water. On an unprotected chimney, every rain event saturates the masonry and every freeze-thaw cycle (common in both New Jersey and Cleveland) forces that absorbed water to expand inside the brick, spalling the face and crumbling the mortar. Over years, this is the mechanism that destroys chimneys from the outside in.\n\nPenetrating chimney waterproofer — different from ordinary paint or sealer — soaks into the masonry and bonds with the mineral structure, blocking liquid water while remaining vapor-permeable. This means moisture trapped inside the masonry can still escape as vapor, preventing the efflorescence and trapped-moisture damage that paint causes.",
    "signs": [
        "White chalky stains (efflorescence) on chimney brick — a sign that water is moving through the masonry",
        "Brick faces that are crumbling, flaking, or pitting (freeze-thaw spalling)",
        "Mortar joints that look eroded or set back from the brick face",
    ],
    "steps": [
        ("Surface preparation", "The chimney is dry-brushed and any loose material removed. Application on a damp surface or before rain is avoided."),
        ("Repair first", "Any significant cracks, failed mortar, or damaged crown are addressed before waterproofing — sealing over damage locks moisture in."),
        ("Waterproofer application", "A penetrating, vapor-permeable masonry waterproofer is applied by brush or sprayer to full saturation — two coats minimum."),
        ("Cure time", "The product requires 24–48 hours to fully cure before rain exposure. We schedule accordingly."),
    ],
    "benefits": [
        ("Freeze-thaw protection", "By blocking liquid water absorption, waterproofing prevents the freeze-thaw cycle that is the leading cause of brick spalling and mortar deterioration."),
        ("Efflorescence prevention", "No water movement through the masonry means no mineral salt deposits forming on the brick surface."),
        ("Investment protection", "Waterproofing applied after tuckpointing or crown repair protects the new mortar and extends the life of that repair significantly."),
    ],
    "price": "Chimney waterproofing typically costs $150–$350 depending on chimney size. It is most cost-effective when combined with tuckpointing or other masonry repair, as mobilization costs are shared.",
},

"chimney-flashing-repair": {
    "intro": "Step flashing and counter flashing form the water seal at the junction between your chimney and roof — the most vulnerable water entry point on any home with a chimney. When this flashing fails, water runs directly into the gap between the chimney and the roof decking, travels down rafters, and appears as ceiling stains inside the home — often far from the chimney itself.\n\nFlashing failure is almost always the cause when homeowners report a 'chimney leak' after inspection shows no crown, cap, or mortar problems. Failed caulk, lifting counter flashing, or corroded step flashing are the most common culprits, and all are fully repairable without roof replacement.",
    "signs": [
        "Water stains on the ceiling inside the home in the vicinity of the chimney",
        "Visible rust staining or lifted edges on the flashing at the roof-chimney junction",
        "Daylight or gaps visible between the flashing and the chimney masonry",
    ],
    "steps": [
        ("Leak source diagnosis", "We distinguish flashing failure from crown, cap, or mortar leaks through a systematic inspection — the repair approach depends on the source."),
        ("Old flashing removal", "Deteriorated step flashing is removed from between shingle courses and old counter flashing is stripped from the chimney."),
        ("Step flashing installation", "New galvanized or aluminum step flashing is woven between shingle courses along both sides of the chimney."),
        ("Counter flashing and sealant", "New counter flashing is secured into the chimney mortar joints and sealed with an appropriate roofing-grade caulk at all edges."),
    ],
    "benefits": [
        ("Leak elimination", "Correctly installed step and counter flashing is the only reliable long-term solution for chimney-adjacent water intrusion — caulk-only 'repairs' fail within 2–3 years."),
        ("Structural protection", "Stopping water infiltration at the flashing prevents ongoing deterioration of roof decking, rafters, and ceiling materials."),
        ("Insurance documentation", "A written report of the flashing repair and the leak source provides documentation for homeowner insurance claims if interior damage is present."),
    ],
    "price": "Chimney flashing repair typically costs $350–$900 depending on chimney size, roof pitch, and how much of the flashing system needs replacement.",
},

"chimney-leak-repair": {
    "intro": "Chimney leaks are among the most misdiagnosed home repair problems. Water appearing in the firebox or on the ceiling near a chimney can originate from a failed crown, deteriorated flashing, a missing or damaged cap, cracked mortar joints, a cracked liner, or condensation — and each source requires a completely different repair. Treating the symptom without finding the source results in repeat leaks.\n\nOur leak diagnosis process is systematic and thorough. We work from the top of the chimney down, ruling out each potential source before recommending repairs. In many cases, a single afternoon of investigation reveals a straightforward fix that a previous contractor missed.",
    "signs": [
        "Water appears in the firebox, particularly after rain",
        "You see ceiling stains or peeling paint near the chimney in upper floors or attic",
        "A musty or moldy odor comes from the fireplace",
    ],
    "steps": [
        ("Top-down inspection", "We start at the cap and crown, then check flashing, mortar joints, and finally the liner — ruling out sources systematically."),
        ("Moisture testing if needed", "We use a garden hose test or moisture meter to isolate the specific entry point when the source is not visually obvious."),
        ("Root-cause repair", "We repair the actual source — whether that is a new crown, flashing work, tuckpointing, or cap installation."),
        ("Follow-up verification", "After repair, we verify the fix with a water test and confirm no secondary sources remain."),
    ],
    "benefits": [
        ("Permanent resolution", "Finding and fixing the actual source — not just caulking over symptoms — produces a repair that lasts rather than one that fails after the next rainstorm."),
        ("Damage prevention", "Water inside a chimney accelerates liner corrosion, masonry deterioration, and in worst cases, structural damage to adjacent framing."),
        ("Clear documentation", "Our written diagnosis report is valuable for insurance claims, future buyers, and understanding what your chimney actually needs."),
    ],
    "price": "Leak diagnosis starts at $150–$250 for inspection and report, applied toward repair costs. Total repair cost depends on source: cap installation ($150–$350), flashing ($350–$900), tuckpointing ($400–$2,000+).",
},

"chimney-animal-removal": {
    "intro": "An uncapped chimney is the most attractive nesting site in your neighborhood for raccoons, squirrels, birds, and bats. Chimney swifts, in particular, are federally protected migratory birds that nest exclusively in chimneys — and once nesting begins in spring, the flue cannot legally be disturbed until the birds migrate in fall.\n\nApart from the noise and odor, nesting animals create real fire hazards. Nests built from twigs, leaves, and debris in the smoke shelf and lower flue are highly flammable. Animal carcasses in the flue can cause dangerous carbon monoxide backup. The solution is humane removal, thorough cleaning, and immediate cap installation to prevent any return.",
    "signs": [
        "Scratching, chirping, or rustling sounds from inside the chimney, especially at dawn and dusk",
        "Strong ammonia or decay odor coming from the fireplace",
        "Twigs, leaves, or debris visible on the smoke shelf when you open the damper",
    ],
    "steps": [
        ("Species identification", "We identify what type of animal is present before attempting removal — protected species require different protocols than unprotected ones."),
        ("Humane removal", "Animals are removed using appropriate methods for the species and situation, without harm."),
        ("Full flue sweep", "After removal, we conduct a complete sweep to clear nesting material, debris, and any carcasses from the entire flue."),
        ("Cap installation", "We install a stainless steel cap immediately after cleaning to permanently prevent re-entry."),
    ],
    "benefits": [
        ("Fire hazard elimination", "Nesting material in the flue is a serious fire risk. Complete removal of all debris eliminates this hazard before the heating season."),
        ("Carbon monoxide prevention", "Decomposing animal remains and nest material can cause dangerous CO backup into the home — removal eliminates this risk."),
        ("Permanent exclusion", "Cap installation after removal is the only way to guarantee animals cannot return — without it, you will have the same problem next season."),
    ],
    "price": "Chimney animal removal typically costs $200–$450 depending on species and the extent of nest material. Cap installation is additional at $150–$350 and is strongly recommended as part of the same service call.",
},

"chimney-crown-repair": {
    "intro": "The chimney crown is the concrete or mortar cap that covers the top of the chimney, sloping away from the flue liner to direct water off the chimney top. When the crown cracks — as it does on almost every chimney over 15–20 years due to thermal expansion and freeze-thaw stress — water enters directly into the masonry below the cap line.\n\nElastomeric crown repair is the industry-preferred method for cracks up to about a quarter inch wide. A flexible elastomeric compound is forced into cracks and spread over the entire crown surface, creating a watertight, flexible membrane that moves with the masonry rather than cracking again at the repair points.",
    "signs": [
        "Visible cracks running across the crown surface, particularly radiating from the flue liner",
        "Spalling or flaking at the crown edges where it overhangs the chimney",
        "Water appears in the firebox after rain even though the cap is in place",
    ],
    "steps": [
        ("Crack assessment", "We measure crack width and depth to determine whether elastomeric repair or full crown rebuild is appropriate."),
        ("Surface cleaning", "Loose material is removed and the crown is thoroughly dried before any compound is applied."),
        ("Crack filling", "Cracks are filled with flexible elastomeric sealant, forced fully into the crack depth."),
        ("Full crown coat", "The entire crown surface — including the area around the flue liner — is coated with elastomeric compound for complete waterproofing."),
    ],
    "benefits": [
        ("Flexible waterproofing", "Unlike rigid mortar patches that crack again at the repair point, elastomeric compound flexes with thermal movement — repairs that hold through multiple freeze-thaw cycles."),
        ("Masonry protection", "A sealed crown stops the primary water entry point that drives deterioration in the masonry courses below."),
        ("Cost-effective repair", "Crown repair at the crack stage costs a fraction of a full crown rebuild — catching it early is the most cost-effective chimney maintenance step."),
    ],
    "price": "Chimney crown repair typically costs $200–$500 depending on crown size and the extent of cracking. Full crown rebuilds are necessary when damage is too extensive for elastomeric repair.",
},

"chimney-crown-rebuild": {
    "intro": "When a chimney crown is severely deteriorated — missing sections, crumbling at the edges, or broken down to the brick course below — elastomeric coating is no longer sufficient. A full crown rebuild removes all deteriorated material and pours a new properly designed concrete crown from scratch.\n\nA properly built chimney crown has two features most original crowns lack: an overhang beyond the chimney face with a drip edge to direct water away from the masonry below, and sufficient thickness (at least 2 inches at the thinnest point) to resist cracking. Many original crowns are thin, poorly formed, and bond directly to the flue liner — all design failures that cause premature cracking.",
    "signs": [
        "The crown has multiple large cracks or sections that are completely missing",
        "The crown surface is crumbling and material falls off when touched",
        "The crown is bonded directly to the flue liner with no expansion joint",
    ],
    "steps": [
        ("Demo and removal", "All deteriorated crown material is removed down to the top course of chimney brick. Material is bagged and removed from the roof."),
        ("Flue liner preparation", "The area around the flue liner is prepped and a bond breaker applied where the new crown will meet the liner — allowing independent movement."),
        ("Form and pour", "A form is built to create the proper overhanging profile, and concrete mixed to the correct water-cement ratio is poured and screeded."),
        ("Final seal", "After curing, the finished crown receives an elastomeric coat for additional waterproofing and surface protection."),
    ],
    "benefits": [
        ("Correct design", "A rebuilt crown has the proper overhang, drip edge, slope, and thickness that most original crowns lack — designed to last 20+ years rather than 10."),
        ("Flue liner protection", "The new crown seals the vulnerable area around the flue liner opening that is the primary entry point for water and debris."),
        ("Fresh 20-year baseline", "A new crown resets the maintenance clock on the most exposed and weather-vulnerable component of the chimney system."),
    ],
    "price": "Full chimney crown rebuilds typically cost $500–$1,200 depending on chimney size, roof accessibility, and crown dimensions. The investment prevents far more expensive masonry repairs below.",
},

"chimney-tuckpointing": {
    "intro": "Mortar is the weak link in any masonry structure. Brick and stone are essentially indestructible over human timescales — the mortar between them is not. In the wet climates of New Jersey and northeastern Ohio, mortar joints absorb water, and each freeze-thaw cycle erodes the mortar face and opens joints wider. Left untreated, deteriorated joints allow water to penetrate the chimney interior, saturating the surrounding brickwork and eventually causing the bricks themselves to crack and spall.\n\nTuckpointing — the process of grinding out deteriorated mortar and packing in fresh mortar — is the most important preventive maintenance you can perform on a brick chimney. Done at the right time, it costs $500–$2,000. Ignored for another decade, the same chimney may require a partial or full rebuild at $3,000–$10,000.",
    "signs": [
        "Mortar joints that appear recessed, eroded, or set back from the brick face",
        "Visible gaps or holes in the mortar between bricks",
        "White efflorescence staining on the brick surface indicating water is moving through the joints",
    ],
    "steps": [
        ("Joint depth assessment", "Deteriorated mortar must be ground out to at least 3/4 inch to ensure the new mortar has enough depth to bond properly."),
        ("Angle grinder removal", "We use a 4-inch angle grinder with a mortar-raking blade to remove deteriorated material cleanly without damaging brick faces."),
        ("Mortar matching", "We assess the existing mortar color, texture, and joint profile to mix a matching Type S mortar."),
        ("Packing and tooling", "New mortar is packed firmly into the joint in layers, then tooled to match the original profile — typically concave, V-shaped, or weathered."),
    ],
    "benefits": [
        ("Water exclusion", "Tight mortar joints are the primary defense against water infiltration in a masonry chimney — repointing restores this protection."),
        ("Structural integrity", "Open joints allow the bricks to shift and spall as water freezes inside them. Repointing stabilizes the masonry and stops brick loss."),
        ("Investment protection", "Tuckpointing at the right time costs a fraction of the masonry repair or rebuild required if joints are ignored until bricks fail."),
    ],
    "price": "Chimney tuckpointing typically costs $500–$2,500 depending on chimney size, height, accessibility, and the extent of joint deterioration. Free estimates are provided before any work begins.",
},

"firebox-rebricking": {
    "intro": "The firebox is the combustion chamber where fires burn, and every surface inside it must be able to withstand repeated thermal cycling to 1,000°F or more. Firebrick and refractory mortar — the materials that line a firebox — are engineered specifically for this environment. Standard brick and standard mortar are not.\n\nWhen firebrick cracks or spalls, it creates gaps that allow combustion gases and excessive heat to contact the surrounding framing and masonry. This is both a fire safety issue and a carbon monoxide risk. Cracked refractory panels in zero-clearance prefabricated fireplaces present the same hazard. Either way, the fireplace should not be used until the damaged material is replaced.",
    "signs": [
        "Cracks running through firebrick, particularly on the back wall of the firebox",
        "Firebrick faces that are spalling, crumbling, or falling out",
        "Refractory panels (in prefab fireplaces) that are cracked or broken",
    ],
    "steps": [
        ("Damage assessment", "We determine whether the damage is limited to the firebox or extends to the smoke chamber and lower flue — critical for scoping the full repair."),
        ("Brick and panel removal", "Damaged firebrick or refractory panels are carefully removed to avoid disturbing the surrounding structure."),
        ("Refractory installation", "New firebrick is set using refractory mortar rated for continuous firebox temperatures — standard mortar cannot be substituted."),
        ("Cure and safety check", "After installation, the mortar requires curing time before first use. We document completion for insurance or warranty purposes."),
    ],
    "benefits": [
        ("Fire safety restoration", "Intact firebrick prevents combustion heat from reaching adjacent wood framing — the primary purpose of the firebox lining."),
        ("Carbon monoxide protection", "Sealed firebox walls prevent combustion gases from escaping into wall cavities and entering living spaces."),
        ("Fireplace usability", "A repaired firebox restores full, safe use of your fireplace — damaged fireboxes should not be used until repairs are complete."),
    ],
    "price": "Firebox rebricking or refractory panel replacement typically costs $400–$1,500 depending on the extent of damage and whether it involves brick or prefab panels.",
},

"firebox-rebuild": {
    "intro": "A full firebox rebuild is necessary when damage is too extensive for patching — multiple structural cracks, missing bricks, a collapsed back wall, or a firebox that was never correctly constructed. Unlike rebricking, which replaces individual damaged components, a rebuild involves removing the entire firebox lining and reconstructing it from scratch to correct dimensions and specifications.\n\nFirebox geometry matters more than most homeowners realize. Correct firebox depth, back wall slope, and smoke shelf dimensions are required for proper draft. A poorly dimensioned firebox causes chronic smoke problems that no amount of cap, damper, or liner work can fix. A rebuild is the opportunity to correct those problems permanently.",
    "signs": [
        "Multiple structural cracks running through the firebox walls or floor",
        "The firebox has chronic smoke problems that persist despite other repairs",
        "Sections of the back or side walls have collapsed or are structurally unstable",
    ],
    "steps": [
        ("Full demo", "All existing firebrick, mortar, and refractory material is demolished and removed from the firebox and smoke shelf area."),
        ("Dimension verification", "We verify correct firebox dimensions (width, height, depth, back wall angle) before reconstruction begins."),
        ("Refractory rebuild", "New firebrick is installed in courses using refractory mortar, with the back wall angled correctly to direct combustion gases toward the smoke shelf."),
        ("Smoke shelf and chamber inspection", "After firebox completion, we inspect the smoke shelf and smoke chamber above for any conditions that would affect draft."),
    ],
    "benefits": [
        ("Structural integrity", "A completely rebuilt firebox has no legacy cracks, failed mortar, or compromised structure — it performs like new."),
        ("Correct draft geometry", "Rebuilding to correct dimensions resolves chronic smoke problems caused by an improperly proportioned original firebox."),
        ("Decades of safe operation", "A correctly built firebrick firebox with refractory mortar has a service life of 20–40 years before significant repair is needed."),
    ],
    "price": "Full firebox rebuilds typically cost $1,000–$3,500 depending on firebox size, accessibility, and whether the smoke chamber and lower flue require concurrent work.",
},

"smoke-chamber-parge": {
    "intro": "The smoke chamber is the funnel-shaped space between the top of the firebox and the bottom of the flue liner. Its job is to compress combustion gases and accelerate them into the flue for efficient venting. The problem: most smoke chambers in older homes were built using 'corbeled' brick — stair-stepped courses that create a rough, irregular interior surface full of gaps and ledges.\n\nThese gaps allow combustion gases to contact adjacent framing through the masonry wall, and the irregular surface promotes turbulence that reduces draft efficiency. Parging — applying a smooth refractory coating over the corbeled surface — seals every gap, creates a smooth aerodynamic interior, and dramatically improves both safety and draft performance.",
    "signs": [
        "Smoke consistently backs into the room even with a clear flue and functioning damper",
        "A previous inspection noted rough or 'corbeled' smoke chamber construction",
        "The home was built before 1980 and has never had a smoke chamber inspection",
    ],
    "steps": [
        ("Access preparation", "We access the smoke chamber through the fireplace opening and set up dust containment to protect the living space."),
        ("Surface assessment", "The full interior of the smoke chamber is inspected for gaps, cracks, and the extent of corbeling."),
        ("Parge coat application", "A refractory parge coat is applied by trowel or brush over the entire smoke chamber interior, filling all voids and creating a smooth surface."),
        ("Cure and use", "The parge coat requires a heat cure — typically a small fire 24 hours after application before full normal use."),
    ],
    "benefits": [
        ("Improved draft", "A smooth smoke chamber reduces turbulence and allows gases to accelerate up the flue more efficiently — often resolving chronic smoke backup."),
        ("Safety sealing", "Every gap in the corbeled masonry is filled, preventing combustion gases from contacting combustible framing materials in the chimney wall."),
        ("Code compliance", "Many jurisdictions require sealed smoke chambers for wood-burning appliances — parging satisfies this requirement."),
    ],
    "price": "Smoke chamber parging typically costs $250–$600 depending on smoke chamber size and accessibility. It is most cost-effective when combined with other firebox or liner work.",
},

"chimney-damper-installation": {
    "intro": "The traditional throat damper — a metal plate at the base of the flue just above the firebox — is one of the least effective energy-saving devices in a home. When closed, most throat dampers still leak substantial amounts of conditioned air up the flue due to warping from heat cycles and poor sealing design. A top-mount damper eliminates this problem by sealing the flue at the top of the chimney with a rubber gasket seal rated to be airtight.\n\nTop-mount dampers like the Lyemance and Lock-Top also double as chimney caps, providing rain and animal exclusion simultaneously. Homeowners who switch from throat to top-mount dampers typically report noticeable reductions in heating costs and the elimination of cold drafts from the fireplace.",
    "signs": [
        "You feel cold air coming down the chimney even when the throat damper is closed",
        "Your throat damper is warped, broken, or missing",
        "Heating bills are unusually high in rooms adjacent to the fireplace",
    ],
    "steps": [
        ("Old damper assessment", "We evaluate the existing throat damper condition and determine whether removal is required or if it can remain in the open position."),
        ("Flue measurement", "The flue tile opening at the chimney top is measured for the correct top-mount damper size."),
        ("Damper installation", "The top-mount damper is secured to the flue tile with the correct method for the tile type."),
        ("Cable routing", "The control cable is routed down the flue to the firebox and a mounting clip installed at the fireplace opening for easy operation."),
    ],
    "benefits": [
        ("Airtight seal", "A top-mount damper with rubber gasket seals the flue completely when closed — no air movement, no drafts, no heat loss."),
        ("Dual function", "Top-mount dampers serve as chimney caps simultaneously, eliminating the need for a separate cap installation."),
        ("Energy savings", "Eliminating the cold-air path down the flue can reduce heating costs noticeably in homes where the fireplace was previously a significant heat loss point."),
    ],
    "price": "Top-mount damper installation typically costs $250–$500 including the damper unit and installation labor. This often replaces a separate cap purchase as well.",
},

"chimney-liner-installation": {
    "intro": "A chimney liner — the clay tile, cast-in-place, or stainless steel tube running the length of the flue — contains combustion gases, protects the surrounding masonry from corrosive byproducts, and ensures gases are vented at the correct temperature to prevent condensation buildup. It is not optional: NFPA 211 and most local building codes require a properly sized and intact liner for any fuel-burning appliance.\n\nStainless steel flexible liners are the most commonly installed type for retrofits. They are sized precisely for the appliance's BTU output and fuel type, wrapped in insulation to maintain flue gas temperature, and connected to a top plate and appliance connector at each end. A correctly installed liner typically carries a lifetime warranty.",
    "signs": [
        "Your home has an older chimney with clay tile liner that has never been inspected or a Level 2 inspection revealed cracked tiles",
        "You are installing a new wood stove, gas insert, or oil furnace that requires a specific liner size",
        "A previous inspection found liner damage, significant offset, or code non-compliance",
    ],
    "steps": [
        ("Appliance and BTU assessment", "Liner diameter is calculated based on the appliance type, fuel, and BTU output — undersized liners cause back-drafting; oversized liners cause condensation."),
        ("Liner insertion", "The flexible stainless steel liner is lowered from the chimney top while a connector at the bottom guides it into the appliance connection point."),
        ("Insulation wrap", "An insulation blanket is wrapped around the liner inside the flue to maintain flue gas temperature and prevent condensation in cold exterior chimneys."),
        ("Top plate and connection", "A stainless steel top plate is fitted around the liner at the chimney crown, and the bottom connection is made to the appliance or fireplace opening."),
    ],
    "benefits": [
        ("Code compliance", "A new liner brings the chimney into current NFPA 211 compliance — required for permit work on appliances and for homeowner insurance in many cases."),
        ("Combustion gas containment", "A correctly sized liner keeps combustion gases — including carbon monoxide — contained within the flue and out of the surrounding masonry and framing."),
        ("Appliance efficiency", "Correct liner sizing optimizes draft for the specific appliance, improving combustion efficiency and reducing fuel consumption."),
    ],
    "price": "Stainless steel liner installation typically costs $1,800–$4,500 depending on flue length, liner diameter, and whether a clay liner removal is required. Liner systems carry lifetime warranties from major manufacturers.",
},

# ─── HANDYMAN ─────────────────────────────────────────────────────────────────

"tv-wall-mounting": {
    "intro": "A wall-mounted television transforms a room — it frees up floor space, improves viewing angles, eliminates the TV stand, and creates a clean, intentional look. But a TV mounted incorrectly is a safety hazard: a 65-inch OLED can weigh 80 pounds, and a mount that misses studs or uses inadequate anchors will eventually fail — often catastrophically.\n\nProfessional TV mounting ensures studs are correctly located (not guessed), the mount is rated for the TV weight and size, the screen is level to within a fraction of a degree, and cables are managed cleanly. On concrete, tile, or brick walls, the process requires entirely different hardware than drywall — hardware most homeowners don't have and can't source easily.",
    "signs": [
        "Your TV is on a stand that takes up floor space or creates a tripping hazard",
        "You want cables hidden inside the wall for a clean, built-in look",
        "The wall material is concrete, brick, or tile — requiring specialized anchors",
    ],
    "steps": [
        ("Wall assessment", "We determine wall type, locate all studs or structural points, and identify any obstructions (electrical, plumbing) before drilling."),
        ("Mount installation", "The mount bracket is secured into studs or masonry with fasteners rated for the TV weight plus a safety factor."),
        ("TV hanging and leveling", "The TV is mounted on the bracket and leveled to within 1/8 inch using a digital level."),
        ("Cable management", "Cables are routed through an in-wall cable management system or concealed in a surface raceway for a clean finish."),
    ],
    "benefits": [
        ("Safety", "A correctly anchored mount cannot pull free from the wall under normal use — protecting children, pets, and the TV itself from a fall."),
        ("Optimal viewing", "Mounting at the correct height and angle for your seating position eliminates neck strain and glare that floor-standing TVs often cause."),
        ("Room aesthetics", "A cleanly mounted TV with hidden cables looks like an architectural feature rather than an afterthought."),
    ],
    "price": "TV wall mounting typically costs $100–$250 depending on wall type, cable management scope, and TV size. Concrete or tile walls require specialty hardware and run toward the higher end.",
},

"mirror-artwork-hanging": {
    "intro": "A large mirror or oversized artwork can anchor a room and transform a blank wall into a design statement — but hanging a piece that weighs 40, 60, or 100 pounds requires more than a standard picture hook. Heavy items need to land on studs, use rated mounting hardware, and in many cases require two-point or French cleat systems that distribute weight correctly across the wall.\n\nThe consequences of improper hanging range from a hole in the drywall to a shattered mirror or damaged artwork — and in worst cases, injury. Professional hanging ensures the right anchor for the right weight on the right wall, every time.",
    "signs": [
        "The piece weighs more than 20 pounds or is larger than 24 inches in any dimension",
        "Your wall is plaster, tile, concrete, or brick — materials that require specialty anchors",
        "You want a two-point hang to keep the piece level over time",
    ],
    "steps": [
        ("Weight and dimension assessment", "We weigh the piece (or estimate from manufacturer specs) and assess the hanging hardware already attached."),
        ("Wall type identification", "We determine whether the mounting point is over a stud, in drywall, plaster, masonry, or tile — each requires a different fastener."),
        ("Anchor selection and installation", "Appropriate anchors rated for the piece weight plus a safety factor are installed — toggle bolts, screw anchors, masonry fasteners, or stud screws as required."),
        ("Level hang and anti-tip", "The piece is hung level and, for mirrors and very large artwork, a security wire or bumper is added to prevent shifting."),
    ],
    "benefits": [
        ("Weight-appropriate support", "Hardware selected for the actual weight of the piece — not just what was already on the wall — ensures the hang is safe for years."),
        ("Wall protection", "Correct anchors for the wall type prevent the tearing and blowout that oversized loads cause when standard picture hooks are used."),
        ("Perfect level", "A digital level ensures the piece hangs perfectly straight, not 'close enough' — the difference is immediately visible in a large mirror."),
    ],
    "price": "Heavy mirror and artwork hanging typically costs $75–$200 depending on piece size, wall type, and number of mounting points required.",
},

"picture-mirror-hanging": {
    "intro": "Hanging pictures sounds simple — and for a single small frame it is. But a gallery wall with 8 frames, a set of matched prints that need precise spacing, or a standard mirror hung in a bathroom with tile walls quickly becomes a project that benefits from professional execution. Getting spacing, alignment, and anchor selection right the first time prevents the repeated patching and rehanging that a DIY approach often produces.\n\nWe handle everything from single-frame hanging to full gallery wall layout — measuring spacing, marking anchor points, installing appropriate hardware, and hanging every piece level and at the correct height for the room.",
    "signs": [
        "You are hanging a gallery wall with multiple frames that need precise spacing",
        "The wall is tile, plaster, or concrete — materials where drilling without the right technique causes damage",
        "Previous hanging attempts left the wall looking patchy from multiple anchor holes",
    ],
    "steps": [
        ("Layout planning", "For gallery walls, we lay pieces out on the floor first and measure the arrangement before marking a single anchor point."),
        ("Height and spacing marking", "Anchor points are marked on the wall using a level and measuring tape — not eye measurement."),
        ("Anchor installation", "Appropriate anchors are installed for each piece weight and wall type."),
        ("Hang and final level", "Each piece is hung and checked with a level. Bumper pads are added to the bottom corners to keep frames from shifting."),
    ],
    "benefits": [
        ("Gallery wall precision", "Consistent spacing and perfect alignment turn a collection of frames into a designed installation rather than a random arrangement."),
        ("Minimal wall damage", "Correct anchor placement means one hole per anchor point — no exploratory drilling, no patchwork from missed attempts."),
        ("Lasting level", "Bumper pads and correctly tensioned wire prevent frames from tilting over time, even in high-traffic areas."),
    ],
    "price": "Single-frame hanging starts at $50–$75. Gallery walls of 4+ pieces typically run $125–$250 depending on count and complexity.",
},

"blinds-curtain-rod-installation": {
    "intro": "Blinds and shades look straightforward to install — until you discover that the inside-mount brackets don't align with the window frame thickness, the curtain rod is too heavy for the wall anchors that come in the box, or the wall above your window is plaster that shatters rather than grips standard anchors.\n\nProfessional installation handles all of this correctly the first time: inside-mount brackets adjusted for exact frame depth, outside-mount hardware anchored at the correct height and width, and curtain rods supported at the right intervals to prevent sagging under the weight of heavy drapery.",
    "signs": [
        "Your window frame is an unusual depth that makes inside-mount installation tricky",
        "You have heavy blackout curtains or drapery panels that require robust rod support",
        "Previous blinds installation left the brackets crooked or the blinds sitting unevenly in the frame",
    ],
    "steps": [
        ("Mount type determination", "We confirm inside vs. outside mount, measure the window recess depth, and select the appropriate bracket for the specific blind or shade type."),
        ("Anchor point marking", "Bracket positions are marked with a level — not by eye — to ensure the blind or rod hangs perfectly horizontal."),
        ("Anchor installation", "Appropriate fasteners are installed for the wall type: studs for heavy rods, rated drywall anchors for standard loads."),
        ("Bracket and hardware mounting", "Brackets are installed and blinds or rods mounted, leveled, and tested for smooth operation."),
    ],
    "benefits": [
        ("Correct inside-mount depth", "Blinds installed at the correct depth in the window recess hang flush and operate without rubbing against the frame."),
        ("Sag-free curtain rods", "Heavy drapery requires support at the correct intervals — longer rods need a center bracket that most DIY installs omit."),
        ("Consistent appearance across multiple windows", "Professional installation ensures all windows in a room hang at the same height for a cohesive look."),
    ],
    "price": "Blind and curtain rod installation typically runs $75–$175 per window depending on hardware type and wall material.",
},

"floating-shelves-installation": {
    "intro": "Floating shelves look minimal and clean — no visible brackets, just a shelf appearing to hover against the wall. Achieving this look correctly requires hitting studs with concealed bracket hardware, or using heavy-duty drywall anchors when studs are not at the right spacing. The weight the shelves need to support must be matched to the anchor type and spacing.\n\nThe common failure mode for DIY floating shelves is anchors that work for the first few months but gradually pull out of drywall under sustained load — especially if books, plants, or kitchenware are placed on them. We install floating shelves with hardware rated for the actual intended load, every time.",
    "signs": [
        "You want to add storage or display space without visible hardware or brackets",
        "The shelf will hold more than 20 pounds (books, plants, kitchen items, décor)",
        "Previous floating shelf attempts have resulted in pulled-out anchors or sagging",
    ],
    "steps": [
        ("Stud location", "We use a reliable stud finder and confirm locations by probing before marking — drywall anchors are used only when studs are not at the required spacing."),
        ("Level marking", "Shelf height and level are marked on the wall with a spirit level — multiple shelves are marked simultaneously for consistency."),
        ("Bracket installation", "Concealed L-brackets or keyhole brackets are secured into studs or with rated wall anchors at the correct spacing for the shelf length."),
        ("Shelf mounting and load test", "The shelf is set on the brackets, secured if required, and a light load test performed before leaving."),
    ],
    "benefits": [
        ("Safe load capacity", "Brackets installed into studs or with appropriate anchors hold the actual weight placed on shelves — not just the shelf itself."),
        ("Perfect horizontal", "A digital level ensures shelves are straight to the eye — slightly off-level shelves are immediately noticeable."),
        ("Finished look", "Correctly spaced and aligned floating shelves look intentional and designed, not improvised."),
    ],
    "price": "Floating shelf installation typically costs $75–$200 per shelf depending on length, wall type, and bracket system. Multiple shelves in the same visit are more cost-effective.",
},

"faucet-replacement": {
    "intro": "A dripping kitchen or bathroom faucet wastes more water than most homeowners realize — a faucet dripping once per second loses over 3,000 gallons per year. But beyond waste, an aging faucet with low pressure, discoloration, or a broken handle simply degrades the daily experience of the most-used fixtures in your home. Replacement is often more cost-effective than repair on faucets older than 10–15 years.\n\nFaucet replacement sounds simple but involves several potential complications: corroded supply line nuts that require specialty tools to remove, mismatched hole configurations between old and new fixtures, and stop valves that have not been turned in decades and no longer close fully.",
    "signs": [
        "The faucet drips persistently and cartridge replacement has not resolved it",
        "Water pressure is poor even though other fixtures in the home are normal",
        "The faucet is discolored, corroded, or has a broken handle or sprayer",
    ],
    "steps": [
        ("Shut-off and disconnect", "The supply valves under the sink are closed, supply lines drained, and the old faucet disconnected and removed."),
        ("Deck preparation", "The sink deck is cleaned of old putty and sealant residue to provide a clean surface for the new faucet."),
        ("New faucet installation", "The new faucet body, supply lines, and drain assembly are installed according to the manufacturer's instructions for the sink configuration."),
        ("Leak test", "With supply water restored, all connections are checked under pressure and the faucet operation tested for proper temperature and pressure."),
    ],
    "benefits": [
        ("Water savings", "Replacing a dripping faucet eliminates the 3,000+ gallon per year waste — a measurable reduction in water bills."),
        ("Stop valve reliability", "We test supply shut-off valves during replacement and replace any that no longer close fully — providing insurance against future leaks."),
        ("Modern functionality", "New faucets deliver better water efficiency, pressure, and features (pull-down sprayers, touchless operation) at a reasonable cost."),
    ],
    "price": "Faucet replacement typically costs $100–$300 in labor, not including the fixture itself. Supply line replacement and stop valve service may add $50–$100.",
},

"garbage-disposal-replacement": {
    "intro": "Garbage disposals have a typical service life of 8–12 years. The warning signs of a failing unit — persistent humming without spinning, frequent jams requiring manual reset, unusual grinding sounds, or leaks from the unit body — indicate that internal components have worn beyond the point of reliable repair. At that point, replacement is almost always more cost-effective than servicing.\n\nDisposal replacement is straightforward in theory but involves a sequence of steps — disconnecting drain plumbing, un-mounting the old unit, wiring the new unit, re-mounting, and reconnecting the drain — where a mistake at any step results in leaks or electrical issues.",
    "signs": [
        "The disposal hums when switched on but the grinding plate does not spin",
        "You reset the unit frequently and it still does not operate reliably",
        "The disposal is leaking from the bottom or sides of the unit body",
    ],
    "steps": [
        ("Power disconnection", "The disposal circuit is switched off at the breaker before any disconnection work begins."),
        ("Drain and mount removal", "Drain plumbing is disconnected and the old unit is untwisted from the sink mounting ring."),
        ("New unit wiring and mounting", "The new disposal is wired using the existing electrical connections, mounted to the sink ring, and the drain connection made."),
        ("Test run", "Power is restored, water is run, and the disposal is tested for correct operation, proper drain flow, and no leaks at any connection."),
    ],
    "benefits": [
        ("Reliable operation", "A new disposal eliminates the frustration of frequent jams, resets, and partial failures that signal the end of a unit's service life."),
        ("Leak prevention", "Leaks from a failing disposal body drip onto cabinet shelving and over time cause significant water damage — replacement stops this."),
        ("Noise reduction", "Modern disposals are significantly quieter than units from 10+ years ago — replacement is a noticeable quality-of-life improvement."),
    ],
    "price": "Garbage disposal replacement typically costs $150–$300 in labor, not including the new unit. Basic units start around $100; premium quiet models run $250–$400.",
},

"toilet-repair": {
    "intro": "A running toilet is one of the most wasteful plumbing conditions in a home — a continuously running fill valve can waste 200 gallons or more per day, showing up silently on your water bill for months before being noticed. A rocking toilet is a different problem with more serious consequences: a broken or deteriorated wax ring seal allows sewer gas to enter the home and, over time, allows water to seep under the floor at every flush.\n\nMost toilet problems — running, rocking, slow fill, weak flush — are resolved by replacing the internal components (flapper, fill valve, flush valve, wax ring) rather than the toilet itself. We diagnose the specific failure and repair it on the first visit in almost every case.",
    "signs": [
        "The toilet runs continuously or intermittently — you hear water flowing when the toilet hasn't been recently flushed",
        "The toilet rocks or shifts when you sit on it",
        "Water appears on the floor around the base of the toilet",
    ],
    "steps": [
        ("Diagnosis", "We identify the specific failure: running fill valve, bad flapper, worn flush valve, broken flange, or failed wax ring — each has a different repair."),
        ("Component replacement", "The failed component is replaced: flapper, fill valve, and flush valve are inexpensive parts; wax ring replacement requires removing and re-setting the toilet."),
        ("Bolt and flange check", "For rocking toilets, we inspect the closet flange for damage and replace both the wax ring and flange bolts."),
        ("Flush test and leak check", "With water restored, the toilet is flushed multiple times and all connections inspected for leaks."),
    ],
    "benefits": [
        ("Water bill reduction", "Fixing a running toilet can reduce monthly water bills by $30–$70 or more — the repair often pays for itself within the first billing cycle."),
        ("Subfloor protection", "A leaking wax ring allows water under the floor at every flush. Catching and repairing it early prevents subfloor rot and tile damage."),
        ("Sewer gas elimination", "A failed wax ring is a direct path for sewer gas into the home. Re-seating the toilet restores the gas barrier."),
    ],
    "price": "Toilet internal component replacement typically costs $100–$250 in labor. Toilet reset with new wax ring costs $150–$300. New toilet supply and installation adds $200–$400.",
},

"bathroom-exhaust-fan": {
    "intro": "A bathroom exhaust fan that doesn't work — or works so poorly that steam still coats every surface — is a direct cause of bathroom mold. Without adequate ventilation, humid air from showers and baths condenses on walls, ceilings, and in wall cavities, creating the warm, damp environment mold needs to grow. In bathrooms without windows, a working exhaust fan isn't optional — it's the only ventilation the room has.\n\nFan replacement is also one of the highest-impact bathroom upgrades available. Modern exhaust fans are dramatically quieter than fans from 10–15 years ago, and many include integrated LED lighting, humidity sensors, or Bluetooth speakers — functional upgrades that cost very little over basic models.",
    "signs": [
        "Steam and condensation remain on mirrors and walls for 30+ minutes after a shower",
        "Mold or mildew appears regularly on bathroom ceilings or grout lines",
        "The fan is loud, rattling, or operates noticeably slower than it used to",
    ],
    "steps": [
        ("Existing fan removal", "The old fan grille and housing are removed. We check the duct connection to the exterior vent."),
        ("Duct inspection", "The duct run from fan to exterior is checked for blockages, disconnection, or improper termination — a common cause of inadequate ventilation even with a new fan."),
        ("New fan installation", "The new fan housing is secured in the ceiling opening, wiring is connected, and the duct is attached securely."),
        ("Operation test", "The fan is switched on and airflow confirmed. The toilet paper test (tissue held at grille) confirms adequate suction."),
    ],
    "benefits": [
        ("Mold prevention", "Adequate air exchange after showers keeps humidity below the threshold for mold growth — the primary function of bathroom ventilation."),
        ("Noise reduction", "Modern fans rated at 0.3–1.0 sones are nearly silent compared to older 4.0 sone models — a noticeable improvement in bathroom comfort."),
        ("Energy efficiency", "New DC motor fans use 50–70% less electricity than older AC motor models while moving significantly more air."),
    ],
    "price": "Bathroom exhaust fan replacement typically costs $150–$350 in labor, not including the fan unit. Basic replacement fans start around $30; combination fan/light units run $75–$200.",
},

"shower-head-grab-bar": {
    "intro": "A shower head upgrade is one of the quickest, lowest-cost improvements to the daily experience in any bathroom. Replacing a 15-year-old 2.5 GPM shower head with a modern 1.8 GPM model with better pressure distribution costs under $50 in parts and half an hour in labor — but significantly improves every shower for years.\n\nGrab bar installation is a safety essential for bathrooms used by older adults, anyone recovering from surgery, or any household where a wet tile floor represents a fall risk. A correctly anchored grab bar — bolted into studs or installed with appropriate toggle anchors behind tile — can support 250+ pounds of force. An incorrectly anchored bar pulls free from the wall in an emergency.",
    "signs": [
        "Shower pressure is weak or the spray pattern is irregular despite adequate water pressure at other fixtures",
        "An older adult, recovering patient, or anyone with mobility limitations uses the shower",
        "The existing shower head is more than 10 years old or shows visible mineral buildup",
    ],
    "steps": [
        ("Shower head removal", "The old shower head is removed using proper tools to avoid damaging the shower arm — overtightening is a common DIY error."),
        ("Thread cleaning and sealing", "The shower arm threads are cleaned and fresh plumber's tape applied before the new head is installed."),
        ("Grab bar location marking", "Stud locations or appropriate anchor points behind tile are identified using a stud finder."),
        ("Grab bar installation", "The bar is bolted into studs or installed with appropriate toggle anchors rated for the required load, and tested with firm lateral pressure."),
    ],
    "benefits": [
        ("Fall prevention", "A correctly anchored grab bar provides a reliable support point that can prevent a fall on wet tile — the leading cause of home injury for adults over 65."),
        ("Better shower experience", "A new shower head delivers better coverage and pressure at lower water flow than older models."),
        ("ADA-ready bathroom", "Grab bar installation makes a bathroom more accessible for aging-in-place and increases home appeal for buyers with accessibility needs."),
    ],
    "price": "Shower head replacement costs $75–$150 in labor. Grab bar installation runs $100–$250 per bar depending on wall construction and bar length.",
},

"tub-caulking": {
    "intro": "The caulk line around your bathtub or shower pan is a critical waterproof seal — the only barrier between the water that splashes against it every day and the subfloor, studs, and drywall behind the tile. When caulk fails — it turns black with mold, peels, cracks, or pulls away from the surface — water infiltrates immediately, and the damage begins invisibly inside the wall.\n\nReplacing tub caulk is not simply applying a new bead over old caulk. The old caulk must be completely removed first — all of it. Applying over existing caulk creates a cosmetically improved but structurally compromised seal that will fail again in 6–12 months. Professional caulking means full removal, surface preparation, and a clean, tooled bead applied with the right product for the application.",
    "signs": [
        "The caulk line is black with mold or mildew that doesn't clean off",
        "Caulk is peeling, cracking, or pulling away from the tub or tile surface",
        "The caulk line has gaps or has completely separated at any point around the tub",
    ],
    "steps": [
        ("Old caulk removal", "Every trace of old caulk is removed using a caulk removal tool and utility knife — a step that cannot be skipped."),
        ("Surface cleaning and drying", "The joint is cleaned with an appropriate cleaner and allowed to dry completely before new caulk is applied — moisture causes adhesion failure."),
        ("Caulk application", "A flexible silicone or siliconized latex caulk appropriate for tub and tile is applied in a continuous bead along the full joint."),
        ("Tooling and cure", "The bead is tooled to a smooth concave profile and left to cure per manufacturer requirements — typically 24 hours before water exposure."),
    ],
    "benefits": [
        ("Waterproof seal restoration", "New caulk completely applied and properly tooled seals the joint against water infiltration that would otherwise damage subfloor and framing."),
        ("Mold elimination", "Removing and replacing black caulk eliminates the existing mold colony and provides a fresh surface that resists regrowth with correct ventilation."),
        ("Extended tile and tub life", "Water infiltration behind tile causes grout failure, tile delamination, and eventually subfloor damage — a $100 recaulk prevents thousands in tile replacement."),
    ],
    "price": "Tub and shower caulking typically costs $100–$250 depending on the length of caulk lines and accessibility. Shower surrounds with multiple surfaces run toward the higher end.",
},

"ceiling-fan-installation": {
    "intro": "Ceiling fans make a measurable difference in room comfort — and energy bills. In summer, the downdraft creates a wind chill effect that makes a room feel 4–6 degrees cooler, allowing thermostat setback. In winter, the reverse direction pushes warm air that has risen to the ceiling back down to living level. In rooms used regularly, a ceiling fan pays for itself in reduced HVAC costs within a single season.\n\nThe critical installation requirement that many homeowners are unaware of: ceiling fans must be mounted on a fan-rated electrical box. Standard light fixture boxes are not designed for the lateral and rotational forces a fan exerts, and mounting a fan on one is a code violation — and a safety hazard that has caused numerous ceiling collapses.",
    "signs": [
        "A room runs consistently hot in summer or cold in winter despite normal HVAC",
        "You are replacing an existing fan that wobbles, is noisy, or has a failing motor",
        "You want to add a fan to a room that currently only has a light fixture",
    ],
    "steps": [
        ("Box verification", "We confirm whether a fan-rated box is present. Standard light fixture boxes must be replaced before fan installation — we handle this as part of the service."),
        ("Fan assembly", "Fan components are assembled per manufacturer instructions before installation — assembling on the floor is safer and more precise than assembling overhead."),
        ("Wiring and mounting", "The fan is connected to the existing wiring, mounted to the fan-rated box, and balanced."),
        ("Balance and speed test", "The fan is run at all speeds in both directions — any wobble is corrected using the included blade balancing kit."),
    ],
    "benefits": [
        ("Energy cost reduction", "A ceiling fan used in conjunction with your thermostat can reduce cooling costs by 4–8% per room — measurable savings over a full season."),
        ("Year-round use", "Ceiling fans in reverse (clockwise at low speed) redistribute warm air from the ceiling in winter, reducing the load on your heating system."),
        ("Safe, code-compliant installation", "Mounting on a fan-rated box ensures the fan will not pull free from the ceiling over time — the most important safety requirement."),
    ],
    "price": "Ceiling fan installation typically costs $150–$300 in labor, including fan-rated box upgrade if required. Fans themselves range from $50 for basic models to $300+ for premium silent motors.",
},

"light-fixture-installation": {
    "intro": "Replacing a dated light fixture is one of the highest-return cosmetic upgrades in any room. A new flush mount in a bedroom, a statement pendant over a kitchen island, or a chandelier in a dining room immediately changes the feel of the space — and modern LED-compatible fixtures use a fraction of the energy of the incandescent-era fixtures they replace.\n\nFixture installation involves more than just swapping one for another. Heavy chandeliers require a rated brace or fan-rated box — standard boxes are rated for 50 pounds; many chandeliers exceed this. Wiring configurations vary between single-switch, three-way, and dimmer setups, and miswiring results in flickering, buzzing, or a fixture that doesn't operate correctly.",
    "signs": [
        "The current fixture is visually outdated or no longer suits the room's style",
        "You are installing a chandelier or semi-flush fixture heavier than the standard 50-pound box rating",
        "You want to add a dimmer switch as part of the fixture upgrade",
    ],
    "steps": [
        ("Power off and box assessment", "The circuit is switched off at the breaker and the existing junction box inspected for its weight rating."),
        ("Box upgrade if needed", "Fixtures over 50 pounds require a fan-rated box or adjustable brace — we install this before mounting any heavy fixture."),
        ("Wiring connection", "Wires are connected in the correct configuration for the switch setup — single pole, three-way, or dimmer-compatible wiring."),
        ("Fixture mounting and test", "The fixture is mounted, any bulbs installed, and the circuit restored. The fixture is tested on all switch positions."),
    ],
    "benefits": [
        ("Immediate visual impact", "A new fixture is one of the fastest and most cost-effective ways to update a room's appearance without renovation."),
        ("Energy reduction", "LED-compatible fixtures paired with LED bulbs use 75% less electricity than incandescent equivalents — visible on every electric bill."),
        ("Safe, weight-appropriate installation", "Correctly rated mounting hardware ensures chandeliers and heavy fixtures remain safely anchored for their full service life."),
    ],
    "price": "Light fixture installation typically costs $100–$250 in labor. Heavy chandeliers requiring a brace installation add $75–$125. The fixture itself is customer-supplied or sourced per preference.",
},

"outlet-switch-upgrades": {
    "intro": "Dead outlets, switches that feel warm, and outlets that sparks when plugging in a device are not minor inconveniences — they are electrical safety issues that should be addressed promptly. Dead outlets are often caused by a tripped GFCI upstream in the circuit, but can also indicate a loose or failed device. Warm switches or outlets indicate excessive resistance in the connection, which generates heat.\n\nBeyond repairs, outlet and switch upgrades are also a maintenance and modernization opportunity. Replacing standard outlets with GFCI-protected devices in kitchens, bathrooms, and garages brings these circuits into current code compliance. Adding USB combo outlets to high-use locations eliminates adapter clutter. Replacing standard switches with smart dimmers provides energy savings and convenience.",
    "signs": [
        "An outlet produces no power even though the breaker is on — often a tripped GFCI upstream",
        "A switch or outlet feels warm to the touch, even when nothing is plugged in",
        "Outlets in kitchen, bathroom, or garage are not GFCI-protected",
    ],
    "steps": [
        ("Circuit diagnosis", "We trace the circuit, test upstream GFCI devices, and identify whether the failure is in the device itself or at a connection."),
        ("Device replacement", "The failed outlet or switch is replaced with a new device of the appropriate type and amperage rating."),
        ("GFCI installation where required", "GFCI devices are installed in all NEC-required locations — kitchens, bathrooms, garages, outdoor circuits."),
        ("Load test", "All new devices are tested under load to confirm correct operation before completing the job."),
    ],
    "benefits": [
        ("Safety restoration", "Replacing a warm or sparking outlet eliminates the fire risk from high-resistance connections before they cause damage."),
        ("GFCI code compliance", "GFCI protection in wet areas is a code requirement — and provides genuine protection against electrocution in kitchen and bathroom environments."),
        ("Modern functionality", "USB combo outlets and smart dimmers add convenience at a cost of $20–$50 per device — typically installed in minutes."),
    ],
    "price": "Standard outlet or switch replacement typically costs $100–$175 per device including labor. GFCI installation runs $125–$200. Multiple devices in the same visit share the trip cost.",
},

"video-doorbell-smart-lock": {
    "intro": "Video doorbells and smart locks have moved from luxury to mainstream home security in the last five years. Seeing and speaking with visitors when you're not home, monitoring package delivery, and locking or unlocking your door remotely from a phone are all practical, daily-use features — not novelties. The challenge is installation: hardwired video doorbells require verifying the existing transformer voltage and wiring; smart locks require precise alignment of the latch, strike, and deadbolt for reliable operation.\n\nImproperly installed smart devices result in connectivity issues, poor video quality from doorbells mounted at the wrong height and angle, and locks that don't fully extend or retract reliably. Professional installation ensures the device works correctly from day one and is set up on your network.",
    "signs": [
        "You want to see visitors and delivery drivers when away from home",
        "Your existing deadbolt is manual and you want keypad or app-controlled access",
        "Your home's current doorbell wiring is older and you are unsure of its compatibility",
    ],
    "steps": [
        ("Compatibility check", "For video doorbells, we verify the existing doorbell transformer voltage (8–24V required) and wiring condition."),
        ("Device mounting", "The doorbell is mounted at the correct height (approximately 48 inches) for optimal face detection, with a wedge angle kit if the mounting surface is angled."),
        ("Smart lock installation", "The existing deadbolt is removed and the new smart lock installed with precise door edge and strike alignment."),
        ("Wi-Fi pairing and app setup", "Both devices are connected to your Wi-Fi network, paired to the companion app, and tested for complete functionality."),
    ],
    "benefits": [
        ("Remote visibility and access", "Seeing and speaking with anyone at your door from anywhere in the world — and unlocking for trusted visitors — is the primary daily value of these devices."),
        ("Package security", "Video footage of delivery interactions reduces package theft and provides documentation for claims."),
        ("Keyless entry convenience", "Smart locks eliminate the need to carry or hide spare keys — access codes for house cleaners, dog walkers, or guests are set and revoked remotely."),
    ],
    "price": "Video doorbell installation typically costs $100–$200. Smart lock installation runs $100–$200. Combined installation in one visit is more cost-effective than separate trips.",
},

"drywall-patching": {
    "intro": "Drywall damage is inevitable in any lived-in home — doorknobs punch through walls, anchors pull out and leave craters, water stains leave softened sections, and renovation work leaves gaps where old fixtures lived. What separates a professional patch from a DIY attempt is not the patch itself — it's the texture match. A correctly patched hole with mismatched texture is immediately visible, while a correctly patched and matched repair is completely invisible.\n\nTexture matching requires assessing the existing texture type (orange peel, knockdown, skip trowel, smooth Level 5), recreating it with the right technique and equipment, and testing the match before applying it to the repair area. This is the step most homeowners skip — and the reason most DIY patches are still visible after painting.",
    "signs": [
        "Holes from doorknobs, removed hardware, or accidental damage anywhere on walls or ceilings",
        "Water damage from a past leak that left soft, stained, or sagging drywall",
        "Seams and nail pops that have cracked through the surface of finished walls",
    ],
    "steps": [
        ("Damage assessment", "We determine the right repair method — setting-type compound for deep holes, standard compound for surface repairs, California patch or backer board for larger holes."),
        ("Patch installation", "The appropriate patch method is used based on hole size: mesh patch for small holes, California patch or blocking for medium holes, full backer board for large sections."),
        ("Texture match", "We assess the existing texture type and apply the appropriate technique — spray, trowel, or brush — testing on a scrap piece before touching the wall."),
        ("Prime and ready for paint", "The patched area is primed with drywall primer — painting without priming causes texture flashing that makes the repair visible even through paint."),
    ],
    "benefits": [
        ("Invisible repair", "A correctly patched and texture-matched repair is completely invisible after painting — the only acceptable result."),
        ("Structural restoration", "Soft, water-damaged drywall removed and replaced with new material restores the wall's structural contribution to the room and eliminates any mold substrate."),
        ("Paint-ready finish", "We leave the patch primed and ready for paint — you need only apply finish coats in your wall color."),
    ],
    "price": "Drywall patching typically costs $100–$350 per area depending on hole size, number of patches, and texture complexity. Water damage repairs with mold treatment run toward the higher end.",
},

"baseboard-molding-installation": {
    "intro": "Baseboards are the visual foundation of a room — they complete the transition between wall and floor and tie together the overall finish quality of the space. Missing sections after renovation, damaged boards from water or impact, or upgrading from builder-grade flat stock to a more substantial profile all create the need for baseboard work.\n\nBaseboard installation requires correct coping at inside corners (not mitering) for a gap-free result that holds up as the house settles, clean mitered outside corners, and secure attachment to the wall framing. The difference between professional and amateur baseboard work is visible from across the room — gaps at corners, boards that bow away from the wall, and caulk lines that try to hide the gaps.",
    "signs": [
        "Baseboards are missing in sections after renovation or floor installation",
        "Corners have visible gaps from settlement or improper original installation",
        "You are upgrading from flat builder-grade stock to a more detailed profile",
    ],
    "steps": [
        ("Measurement and material selection", "We measure the room perimeter, calculate material quantities, and confirm the profile matches existing boards or the customer's selection."),
        ("Cut and fit", "Inside corners are coped — not mitered — for a tight fit that accommodates settlement. Outside corners are mitered at 45 degrees."),
        ("Attachment", "Boards are nailed to the wall plate at stud locations with finish nails, countersunk for filling."),
        ("Fill, caulk, and ready for paint", "Nail holes are filled, the top edge of the baseboard is caulked to the wall, and the bottom is caulked to the floor for a finished appearance."),
    ],
    "benefits": [
        ("Finished appearance", "Properly installed baseboards with tight corners and clean caulk lines are the final step that makes a renovation look complete rather than unfinished."),
        ("Gap prevention", "Coped inside corners hold tight over time as the house settles — mitered corners open up, coped corners close."),
        ("Seamless material match", "We match existing profiles in adjacent rooms so new baseboard is indistinguishable from original work after painting."),
    ],
    "price": "Baseboard installation typically costs $150–$400 per room depending on room size, corner count, and profile complexity. Material cost is additional.",
},

"cabinet-hardware-upgrade": {
    "intro": "Cabinet hardware — hinges, pulls, and handles — is one of the most cost-effective cosmetic upgrades available for a kitchen or bathroom. Replacing basic chrome pulls with brushed nickel bar pulls, or swapping standard hinges for soft-close versions, instantly updates the feel of cabinets that may otherwise be in perfectly good condition.\n\nSoft-close hinge installation requires removing existing hinges, selecting the correct soft-close model for the cabinet door thickness and overlay, and adjusting the six-way (height, depth, side-to-side) adjustment on each hinge so every door closes perfectly flat and at the correct gap. Done correctly, it takes 20–30 minutes per door. Done in a hurry, misaligned doors and uneven gaps undermine the entire effect.",
    "signs": [
        "Cabinet doors slam rather than close softly — a constant noise and wear issue",
        "Existing pulls and handles are dated, corroded, or mismatched",
        "Cabinet doors are slightly misaligned and the existing hinges don't have adjustment capability",
    ],
    "steps": [
        ("Hardware selection and hole measurement", "Existing pull hole spacing (center-to-center) is measured to confirm replacement compatibility, or template marks are made for new holes."),
        ("Old hardware removal", "Existing hinges and pulls are removed. Screw holes that need to be relocated are filled."),
        ("Soft-close hinge installation", "New soft-close hinges are installed at the correct cup depth and overlay setting, then adjusted in all six planes for perfect door alignment."),
        ("Pull installation", "New pulls are installed with a jig for consistent alignment across all doors and drawers."),
    ],
    "benefits": [
        ("Soft-close functionality", "Soft-close hinges eliminate cabinet door slamming — protecting the cabinet box, reducing noise, and extending hinge life."),
        ("Fresh aesthetic", "New hardware is the fastest way to refresh dated kitchen or bathroom cabinetry without the cost of replacement."),
        ("Precise alignment", "Adjustable soft-close hinges allow fine-tuning of door position to achieve perfectly even gaps and a flat, consistent appearance."),
    ],
    "price": "Cabinet hardware upgrades typically cost $100–$300 in labor depending on cabinet count. Soft-close hinge upgrades run $10–$25 per hinge in parts.",
},

"cabinet-repair-replacement": {
    "intro": "Cabinets take more daily wear than almost any other fixture in the home — doors open and close hundreds of times per year, drawers are loaded and yanked, and the interior is exposed to humidity, cleaning products, and impact. Over time, hinges fail, drawer slides crack, doors warp, and cabinet boxes sustain damage from water or impact that compromises both appearance and function.\n\nMany homeowners assume damaged cabinets require full replacement — an expensive and disruptive project. In most cases, targeted repair is far more cost-effective: replacing a failed drawer slide, repairing a damaged panel, re-hanging a warped door, or refacing cabinet faces with new veneer or paint. We assess the actual condition and recommend the most cost-effective path.",
    "signs": [
        "Drawers that stick, won't close fully, or have fallen off the slides entirely",
        "Cabinet doors that are warped, cracked, or no longer hang straight",
        "Visible water damage on the cabinet box near the sink or dishwasher",
    ],
    "steps": [
        ("Assessment", "We inspect each cabinet for structural integrity, hardware condition, and cosmetic damage — distinguishing what is repairable from what requires replacement."),
        ("Hardware replacement", "Failed drawer slides, hinges, and door bumpers are replaced with correct-size replacements."),
        ("Panel repair or replacement", "Damaged cabinet box panels are repaired with filler and refinishing, or replaced if structural integrity is compromised."),
        ("Door and drawer alignment", "After repair, all doors and drawers are adjusted for proper operation and even appearance."),
    ],
    "benefits": [
        ("Cost vs. replacement", "Targeted cabinet repair typically costs 10–30% of full replacement while restoring full functionality and appearance."),
        ("Extended cabinet life", "Addressing hardware failures and water damage early prevents the progressive deterioration that eventually forces replacement."),
        ("Matching existing style", "Repair preserves the existing cabinet style — relevant in older homes where current stock doesn't match original millwork."),
    ],
    "price": "Cabinet repair typically costs $150–$500 per affected area depending on the extent of damage and parts required. Full cabinet replacement is quoted separately based on scope.",
},

"pet-door-installation": {
    "intro": "A pet door gives cats and dogs the freedom to move between indoors and outdoors on their own schedule, reducing the demand on owners to constantly manage access and eliminating the accident risk when no one is home to let them out. Modern pet doors with magnetic or electronic locking mechanisms also prevent wildlife from using the same entrance.\n\nInstallation location matters: exterior doors are the most common installation point, but pet doors can also be cut into walls, siding, or sliding glass door panels. Each surface requires a different approach — wood doors are straightforward, but metal doors, fiberglass, and masonry require specialty tools and techniques that are not appropriate for a DIY approach.",
    "signs": [
        "Your pet requires constant trips to the door to be let in and out",
        "You want to provide outdoor access during the day while you are at work",
        "Your existing pet door is damaged, has a broken flap, or is the wrong size for a new or larger pet",
    ],
    "steps": [
        ("Size and location selection", "We confirm the correct door size for the pet's height and weight, and identify the best installation location for the door and outside terrain."),
        ("Template marking", "The cut template is marked precisely on the door, wall, or panel, centered and at the correct height for the pet."),
        ("Cutting", "The opening is cut using appropriate tools for the material — jigsaw for wood doors, oscillating tool or reciprocating saw for walls, and specialty blades for fiberglass."),
        ("Frame installation and weatherstripping", "The pet door frame is installed, secured, and sealed at all edges to maintain the door's weathertightness."),
    ],
    "benefits": [
        ("Pet independence", "Freedom to come and go eliminates accidents, reduces anxiety in pets that need outdoor stimulation, and removes the constant interruption of managing access."),
        ("Security features", "Magnetic and microchip-activated pet doors allow only your pet to enter — preventing neighborhood animals from using the door."),
        ("Weathertight installation", "A correctly sealed pet door installation maintains the insulation value of the original door or wall with no air or water infiltration."),
    ],
    "price": "Pet door installation typically costs $150–$300 depending on door or wall material. Wall installation through multiple layers runs toward the higher end. The door unit itself is customer-supplied or sourced per preference.",
},

"furniture-assembly": {
    "intro": "Flat-pack furniture from IKEA, Wayfair, Amazon, and other retailers accounts for hundreds of millions of pieces assembled per year — and an enormous number of them are assembled incorrectly. Misaligned cam locks, reversed panels, missed dowels, and overtightened fasteners create furniture that wobbles, drawers that bind, and beds that squeak — or in worst cases, furniture that fails structurally.\n\nProfessional assembly gets it right the first time: instructions followed in sequence, hardware sorted and identified before starting, panels assembled in the correct orientation, and cam locks tightened to the right torque. The result is furniture that operates smoothly and safely for its full intended service life.",
    "signs": [
        "Large or complex multi-box furniture has just been delivered",
        "Previous self-assembly attempts have resulted in misaligned doors, stuck drawers, or wobbly frames",
        "The furniture requires wall anchoring with an anti-tip bracket — a safety requirement for wardrobes, bookcases, and dressers",
    ],
    "steps": [
        ("Inventory and sort", "All parts and hardware are inventoried against the parts list before assembly begins — missing parts are identified before you are midway through the build."),
        ("Sequential assembly", "Instructions are followed in the specified sequence to prevent the common mistake of discovering a reversed panel after 40 steps have been completed."),
        ("Hardware torque", "Cam locks and bolts are tightened to the correct torque — hand-tight plus a quarter turn — not over-tightened, which strips threads and splits panels."),
        ("Anti-tip anchoring", "Wardrobes, dressers, and bookcases are anchored to the wall stud with the included anti-tip strap as a mandatory safety step."),
    ],
    "benefits": [
        ("Correct assembly first time", "Professional assembly avoids the reverse-engineering required when panels go in backward — the most common and time-consuming flat-pack mistake."),
        ("Safe anti-tip anchoring", "Wardrobes and tall furniture tipping is a leading cause of child injury. Anti-tip brackets installed into studs prevent this."),
        ("Time savings", "A bedroom set that takes an average DIY assembler 6–8 hours takes a professional 2–3 hours. Your day stays intact."),
    ],
    "price": "Furniture assembly typically costs $75–$200 per piece depending on complexity. Bedroom sets and full-wall storage systems requiring multiple boxes are quoted based on item count.",
},

"attic-ladder-replacement": {
    "intro": "An attic ladder that wobbles, sticks, or fails to fully extend is more than an inconvenience — it's a fall hazard. Attic ladders carry a duty rating (typically 225–375 pounds) that accounts for the person plus whatever they're carrying. A ladder with cracked rails, broken spring mechanisms, or a deteriorated hinge assembly can fail under load.\n\nReplacement also provides an energy-efficiency opportunity. Original attic ladders in homes built before 2000 are almost always uninsulated — a direct air path between conditioned living space and the unconditioned attic. Modern replacement ladders include foam-sealed hatches and insulated covers that dramatically reduce heat loss through this often-ignored air pathway.",
    "signs": [
        "The ladder wobbles sideways when in use or the steps flex under normal body weight",
        "The spring mechanism has broken or weakened so the ladder no longer stays closed or opens smoothly",
        "You can feel cold air coming down through the attic hatch in winter",
    ],
    "steps": [
        ("Old ladder removal", "The existing ladder and hatch frame are removed. We inspect the rough opening for any rot, damage, or framing that needs attention."),
        ("Rough opening adjustment", "If the new ladder requires a different rough opening size, we trim or frame as needed."),
        ("New ladder installation", "The new ladder is set into the opening, shimmed level and plumb, and fastened to the surrounding framing."),
        ("Insulation gasket and testing", "The hatch is sealed with the foam gasket supplied with the unit and tested through multiple open-close cycles."),
    ],
    "benefits": [
        ("Structural safety", "A new ladder rated to current standards provides a safe, non-wobbling path to the attic under the full rated load."),
        ("Energy savings", "An insulated, foam-gasketed attic hatch dramatically reduces air infiltration through one of the home's largest uninsulated air bypasses."),
        ("Smooth operation", "New spring mechanisms open and retract the ladder fully and smoothly — eliminating the wrestling match that old worn springs require."),
    ],
    "price": "Attic ladder replacement typically costs $250–$500 in labor. The ladder unit itself typically runs $150–$350 for a quality aluminum model.",
},

"mailbox-post-installation": {
    "intro": "A leaning mailbox post is a slow-motion project that most homeowners notice for years before doing anything about it. The causes are almost always the same: a post set without sufficient concrete footing that has loosened over years of wind loading, or a wood post that has rotted at the ground line. Neither problem resolves itself, and a mailbox that doesn't meet USPS height specifications (41–45 inches to the mailbox floor) can result in mail service disruption.\n\nNew mailbox and post installation is also a curb appeal upgrade. A properly set post with the mailbox at the correct height, plumb and aligned with the property line, makes an immediate positive impression. We handle everything from hole digging to concrete pouring to final alignment.",
    "signs": [
        "The post is leaning and does not return to plumb when pushed",
        "The existing wood post is visibly rotted at ground level",
        "The mailbox itself is damaged, rusted, or too small for current package volume",
    ],
    "steps": [
        ("Old post removal", "The existing post and any remaining concrete footing are removed and the hole cleared."),
        ("New hole and footing", "A new hole 24 inches deep is dug, the post set plumb at the correct height, and concrete poured and tamped around the base."),
        ("Cure time", "The concrete is allowed to cure for 24 hours before the post is put under load — we brace the post during this time."),
        ("Mailbox mounting", "The mailbox is mounted at the correct height (41–45 inches to floor) and aligned with the road."),
    ],
    "benefits": [
        ("Permanent stability", "A concrete-footed post does not lean — it holds its position against wind loading and vehicle turbulence for 10+ years."),
        ("USPS compliance", "Correct height and setback ensures uninterrupted mail delivery — carriers are not required to deliver to non-compliant installations."),
        ("Curb appeal", "A plumb, clean mailbox installation is a small but visible improvement to the front of any home."),
    ],
    "price": "Mailbox and post installation typically costs $150–$350 depending on access, post type, and whether the mailbox is customer-supplied or sourced.",
},

"roof-leak-repair": {
    "intro": "A roof leak is one of the most urgent home repair situations because every additional rain event extends the damage deeper into the structure. Water that enters at the roof travels along rafters, saturates insulation, and eventually appears on ceilings — often far from the actual entry point. The ceiling stain you see may be 6 feet from the actual leak source.\n\nMost roof leaks originate not from the field of the shingles but from failure at specific weak points: flashing around chimneys, skylights, and vents; deteriorated pipe boot collars; or lifted shingles at edges and ridges. These are targeted repairs — not roof replacements — and addressing them promptly prevents the far more expensive damage that follows from delayed repair.",
    "signs": [
        "Water stains appear on ceilings or walls, particularly after rain",
        "Daylight is visible through the attic roof deck",
        "Shingles are missing, curled, or visibly cracked near the roof edge or around any roof penetration",
    ],
    "steps": [
        ("Interior and exterior inspection", "We trace the path from the ceiling stain to the roof to identify the actual entry point — stains migrate, so the visible damage point is not always directly above the source."),
        ("Source identification", "Common sources — flashing, pipe boots, ridge caps, or individual damaged shingles — are inspected and the specific failure point identified."),
        ("Targeted repair", "Flashing is re-sealed or replaced; pipe boot collars are replaced; damaged shingles are swapped out individually."),
        ("Water test", "A water test with a garden hose confirms the repair has eliminated the entry point before we leave."),
    ],
    "benefits": [
        ("Damage containment", "Fixing a roof leak promptly stops water infiltration that would otherwise continue saturating insulation, rotting sheathing, and spreading ceiling damage."),
        ("Targeted cost", "Repairing the specific failure point — rather than replacing the entire roof — costs a fraction of a full replacement while providing a complete fix."),
        ("Documented repair", "A written description of the repair location and method is valuable for insurance purposes and future reference."),
    ],
    "price": "Roof leak repair typically costs $200–$600 depending on the access difficulty, repair scope, and whether flashing replacement is required. Emergency same-day service is available.",
},

"fascia-repair": {
    "intro": "Fascia boards run along the lower edge of the roof, capping the rafter tails and providing the mounting surface for gutters. They are exposed to more moisture than almost any other exterior wood component — gutters overflow onto them, ice dams push against them, and they sit in the shadow of the roof overhang where they stay damp long after rain.\n\nRotted fascia boards are not just cosmetic — they compromise the attachment point for gutters, which can then pull away from the house, and in advanced cases can allow water and pests to access the rafter bay. Repair or replacement at the first sign of softness prevents significantly more expensive structural repairs later.",
    "signs": [
        "The fascia board feels soft when pressed — a sign of active rot",
        "Paint is peeling from the fascia in patches, particularly near gutter hangers",
        "Gutters are pulling away from the house or sitting at an angle",
    ],
    "steps": [
        ("Scope assessment", "We determine the extent of rot — whether it affects only the fascia board or has spread to the sub-fascia or rafter tails."),
        ("Gutter removal", "Gutters in the affected section are carefully removed and set aside for re-mounting after repair."),
        ("Damaged board removal and replacement", "The rotted section is cut out, any underlying damage is treated or repaired, and new primed fascia board is cut, fitted, and fastened."),
        ("Caulk, prime, and paint", "All seams and nail holes are caulked, and the new board is primed and painted to match the existing fascia."),
    ],
    "benefits": [
        ("Gutter support restoration", "New fascia provides a solid attachment point for gutters — preventing the sagging and separation that allows water to fall directly against the foundation."),
        ("Pest exclusion", "A solid, intact fascia board closes off the gap that rotted wood creates between the roof and the exterior — an access point for wasps, carpenter bees, and squirrels."),
        ("Early intervention savings", "Replacing a $200 fascia board today prevents the $1,500–$3,000 rafter tail and roof deck repair that active rot eventually creates."),
    ],
    "price": "Fascia repair typically costs $150–$450 per section depending on length and whether sub-fascia or rafter repair is also needed. Paint matching is included.",
},

"gutter-repair-cleaning": {
    "intro": "Gutters have one job: carry rainwater from the roof edge to downspouts and away from the foundation. When they fail at this job — because they are clogged with debris, have sagged out of pitch, or have open seams — the consequences are predictable and expensive: foundation water infiltration, basement flooding, wood rot at the fascia and soffits, and in cold climates, ice dams.\n\nAnnual gutter cleaning is the single most cost-effective home maintenance task. A gutter cleaning that costs $150–$300 prevents the foundation drainage problems that cost thousands to remediate. Gutter repairs — re-pitching sagging sections, resealing open joints, replacing damaged hangers — restore function and extend gutter life significantly.",
    "signs": [
        "Water pours over the front of gutters during rain rather than flowing to downspouts",
        "Gutters are visibly sagging in sections, creating a low point where debris accumulates",
        "Foundation areas are consistently damp after rain even without visible ground saturation",
    ],
    "steps": [
        ("Full gutter cleaning", "All debris is removed from every gutter run — debris bags are used, not blowing material onto the roof or landscape."),
        ("Downspout clearing", "Downspouts are flushed with water to confirm they are clear from top to bottom."),
        ("Pitch correction", "Sections that have sagged out of proper pitch (1/4 inch per 10 feet toward downspout) are re-hung at the correct angle."),
        ("Seam resealing", "Open or leaking seams and joints are cleaned and resealed with gutter sealant from the inside."),
    ],
    "benefits": [
        ("Foundation protection", "Functioning gutters direct roof runoff away from the foundation — the primary defense against basement moisture and foundation movement."),
        ("Wood rot prevention", "Overflowing gutters saturate fascia boards and soffits, causing rot that progressively damages roof edge structure. Clean, flowing gutters prevent this."),
        ("Ice dam reduction", "In cold climates, debris-clogged gutters contribute to ice dam formation by trapping standing water that freezes at the roof edge."),
    ],
    "price": "Gutter cleaning typically costs $150–$350 depending on linear footage and debris volume. Gutter repair (re-pitching, seam sealing) adds $100–$250 depending on the extent of work needed.",
},

"fence-repair-installation": {
    "intro": "A fence defines property lines, provides privacy, contains pets and children, and contributes significantly to the visual character of a property. Posts that lean, panels that sag, and gates that won't latch are not just cosmetic problems — they undermine the fence's functional purpose and, left unrepaired, progressively worsen as water and frost continue to work on loose footings.\n\nMost fence failures originate at the post: wood posts rot at the ground line, and even treated lumber has a finite service life in direct soil contact. Post replacement with concrete footings is more labor-intensive than simply tamping a new post back in, but it produces a repair that lasts 15–20 years rather than 2–3.",
    "signs": [
        "Posts are visibly leaning and do not return to plumb under hand pressure",
        "Panel boards have cracked, warped, or pulled free from rails",
        "The gate no longer latches or drags on the ground",
    ],
    "steps": [
        ("Post assessment", "Each leaning or damaged post is assessed for rot depth. Posts rotted at grade are replaced; posts with surface rot but sound cores can be repaired."),
        ("Post reset or replacement", "Rotted posts are removed along with old concrete, and new posts are set in fresh concrete footings at the correct depth (1/3 of post height in ground)."),
        ("Panel and rail repair", "Damaged panels, rails, and pickets are replaced with matching material — pressure-treated where it contacts the ground, cedar or matching species for above-grade sections."),
        ("Gate adjustment", "Gate hardware is adjusted or replaced for correct operation — proper latch engagement and zero drag on the ground."),
    ],
    "benefits": [
        ("Post stability", "Concrete-footed posts hold plumb against frost heave, wind loading, and lateral pressure — the most common cause of fence failure is inadequately footed posts."),
        ("Pet and child containment", "A fence with gaps, loose panels, or non-latching gates doesn't contain pets or children — repair restores the fence's core function."),
        ("Extended fence life", "Addressing post and rail failures early extends the remaining fence life significantly, deferring the cost of full replacement."),
    ],
    "price": "Fence repair typically costs $200–$600 per section depending on post count, material, and extent of damage. New fence installation is quoted based on linear footage, style, and material.",
},

}  # end SERVICE_CONTENT
