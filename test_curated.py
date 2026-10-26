import re

card_data = [
    {
        "id": "funky-twist",
        "index": "01",
        "title": "Funky Twist",
        "subtitle": "Creative Laboratory",
        "badge": "108™",
        "category": "A LAB FOR THE UNCONVENTIONAL",
        "headline": "For ideas that refuse to stay inside the lines.",
        "desc": "An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.",
        "gradient": "linear-gradient(175deg, #18100b 0%, #2a1910 32%, #824722 65%, #c07742 85%, #b46833 100%)",
        "sceneId": "scene-starry",
        "modalId": "homeModal"
    },
    {
        "id": "floating-studio",
        "index": "02",
        "title": "Floating Studio",
        "subtitle": "Workshops & Atelier",
        "badge": "108™",
        "category": "CLASSES & SPECIAL WORKSHOPS",
        "headline": "Weekly classes, adult workshops, and open atelier in Carmel.",
        "desc": "Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process-based discovery across ceramics, printmaking, and glaze.",
        "gradient": "linear-gradient(175deg, #180c12 0%, #351622 32%, #8e3f4e 65%, #cf6c6c 85%, #d48270 100%)",
        "sceneId": "scene-classroom",
        "modalId": "classesModal"
    },
    {
        "id": "color-magic",
        "index": "03",
        "title": "Color Magic",
        "subtitle": "Celebrations & Joy",
        "badge": "108™",
        "category": "UNFORGETTABLE CELEBRATIONS",
        "headline": "Vibrant art parties dipped in joy, clay sculpting, and confetti.",
        "desc": "Celebrate your milestone with personalized painting, tactile clay sculpting, and guided mess-making where every guest creates a keepsake.",
        "gradient": "linear-gradient(175deg, #140718 0%, #2e0f39 32%, #822b82 65%, #c64fa8 85%, #e06fa6 100%)",
        "sceneId": "scene-birthday",
        "modalId": "classesModal"
    },
    {
        "id": "cloud-vision",
        "index": "04",
        "title": "Cloud Vision",
        "subtitle": "Retreats & Innovation",
        "badge": "108™",
        "category": "COLLABORATIVE RETREATS",
        "headline": "Inspiring collaborative workshops and vision sessions in the clouds.",
        "desc": "Energize your organization with collaborative creative challenges designed to unlock breakthrough thinking, strategic clarity, and team synergy.",
        "gradient": "linear-gradient(175deg, #070e1b 0%, #0f223f 32%, #225596 65%, #3d88cf 85%, #5aa5e6 100%)",
        "sceneId": "scene-presentation",
        "modalId": "foundationModal"
    },
    {
        "id": "garden-twilight",
        "index": "05",
        "title": "Garden Twilight",
        "subtitle": "Private Gatherings",
        "badge": "108™",
        "category": "PRIVATE PARTIES & GATHERINGS",
        "headline": "Intimate celebratory gatherings under sunlit canopies and twilight.",
        "desc": "Tailored private evenings featuring guided art projects, lush floral settings, live music, and warm hospitality for your closest friends and family.",
        "gradient": "linear-gradient(175deg, #09120c 0%, #172719 32%, #4e6328 65%, #9fa13c 85%, #d8b248 100%)",
        "sceneId": "scene-party",
        "modalId": "donateModal"
    }
]

print("Card data valid, count:", len(card_data))
