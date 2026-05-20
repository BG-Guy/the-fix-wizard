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
