"""
AgroScan — Comprehensive Plant Pathology Database (42 Classes)
Includes all 38 PlantVillage benchmark classes + 4 staple Indian crop diseases (Rice/Paddy, Cotton, Sugarcane).
Bilingual: English (en) & Tamil (ta)
Stored and indexed in SQLite (`diseases` table).
"""

DISEASES = {
    # ══════════════════════════════════════════════
    # APPLE (4 Classes)
    # ══════════════════════════════════════════════
    "Apple___Apple_scab": {
        "crop": "Apple",
        "en": {
            "name": "Apple Scab",
            "cause": "Fungus Venturia inaequalis",
            "symptoms": "Olive-green to velvety black lesions on leaves, blossoms, and fruit. Leaves may twist and drop prematurely.",
            "immediate": "Rake and destroy fallen infected leaves immediately. Prune canopy to increase sunlight and airflow.",
            "organic": "Spray wettable sulfur (3g/L) or neem oil (5ml/L) with potassium soap every 7–10 days during wet spring weather.",
            "chemical": "Apply Captan 50% WP (2g/L) or Mancozeb 75% WP (2.5g/L) from green-tip stage every 10 days.",
            "prevention": "Plant scab-resistant cultivars, avoid overhead sprinkler irrigation, and apply autumn urea spray (5%) to speed leaf decomposition.",
            "weather": "Cool, wet spring weather (16–24°C) with continuous leaf wetness > 9 hours.",
            "recovery": "14–21 days for new foliage protection",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍎"
        },
        "ta": {
            "name": "ஆப்பிள் சொறி நோய் (Apple Scab)",
            "cause": "Venturia inaequalis பூஞ்சை",
            "symptoms": "இலைகள் மற்றும் பழங்களில் ஆலிவ்-பச்சை முதல் கருப்பு நிற வெல்வெட் புள்ளிகள் தோன்றும். இலைகள் சுருண்டு உதிரும்.",
            "immediate": "உதிர்ந்த பாதிக்கப்பட்ட இலைகளை சேகரித்து அழிக்கவும். காற்றோட்டத்திற்கு கிளைகளை கவாத்து செய்யவும்.",
            "organic": "நனையும் கந்தகம் (3 கிராம்/லி) அல்லது வேப்பெண்ணெய் (5 மி.லி/லி) 7-10 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "chemical": "Mancozeb 75% WP (2.5 கிராம்/லி) அல்லது Captan (2 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "நோய் எதிர்ப்பு சக்தி கொண்ட ரகங்களை நடவும்; மேல்வழி நீர்ப்பாசனத்தை தவிர்க்கவும்.",
            "weather": "குளிர்ந்த மற்றும் ஈரப்பதமான வானிலை (16–24°C).",
            "recovery": "14–21 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍎"
        }
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "en": {
            "name": "Apple Black Rot",
            "cause": "Fungus Botryosphaeria obtusa",
            "symptoms": "Circular 'frog-eye' leaf spots with purple margins and tan centers; black mummified fruit and sunken limb cankers.",
            "immediate": "Prune out dead wood, fire-blighted twigs, and remove all mummified fruit hanging on trees.",
            "organic": "Apply Bordeaux mixture (1%) or copper oxychloride spray during dormant and early bud stages.",
            "chemical": "Spray Thiophanate-methyl 70% WP (1g/L) or Captan (2g/L) from petal fall every 10–14 days.",
            "prevention": "Maintain tree vigor, sanitize pruning shears with 70% alcohol, and clear orchard floor debris.",
            "weather": "Warm, humid rains (24–29°C) favor spore release.",
            "recovery": "21–30 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍎"
        },
        "ta": {
            "name": "ஆப்பிள் கருப்பு அழுகல் (Black Rot)",
            "cause": "Botryosphaeria obtusa பூஞ்சை",
            "symptoms": "இலைகளில் ஊதா விளிம்புடன் கூடிய வட்ட வடிவ பழுப்பு புள்ளிகள்; பழங்கள் கருப்பாகி சுருங்கிவிடும்.",
            "immediate": "காய்ந்த கிளைகள் மற்றும் மரத்தில் தொங்கும் அழுகிய பழங்களை உடனடியாக அகற்றவும்.",
            "organic": "போர்டோ கலவை (1%) அல்லது செம்பு ஆக்சிகுளோரைடு தெளிக்கவும்.",
            "chemical": "Thiophanate-methyl (1 கிராம்/லி) அல்லது Captan (2 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "கவாத்து கருவிகளை கிருமி நீக்கம் செய்யவும்; தோட்டத்தை சுத்தமாக வைத்திருக்கவும்.",
            "weather": "வெப்பமான மற்றும் ஈரப்பதமான மழைக்காலம் (24–29°C).",
            "recovery": "21–30 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍎"
        }
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "en": {
            "name": "Cedar Apple Rust",
            "cause": "Fungus Gymnosporangium juniperi-virginianae",
            "symptoms": "Bright yellow-orange spots on upper leaf surfaces with tiny black dots; tube-like projections underneath.",
            "immediate": "Inspect and remove gelatinous orange galls from nearby juniper/cedar windbreaks within 300m.",
            "organic": "Spray liquid copper soap or sulfur suspension weekly from pink bud through early summer.",
            "chemical": "Apply Myclobutanil 10% WP (1g/L) or Propiconazole (1ml/L) at 7–10 day intervals.",
            "prevention": "Avoid planting eastern red cedar near apple orchards; select rust-resistant cultivars.",
            "weather": "Spring rains at 13–24°C carry windborne spores.",
            "recovery": "14–20 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍎"
        },
        "ta": {
            "name": "சிடார் ஆப்பிள் துரு (Cedar Rust)",
            "cause": "Gymnosporangium பூஞ்சை",
            "symptoms": "இலைகளின் மேற்பகுதியில் பிரகாசமான ஆரஞ்சு-மஞ்சள் புள்ளிகள் தோன்றும்.",
            "immediate": "அருகிலுள்ள சிடார் மரங்களில் உள்ள பூஞ்சை முடிச்சுகளை அகற்றவும்.",
            "organic": "கந்தகம் அல்லது செம்பு சோப்பு கரைசலை வாரந்தோறும் தெளிக்கவும்.",
            "chemical": "Myclobutanil 10% WP (1 கிராம்/லி) 7-10 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "prevention": "துரு நோய் எதிர்ப்பு ஆப்பிள் ரகங்களை தேர்வு செய்யவும்.",
            "weather": "வசந்த கால மழை (13–24°C).",
            "recovery": "14–20 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍎"
        }
    },
    "Apple___healthy": {
        "crop": "Apple",
        "en": {
            "name": "Healthy Apple Leaf",
            "cause": "No pathogen detected — Optimal physiology",
            "symptoms": "Vibrant, uniform green lamina with intact cuticles, strong venation, and zero necrotic lesions.",
            "immediate": "No corrective action needed. Continue routine weekly scouting.",
            "organic": "Apply compost mulch and foliar seaweed extract (2ml/L) once a month for micronutrient resilience.",
            "chemical": "None required.",
            "prevention": "Maintain balanced pruning, drip irrigation, and orchard sanitation.",
            "weather": "All normal growing conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍎"
        },
        "ta": {
            "name": "ஆரோக்கியமான ஆப்பிள் இலை",
            "cause": "நோய் எதுவும் இல்லை — சிறந்த ஆரோக்கியம்",
            "symptoms": "எந்த புள்ளிகளும் இன்றி பிரகாசமான பச்சை நிறத்தில் ஆரோக்கியமாக உள்ளது.",
            "immediate": "எந்த நடவடிக்கையும் தேவையில்லை. வழக்கமான கண்காணிப்பை தொடரவும்.",
            "organic": "மாதம் ஒருமுறை கடற்பாசி திரவ உரம் (2 மி.லி/லி) அளிக்கலாம்.",
            "chemical": "தேவையில்லை.",
            "prevention": "சீரான நீர்ப்பாசனம் மற்றும் கவாத்து பராமரிப்பு.",
            "weather": "சாதாரண வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍎"
        }
    },

    # ══════════════════════════════════════════════
    # BLUEBERRY & CHERRY (3 Classes)
    # ══════════════════════════════════════════════
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "en": {
            "name": "Healthy Blueberry Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Glossy, dark-green elliptical leaves showing proper acidic soil nutrition (pH 4.5–5.5).",
            "immediate": "No treatment needed.",
            "organic": "Mulch with pine needles or sawdust to maintain acidic root zone.",
            "chemical": "None required.",
            "prevention": "Monitor soil pH and avoid waterlogging.",
            "weather": "Temperate sunny conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🫐"
        },
        "ta": {
            "name": "ஆரோக்கியமான அவுரிநெல்லி இலை (Blueberry)",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "பளபளப்பான அடர் பச்சை இலைகள்.",
            "immediate": "சிகிச்சை தேவையில்லை.",
            "organic": "மண்ணின் அமிலத்தன்மையை (pH 4.5–5.5) பராமரிக்கவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "சீரான வடிகால் வசதியை உறுதி செய்யவும்.",
            "weather": "சாதாரண வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🫐"
        }
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "en": {
            "name": "Cherry Powdery Mildew",
            "cause": "Fungus Podosphaera clandestina",
            "symptoms": "White talcum-like powdery fungal growth on young leaves; leaves curl upward and shoots become stunted.",
            "immediate": "Prune affected water sprouts and crowded inner branches to lower humidity.",
            "organic": "Spray potassium bicarbonate (5g/L) or neem oil (5ml/L) every 7 days.",
            "chemical": "Apply Wettable Sulfur 80% WP (2g/L) or Hexaconazole 5% EC (1ml/L).",
            "prevention": "Avoid excess nitrogen fertilizer which promotes soft susceptible shoot growth.",
            "weather": "Warm dry days (20–28°C) with high night humidity (>75%).",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍒"
        },
        "ta": {
            "name": "செர்ரி சாம்பல் நோய் (Powdery Mildew)",
            "cause": "Podosphaera clandestina பூஞ்சை",
            "symptoms": "இளம் இலைகளில் வெள்ளை மாவு போன்ற பூஞ்சை படலம்; இலைகள் மேல்நோக்கி சுருளும்.",
            "immediate": "பாதிக்கப்பட்ட தளிர்களை கவாத்து செய்து காற்றோட்டத்தை அதிகரிக்கவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது பொட்டாசியம் பைகார்பனேட் (5 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "நனையும் கந்தகம் 80% WP (2 கிராம்/லி) அல்லது Hexaconazole (1 மி.லி/லி).",
            "prevention": "அதிகப்படியான தழைச்சத்து (Nitrogen) உரத்தை தவிர்க்கவும்.",
            "weather": "வறண்ட பகல் மற்றும் ஈரப்பதமான இரவு (20–28°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍒"
        }
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "en": {
            "name": "Healthy Cherry Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Clean serrated green leaves with healthy petioles and no powdery coating.",
            "immediate": "No action required.",
            "organic": "Apply vermicompost around drip line in spring.",
            "chemical": "None required.",
            "prevention": "Keep orchard floor clean and well-drained.",
            "weather": "Normal growing conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍒"
        },
        "ta": {
            "name": "ஆரோக்கியமான செர்ரி இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "சுத்தமான பச்சை இலைகள்; எவ்வித பூஞ்சை படலமும் இல்லை.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "மண்புழு உரம் இட்டு பராமரிக்கவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "நல்ல வடிகால் வசதியை பராமரிக்கவும்.",
            "weather": "சாதாரண வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍒"
        }
    },

    # ══════════════════════════════════════════════
    # CORN / MAIZE (4 Classes)
    # ══════════════════════════════════════════════
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn",
        "en": {
            "name": "Corn Gray Leaf Spot",
            "cause": "Fungus Cercospora zeae-maydis",
            "symptoms": "Rectangular, tan-to-gray necrotic lesions bounded sharply by leaf veins.",
            "immediate": "Remove heavily blighted lower leaves if small plot; monitor ear leaf closely.",
            "organic": "Apply Trichoderma viride foliar bio-spray (5g/L) and rotate out of maize for 1–2 years.",
            "chemical": "Spray Azoxystrobin + Tebuconazole (1ml/L) or Propiconazole 25% EC (1ml/L) at tasseling.",
            "prevention": "Deep plow crop residue after harvest; plant resistant hybrids.",
            "weather": "Prolonged warm, foggy/humid weather (22–30°C, >90% RH).",
            "recovery": "14–21 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌽"
        },
        "ta": {
            "name": "மக்காச்சோள சாம்பல் இலைப்புள்ளி (Gray Leaf Spot)",
            "cause": "Cercospora zeae-maydis பூஞ்சை",
            "symptoms": "இலை நரம்புகளுக்கு இடையே செவ்வக வடிவ சாம்பல்-பழுப்பு நிற புண்கள் தோன்றும்.",
            "immediate": "கடுமையாக பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றவும்.",
            "organic": "டிரைக்கோடெர்மா விரிடி (5 கிராம்/லி) தெளிக்கவும்; பயிர் சுழற்சி செய்யவும்.",
            "chemical": "Propiconazole 25% EC (1 மி.லி/லி) அல்லது Azoxystrobin தெளிக்கவும்.",
            "prevention": "அறுவடைக்குப் பின் ஆழ உழவு செய்யவும்; எதிர்ப்பு ரகங்களை பயிரிடவும்.",
            "weather": "வெப்பமான மற்றும் அதிக ஈரப்பதம் (22–30°C, >90% RH).",
            "recovery": "14–21 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌽"
        }
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn",
        "en": {
            "name": "Corn Common Rust",
            "cause": "Fungus Puccinia sorghi",
            "symptoms": "Small, oval, cinnamon-brown powdery pustules scattered on both upper and lower leaf surfaces.",
            "immediate": "Scout fields weekly; treat immediately if pustules appear before silking.",
            "organic": "Spray neem oil (5ml/L) or wettable sulfur (3g/L) at early pustule appearance.",
            "chemical": "Apply Mancozeb 75% WP (2.5g/L) or Propiconazole 25% EC (1ml/L).",
            "prevention": "Plant early in the season and eradicate oxalis weeds (alternate host) around field borders.",
            "weather": "Cool to moderate temperatures (16–23°C) with heavy morning dew.",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌽"
        },
        "ta": {
            "name": "மக்காச்சோள துரு நோய் (Common Rust)",
            "cause": "Puccinia sorghi பூஞ்சை",
            "symptoms": "இலையின் இரு புறங்களிலும் செம்பழுப்பு நிற கொப்புளங்கள் தோன்றும்.",
            "immediate": "வயலை தொடர்ந்து கண்காணித்து ஆரம்ப நிலையிலேயே மருந்து தெளிக்கவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது நனையும் கந்தகம் (3 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "Mancozeb (2.5 கிராம்/லி) அல்லது Propiconazole (1 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "வரப்புகளில் உள்ள புளிச்ச கீரை (Oxalis) களைகளை அகற்றவும்.",
            "weather": "குளிர்ந்த காற்று மற்றும் பனிப்பொழிவு (16–23°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌽"
        }
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn",
        "en": {
            "name": "Northern Corn Leaf Blight",
            "cause": "Fungus Exserohilum turcicum",
            "symptoms": "Large, cigar-shaped gray-green to tan lesions (3–15 cm long) starting on lower leaves.",
            "immediate": "Ensure adequate potassium nutrition; apply fungicide if lesions reach the ear leaf.",
            "organic": "Foliar spray of Pseudomonas fluorescens (10g/L) every 10 days.",
            "chemical": "Spray Mancozeb 75% WP (2.5g/L) or Zineb (2g/L) in 500L water/ha.",
            "prevention": "Use Ht-gene resistant hybrids and practice 1-year crop rotation with legumes.",
            "weather": "Moderate temperatures (18–27°C) with heavy dew or rain.",
            "recovery": "14–18 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌽"
        },
        "ta": {
            "name": "மக்காச்சோள இலைக் கருகல் (Northern Leaf Blight)",
            "cause": "Exserohilum turcicum பூஞ்சை",
            "symptoms": "கீழ் இலைகளில் சுருட்டு வடிவ நீண்ட சாம்பல்-பழுப்பு நிற புண்கள் (3–15 செ.மீ) தோன்றும்.",
            "immediate": "பोटाஷ் சத்து குறைபாடு இல்லாமல் பார்த்துக்கொள்ளவும்; உடனடியாக பூஞ்சைக் கொல்லி தெளிக்கவும்.",
            "organic": "சூடோமோனாஸ் புளோரசன்ஸ் (10 கிராம்/லி) 10 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "chemical": "Mancozeb 75% WP (2.5 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "பயறு வகைப் பயிர்களுடன் பயிர் சுழற்சி செய்யவும்.",
            "weather": "மிதமான வெப்பநிலை மற்றும் மழை (18–27°C).",
            "recovery": "14–18 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌽"
        }
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn",
        "en": {
            "name": "Healthy Corn Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Broad, arch-shaped dark green leaf blades with strong midrib and high photosynthetic vigor.",
            "immediate": "No action required.",
            "organic": "Side-dress with vermicompost or Jeevamrutham during knee-high stage.",
            "chemical": "None required.",
            "prevention": "Maintain weed-free inter-rows and timely irrigation at tasseling.",
            "weather": "Warm sunny conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌽"
        },
        "ta": {
            "name": "ஆரோக்கியமான மக்காச்சோள இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "அடர் பச்சை நிறத்தில் உறுதியான நடு நரம்புடன் ஆரோக்கியமாக உள்ளது.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "ஜீவாமிர்தம் அல்லது மண்புழு உரம் இடவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "களை நிர்வாகம் மற்றும் பூக்கும் பருவத்தில் சீரான நீர்ப்பாசனம்.",
            "weather": "சூரிய ஒளி நிறைந்த வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌽"
        }
    },

    # ══════════════════════════════════════════════
    # GRAPE (4 Classes)
    # ══════════════════════════════════════════════
    "Grape___Black_rot": {
        "crop": "Grape",
        "en": {
            "name": "Grape Black Rot",
            "cause": "Fungus Guignardia bidwellii",
            "symptoms": "Reddish-brown circular foliar spots with dark borders; berries shrivel into hard black mummies.",
            "immediate": "Remove and burn all mummified clusters and infected tendrils during pruning.",
            "organic": "Spray Bordeaux mixture (1%) or copper hydroxide at new shoot emergence.",
            "chemical": "Apply Myclobutanil (1g/L) or Mancozeb (2.5g/L) pre-bloom and post-bloom.",
            "prevention": "Open canopy training for rapid drying after rain; cultivate soil before bud break.",
            "weather": "Warm wet spells (21–27°C) during bloom and early fruit set.",
            "recovery": "14–21 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍇"
        },
        "ta": {
            "name": "திராட்சை கருப்பு அழுகல் (Black Rot)",
            "cause": "Guignardia bidwellii பூஞ்சை",
            "symptoms": "இலைகளில் கருப்பு விளிம்புடன் கூடிய செம்பழுப்பு புள்ளிகள்; பழங்கள் கருப்பாக சுருங்கிவிடும்.",
            "immediate": "பாதிக்கப்பட்ட பழக்கொத்துகள் மற்றும் கொடிகளை அகற்றி எரிக்கவும்.",
            "organic": "போர்டோ கலவை (1%) தெளிக்கவும்.",
            "chemical": "Mancozeb (2.5 கிராம்/லி) அல்லது Myclobutanil (1 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "பந்தலில் நல்ல காற்றோட்டம் மற்றும் சூரிய ஒளி படுமாறு கவாத்து செய்யவும்.",
            "weather": "ஈரப்பதமான வெப்ப வானிலை (21–27°C).",
            "recovery": "14–21 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍇"
        }
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "en": {
            "name": "Grape Esca (Black Measles)",
            "cause": "Fungal complex Phaeomoniella chlamydospora & Phaeoacremonium",
            "symptoms": "Interveinal 'tiger-stripe' chlorosis and necrosis on leaves; dark purple-black spots on berry skin.",
            "immediate": "Mark infected vines; prune during dry weather only and seal large pruning wounds immediately.",
            "organic": "Apply Trichoderma harzianum paste on pruning wounds to block fungal entry.",
            "chemical": "Paint pruning cuts with Carbendazim 50% WP paste or copper oxychloride slurry.",
            "prevention": "Remove dead cordons and trunks; disinfect saws between vines.",
            "weather": "Alternating wet spring and hot summer heatwaves.",
            "recovery": "Chronic vascular management (30+ days)",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍇"
        },
        "ta": {
            "name": "திராட்சை எஸ்கா / வரி நோய் (Black Measles)",
            "cause": "Phaeomoniella பூஞ்சை கூட்டு",
            "symptoms": "இலைகளில் புலி வரிகள் போன்ற மஞ்சள் மற்றும் பழுப்பு நிற கோடுகள்; பழங்களில் கருப்பு புள்ளிகள்.",
            "immediate": "பாதிக்கப்பட்ட கொடிகளை அடையாளம் கண்டு வறண்ட காலத்தில் மட்டும் கவாத்து செய்யவும்.",
            "organic": "கவாத்து வெட்டுகளில் டிரைக்கோடெர்மா பசை தடவவும்.",
            "chemical": "Carbendazim 50% WP அல்லது செம்பு ஆக்சிகுளோரைடு பசையை வெட்டுப் பகுதிகளில் தடவவும்.",
            "prevention": "கவாத்து கத்திகளை கிருமி நீக்கம் செய்யவும்; காய்ந்த தண்டுகளை அகற்றவும்.",
            "weather": "மழைக்குப் பின் வரும் கடும் வெயில் காலம்.",
            "recovery": "30 நாட்களுக்கு மேல் (தொடர் பராமரிப்பு)",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍇"
        }
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "en": {
            "name": "Grape Isariopsis Leaf Blight",
            "cause": "Fungus Pseudocercospora vitis",
            "symptoms": "Irregular dark-brown to reddish patches on older leaves leading to premature defoliation.",
            "immediate": "Collect and burn fallen leaves; thin out dense foliage.",
            "organic": "Spray neem oil (5ml/L) or copper oxychloride (2.5g/L).",
            "chemical": "Apply Chlorothalonil (2g/L) or Carbendazim + Mancozeb (2g/L).",
            "prevention": "Ensure balanced potassium nutrition and proper trellis drainage.",
            "weather": "Late season high humidity and warm rains.",
            "recovery": "14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍇"
        },
        "ta": {
            "name": "திராட்சை இலைக் கருகல் (Isariopsis Leaf Blight)",
            "cause": "Pseudocercospora vitis பூஞ்சை",
            "symptoms": "முதிர்ந்த இலைகளில் ஒழுங்கற்ற கரும்பழுப்பு புள்ளிகள் தோன்றி இலைகள் உதிரும்.",
            "immediate": "உதிர்ந்த இலைகளை அகற்றி எரிக்கவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது செம்பு ஆக்சிகுளோரைடு தெளிக்கவும்.",
            "chemical": "Chlorothalonil (2 கிராம்/லி) அல்லது Mancozeb தெளிக்கவும்.",
            "prevention": "சீரான பொட்டாஷ் உரமிடுதல் மற்றும் வடிகால் வசதி.",
            "weather": "அதிக ஈரப்பதம் மற்றும் மழைக்காலம்.",
            "recovery": "14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍇"
        }
    },
    "Grape___healthy": {
        "crop": "Grape",
        "en": {
            "name": "Healthy Grape Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Vibrant, palmate lobed green leaf with clean margins and active tendril growth.",
            "immediate": "No action needed.",
            "organic": "Apply fish amino acid or Panchagavya (3%) foliar spray for berry sweetness.",
            "chemical": "None required.",
            "prevention": "Regular canopy management and drip irrigation.",
            "weather": "Warm dry sunshine.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍇"
        },
        "ta": {
            "name": "ஆரோக்கியமான திராட்சை இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "பச்சை நிறத்தில் சுத்தமான விளிம்புகளுடன் ஆரோக்கியமாக உள்ளது.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "பஞ்சகவ்யா (3%) தெளித்து வளர்ச்சியை ஊக்குவிக்கலாம்.",
            "chemical": "தேவையில்லை.",
            "prevention": "சொட்டு நீர்ப்பாசனம் மற்றும் முறையான கவாத்து.",
            "weather": "சாதாரண வெயில் காலம்.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍇"
        }
    },

    # ══════════════════════════════════════════════
    # ORANGE, PEACH, BELL PEPPER (5 Classes)
    # ══════════════════════════════════════════════
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange",
        "en": {
            "name": "Citrus Greening (Huanglongbing / HLB)",
            "cause": "Bacterium Candidatus Liberibacter spp. (Vector: Asian Citrus Psyllid)",
            "symptoms": "Asymmetrical blotchy mottling of leaves across veins, yellow shoots, lopsided bitter green fruit.",
            "immediate": "Control Asian Citrus Psyllid vector immediately before pruning or removing infected trees.",
            "organic": "Install yellow sticky traps (20/acre) and spray neem oil (5ml/L) to suppress psyllid nymphs.",
            "chemical": "Apply Imidacloprid 17.8% SL (0.5ml/L) or Thiamethoxam 25% WG (0.3g/L) during new flush.",
            "prevention": "Plant only certified disease-free nursery budwood; remove confirmed HLB-infected trees.",
            "weather": "Warm flush seasons attract psyllid vectors.",
            "recovery": "Incurable systemic infection — focus on vector containment",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍊"
        },
        "ta": {
            "name": "சிட்ரஸ் பசுமை நோய் (Citrus Greening / HLB)",
            "cause": "Candidatus Liberibacter பாக்டீரியா (ப்சில்லிட் பூச்சி மூலம் பரவும்)",
            "symptoms": "இலைகளில் சமச்சீரற்ற மஞ்சள் திட்டுகள்; பழங்கள் சிறியதாகி அடிப்பகுதி பச்சையாகவும் கசப்பாகவும் மாறும்.",
            "immediate": "மரங்களை அகற்றுவதற்கு முன் ப்சில்லிட் (Psyllid) பூச்சிகளை உடனடியாக கட்டுப்படுத்தவும்.",
            "organic": "ஏக்கருக்கு 20 மஞ்சள் ஒட்டுப் பொறிகள் வைக்கவும்; வேப்பெண்ணெய் (5 மி.லி/லி) தெளிக்கவும்.",
            "chemical": "Imidacloprid 17.8% SL (0.5 மி.லி/லி) தளிர்கள் வரும் பருவத்தில் தெளிக்கவும்.",
            "prevention": "சான்றளிக்கப்பட்ட நோய் இல்லாத கன்றுகளை மட்டுமே நடவு செய்யவும்.",
            "weather": "புதிய தளிர்கள் தோன்றும் மிதமான வெப்ப காலம்.",
            "recovery": "முழுமையாக குணப்படுத்த முடியாது — பூச்சி கட்டுப்பாடு அவசியம்",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍊"
        }
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "en": {
            "name": "Peach Bacterial Spot",
            "cause": "Bacterium Xanthomonas arboricola pv. pruni",
            "symptoms": "Angular purple-to-black water-soaked spots on leaves that drop out leaving 'shot-holes'; pitted fruit.",
            "immediate": "Avoid overhead irrigation; prune out cankered twigs during dry summer weather.",
            "organic": "Apply copper hydroxide or Bordeaux spray at leaf drop and late dormant stage.",
            "chemical": "Spray Copper Oxychloride (2.5g/L) + Streptocycline (100 ppm) at shuck split.",
            "prevention": "Plant windbreaks to reduce sandblasting leaf injury; maintain balanced nitrogen/calcium.",
            "weather": "Warm, windy, rainy spring weather (24–29°C).",
            "recovery": "14–21 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍑"
        },
        "ta": {
            "name": "பீச் பாக்டீரியா புள்ளி நோய்",
            "cause": "Xanthomonas arboricola பாக்டீரியா",
            "symptoms": "இலைகளில் கோண வடிவ ஊதா-கருப்பு புள்ளிகள் விழுந்து துளைகள் ஏற்படும்.",
            "immediate": "மேல்வழி நீர்ப்பாசனத்தை தவிர்க்கவும்; பாதிக்கப்பட்ட கிளைகளை அகற்றவும்.",
            "organic": "போர்டோ கலவை அல்லது செம்பு ஹைட்ராக்சைடு தெளிக்கவும்.",
            "chemical": "செம்பு ஆக்சிகுளோரைடு (2.5 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "காற்று தடுப்பு மரங்களை வளர்த்து இலை சேதத்தை குறைக்கவும்.",
            "weather": "காற்றுடன் கூடிய மழைக்காலம் (24–29°C).",
            "recovery": "14–21 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍑"
        }
    },
    "Peach___healthy": {
        "crop": "Peach",
        "en": {
            "name": "Healthy Peach Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Smooth, lance-shaped bright green leaves with healthy glands and zero shot-holes.",
            "immediate": "No action needed.",
            "organic": "Mulch root zone with organic compost.",
            "chemical": "None required.",
            "prevention": "Annual dormant pruning for open-center sunlight penetration.",
            "weather": "Normal growing conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍑"
        },
        "ta": {
            "name": "ஆரோக்கியமான பீச் இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "நீண்ட பிரகாசமான பச்சை நிற இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "இயற்கை மக்கिए உரம் இடவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "சூரிய ஒளி படும்படி ஆண்டுதோறும் கவாத்து செய்யவும்.",
            "weather": "சாதாரண வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍑"
        }
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper / Chilli",
        "en": {
            "name": "Bell Pepper & Chilli Bacterial Spot",
            "cause": "Bacterium Xanthomonas campestris pv. vesicatoria",
            "symptoms": "Small water-soaked dark brown spots with yellow halos on leaves; raised scabby warts on peppers.",
            "immediate": "Stop overhead watering immediately. Do not walk through or harvest wet plants.",
            "organic": "Spray Copper Oxychloride (2.5g/L) or Pseudomonas fluorescens (10g/L) every 7 days.",
            "chemical": "Apply Copper Hydroxide 77% WP (2g/L) + Mancozeb (2g/L) spray.",
            "prevention": "Treat seeds in hot water (50°C for 25 min) before sowing; rotate away from solanaceous crops.",
            "weather": "Warm monsoon rains with driving wind (24–30°C).",
            "recovery": "14–18 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🫑"
        },
        "ta": {
            "name": "குடைமிளகாய் பாக்டீரியா இலைப்புள்ளி",
            "cause": "Xanthomonas campestris பாக்டீரியா",
            "symptoms": "இலைகளில் மஞ்சள் வளையத்துடன் கூடிய நீர் கோர்த்த கரும்பழுப்பு புள்ளிகள்; காய்களில் சொறி போன்ற புண்கள்.",
            "immediate": "தெளிப்பு நீர்ப்பாசனத்தை நிறுத்தவும். செடிகள் ஈரமாக இருக்கும்போது வயலில் இறங்க வேண்டாம்.",
            "organic": "சூடோமோனாஸ் புளோரசன்ஸ் (10 கிராம்/லி) அல்லது செம்பு ஆக்சிகுளோரைடு தெளிக்கவும்.",
            "chemical": "செம்பு ஹைட்ராக்சைடு 77% WP (2 கிராம்/லி) + Mancozeb தெளிக்கவும்.",
            "prevention": "விதை நேர்த்தி செய்து நடவும்; தக்காளி/கத்திரி குடும்ப பயிர்களுடன் சுழற்சி தவிர்க்கவும்.",
            "weather": "வெப்பமான காற்று மற்றும் மழைக்காலம் (24–30°C).",
            "recovery": "14–18 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🫑"
        }
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper / Chilli",
        "en": {
            "name": "Healthy Bell Pepper Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Glossy, smooth dark-green ovate leaves with strong stems and healthy blossoms.",
            "immediate": "No action needed.",
            "organic": "Apply neem cake in soil and foliar Panchagavya (3%) every 15 days.",
            "chemical": "None required.",
            "prevention": "Use raised beds with plastic mulch and drip fertigation.",
            "weather": "Warm sunny weather (20–28°C).",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🫑"
        },
        "ta": {
            "name": "ஆரோக்கியமான குடைமிளகாய் இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "பளபளப்பான அடர் பச்சை நிற இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "வேப்பம் புண்ணாக்கு மற்றும் பஞ்சகவ்யா (3%) பயன்படுத்தவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "மேட்டுப்பாத்தி மற்றும் சொட்டு நீர்ப்பாசனம் அமைக்கவும்.",
            "weather": "மிதமான வெயில் காலம்.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🫑"
        }
    },

    # ══════════════════════════════════════════════
    # POTATO (3 Classes)
    # ══════════════════════════════════════════════
    "Potato___Early_blight": {
        "crop": "Potato",
        "en": {
            "name": "Potato Early Blight",
            "cause": "Fungus Alternaria solani",
            "symptoms": "Dark brown bullseye lesions with concentric rings on older lower leaves, surrounded by yellow chlorotic tissue.",
            "immediate": "Prune and destroy infected lower foliage. Hill up soil around base to protect tubers.",
            "organic": "Spray neem oil (5ml/L) or Trichoderma viride (5g/L) weekly.",
            "chemical": "Apply Mancozeb 75% WP (2.5g/L) or Chlorothalonil 75% WP (2g/L) every 7–10 days.",
            "prevention": "Avoid nitrogen/potassium deficiency; harvest only when tuber skin is fully set.",
            "weather": "Alternating wet and dry warm periods (24–29°C).",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🥔"
        },
        "ta": {
            "name": "உருளைக்கிழங்கு ஆரம்பக் கருகல் (Early Blight)",
            "cause": "Alternaria solani பூஞ்சை",
            "symptoms": "முதிர்ந்த கீழ் இலைகளில் இலக்கு பலகை (Target-board) போன்ற வட்ட வடிவ கரும்பழுப்பு புள்ளிகள்.",
            "immediate": "பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றவும்; கிழங்குகள் மண்ணுக்கு வெளியே தெரியாமல் மண் அணைக்கவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது டிரைக்கோடெர்மா விரிடி வாரந்தோறும் தெளிக்கவும்.",
            "chemical": "Mancozeb 75% WP (2.5 கிராம்/லி) அல்லது Chlorothalonil (2 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "சீரான உர நிர்வாகம் மற்றும் பயிர் சுழற்சி மேற்கொள்ளவும்.",
            "weather": "வெப்பமும் ஈரப்பதமும் மாறி மாறி வரும் வானிலை (24–29°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🥔"
        }
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "en": {
            "name": "Potato Late Blight",
            "cause": "Oomycete Phytophthora infestans",
            "symptoms": "Rapidly expanding water-soaked dark green to black blotches on leaf tips; white cottony mildew on underside in morning.",
            "immediate": "Destroy severely infected haulms immediately. Do not harvest during wet conditions.",
            "organic": "Preventive spray of Bordeaux mixture (1%) or Copper Hydroxide (2g/L) before cool rain spells.",
            "chemical": "Apply Metalaxyl 8% + Mancozeb 64% WP (2.5g/L) or Cymoxanil + Mancozeb (3g/L) urgently.",
            "prevention": "Plant certified disease-free seed tubers; eliminate volunteer potato plants and cull piles.",
            "weather": "Cool, cloudy, wet weather (12–20°C, >90% RH) — can destroy a field in 7 days.",
            "recovery": "Immediate containment required (7–10 days)",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🥔"
        },
        "ta": {
            "name": "உருளைக்கிழங்கு தாமதக் கருகல் (Late Blight)",
            "cause": "Phytophthora infestans பூஞ்சை",
            "symptoms": "இலை நுனிகளில் நீர் கோர்த்த கருப்பு படலங்கள் வேகமாக பரவும்; இலையின் அடிப்பகுதியில் வெள்ளை பூஞ்சை காணப்படும்.",
            "immediate": "பாதிக்கப்பட்ட செடிகளை உடனடியாக பிடுங்கி எரிக்கவும். ஈரமான நிலையில் அறுவடை செய்ய வேண்டாம்.",
            "organic": "போர்டோ கலவை (1%) அல்லது செம்பு ஹைட்ராக்சைடு (2 கிராம்/லி) தடுப்பு மருந்தாக தெளிக்கவும்.",
            "chemical": "Metalaxyl + Mancozeb (2.5 கிராம்/லி) அல்லது Cymoxanil + Mancozeb உடனடியாக தெளிக்கவும்.",
            "prevention": "சான்றளிக்கப்பட்ட விதைக் கிழங்குகளை மட்டுமே பயன்படுத்தவும்.",
            "weather": "குளிர்ந்த மற்றும் மூடுபனி நிறைந்த மழைக்காலம் (12–20°C).",
            "recovery": "உடனடி கட்டுப்பாடு அவசியம் (7–10 நாட்கள்)",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🥔"
        }
    },
    "Potato___healthy": {
        "crop": "Potato",
        "en": {
            "name": "Healthy Potato Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Compound dark green leaves with turgid leaflets and vigorous stolon development.",
            "immediate": "No action needed.",
            "organic": "Apply wood ash or bio-potash during tuber bulking stage.",
            "chemical": "None required.",
            "prevention": "Proper earthing-up at 30 and 45 days after planting.",
            "weather": "Cool sunny days (15–22°C).",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🥔"
        },
        "ta": {
            "name": "ஆரோக்கியமான உருளைக்கிழங்கு இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "அடர் பச்சை நிறத்தில் ஆரோக்கியமான கூட்டு இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "கிழங்கு பருக்கும் பருவத்தில் சாம்பல் சத்து (Bio-potash) இடவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "30 மற்றும் 45வது நாட்களில் மண் அணைக்கவும்.",
            "weather": "குளிர்ச்சியான வெயில் காலம்.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🥔"
        }
    },

    # ══════════════════════════════════════════════
    # RASPBERRY, SOYBEAN, SQUASH, STRAWBERRY (5 Classes)
    # ══════════════════════════════════════════════
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "en": {
            "name": "Healthy Raspberry Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Bright green palmate leaflets with silvery undersides and vigorous cane growth.",
            "immediate": "No action needed.",
            "organic": "Prune spent floricanes after fruiting and mulch with compost.",
            "chemical": "None required.",
            "prevention": "Trellis canes for airflow and weed control.",
            "weather": "Temperate conditions.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍓"
        },
        "ta": {
            "name": "ஆரோக்கியமான ராஸ்பெர்ரி இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "பச்சை நிறத்தில் ஆரோக்கியமான இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "இயற்கை உரம் இட்டு பராமரிக்கவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "நல்ல காற்றோட்டம் மற்றும் வடிகால்.",
            "weather": "சாதாரண வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍓"
        }
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "en": {
            "name": "Healthy Soybean Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Trifoliate deep green leaves indicating active Rhizobium root nodulation and nitrogen fixation.",
            "immediate": "No action required.",
            "organic": "Inoculate seeds with Bradyrhizobium japonicum and PSB biofertilizer.",
            "chemical": "None required.",
            "prevention": "Monitor for defoliating caterpillars and rust during pod fill.",
            "weather": "Warm moist growing weather.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🫘"
        },
        "ta": {
            "name": "ஆரோக்கியமான சோயாபீன் இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "அடர் பச்சை நிற மூவிலைகள்; வேர் முடிச்சுகளில் நல்ல தழைச்சத்து சேமிப்பு.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "ரைசோபியம் (Rhizobium) உயிர் உர விதை நேர்த்தி.",
            "chemical": "தேவையில்லை.",
            "prevention": "காய் பிடிக்கும் பருவத்தில் பூச்சி கண்காணிப்பு.",
            "weather": "மிதமான வெப்ப வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🫘"
        }
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash / Pumpkin",
        "en": {
            "name": "Squash & Gourds Powdery Mildew",
            "cause": "Fungus Podosphaera xanthii / Erysiphe cichoracearum",
            "symptoms": "White chalky powder patches covering upper and lower leaf surfaces; leaves turn brown and papery.",
            "immediate": "Remove heavily coated older leaves to stop spore cloud dispersal.",
            "organic": "Spray raw milk solution (1:9 in water) or potassium bicarbonate (5g/L) + neem oil (3ml/L) weekly.",
            "chemical": "Apply Wettable Sulfur (2g/L) or Dinocap (1ml/L) in early evening.",
            "prevention": "Space vines widely, ensure full sun exposure, and water only at the root zone.",
            "weather": "Warm dry days (22–30°C) with high relative humidity and shade.",
            "recovery": "7–12 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🎃"
        },
        "ta": {
            "name": "பூசணி மற்றும் சுரைக்காய் சாம்பல் நோய்",
            "cause": "Podosphaera xanthii பூஞ்சை",
            "symptoms": "இலைகளின் இருபுறமும் வெண்ணிற திருநீறு பூசியது போன்ற பூஞ்சை படலம் தோன்றி இலைகள் காய்ந்துவிடும்.",
            "immediate": "அதிகம் பாதிக்கப்பட்ட முதிர்ந்த இலைகளை அகற்றி அழிக்கவும்.",
            "organic": "வேப்பெண்ணெய் (3 மி.லி/லி) அல்லது பால் கரைசல் (1:9 விகிதம்) வாரந்தோறும் தெளிக்கவும்.",
            "chemical": "நனையும் கந்தகம் (2 கிராம்/லி) அல்லது Dinocap (1 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "கொடிகளுக்கு இடையே போதிய இடைவெளி விட்டு சூரிய ஒளி படுமாறு பராமரிக்கவும்.",
            "weather": "வறண்ட மற்றும் நிழலான ஈரப்பத வானிலை (22–30°C).",
            "recovery": "7–12 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🎃"
        }
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "en": {
            "name": "Strawberry Leaf Scorch",
            "cause": "Fungus Diplocarpon earliana",
            "symptoms": "Numerous irregular purple-to-reddish blotches that coalesce until the entire leaf dries and looks burned.",
            "immediate": "Clip and remove scorched leaves; renovate strawberry beds right after harvest.",
            "organic": "Spray copper soap or Trichoderma viride (5g/L) and mulch with clean straw.",
            "chemical": "Apply Captan 50% WP (2g/L) or Thiophanate-methyl (1g/L) at 10-day intervals.",
            "prevention": "Use drip irrigation instead of overhead sprinklers; replace beds every 2–3 years.",
            "weather": "Frequent spring/autumn rain splashes at 15–25°C.",
            "recovery": "12–16 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍓"
        },
        "ta": {
            "name": "ஸ்ட்ராபெர்ரி இலைக் கருகல் (Leaf Scorch)",
            "cause": "Diplocarpon earliana பூஞ்சை",
            "symptoms": "இலைகளில் ஊதா மற்றும் சிவப்பு நிற புள்ளிகள் இணைந்து இலை முழுவதும் தீய்ந்தது போல் காய்ந்துவிடும்.",
            "immediate": "கருகிய இலைகளை கத்தரித்து அகற்றவும்.",
            "organic": "டிரைக்கோடெர்மா விரிடி (5 கிராம்/லி) தெளிக்கவும்; வைக்கோல் நிலப்போர்வை இடவும்.",
            "chemical": "Captan 50% WP (2 கிராம்/லி) 10 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "prevention": "சொட்டு நீர்ப்பாசனம் மட்டுமே பயன்படுத்தவும்.",
            "weather": "மழைத்துளிகள் தெறிக்கும் ஈரமான வானிலை (15–25°C).",
            "recovery": "12–16 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍓"
        }
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "en": {
            "name": "Healthy Strawberry Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Vibrant trifoliate leaves with uniform saw-toothed margins and clean runners.",
            "immediate": "No action needed.",
            "organic": "Maintain straw mulch to keep berries off damp soil.",
            "chemical": "None required.",
            "prevention": "Ensure well-drained raised beds.",
            "weather": "Cool sunny days.",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍓"
        },
        "ta": {
            "name": "ஆரோக்கியமான ஸ்ட்ராபெர்ரி இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "பச்சை நிறத்தில் ரம்ப விளிம்புகளுடன் கூடிய ஆரோக்கியமான இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "பழங்கள் மண்ணில் படாமல் வைக்கோல் போர்வை அமைக்கவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "மேட்டுப்பாத்தி வடிகால் வசதி.",
            "weather": "குளிர்ந்த வெயில் வானிலை.",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍓"
        }
    },

    # ══════════════════════════════════════════════
    # TOMATO (10 Classes)
    # ══════════════════════════════════════════════
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Bacterial Spot",
            "cause": "Bacterium Xanthomonas campestris pv. vesicatoria",
            "symptoms": "Small, greasy water-soaked dark brown spots on leaves and stems; raised scabby spots on green fruit.",
            "immediate": "Cease overhead watering. Stake plants to improve air circulation and prevent soil splash.",
            "organic": "Spray Copper Hydroxide (2g/L) or Pseudomonas fluorescens (10g/L) every 5–7 days.",
            "chemical": "Apply Copper Oxychloride (2.5g/L) + Streptocycline (1g/10L water).",
            "prevention": "Use hot-water treated certified seeds; sanitize stakes and cages with bleach.",
            "weather": "Warm, humid rainy weather (24–30°C).",
            "recovery": "14 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி பாக்டீரியா புள்ளி நோய்",
            "cause": "Xanthomonas campestris பாக்டீரியா",
            "symptoms": "இலைகள் மற்றும் தண்டுகளில் மஞ்சள் வளையத்துடன் கூடிய சிறிய கருப்பு புள்ளிகள்; காய்களில் சொறி புள்ளிகள்.",
            "immediate": "மேல்வழி நீர்ப்பாசனத்தை தவிர்க்கவும். செடிகளுக்கு குச்சி நட்டு கட்டவும்.",
            "organic": "செம்பு ஹைட்ராக்சைடு (2 கிராம்/லி) அல்லது சூடோமோனாஸ் (10 கிராம்/லி) 7 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "chemical": "செம்பு ஆக்சிகுளோரைடு (2.5 கிராம்/லி) + ஸ்ட்ரெப்டோசைக்ளின் தெளிக்கவும்.",
            "prevention": "நோய் இல்லாத விதைகள் மற்றும் சுத்தமான குச்சிகளை பயன்படுத்தவும்.",
            "weather": "வெப்பமான மழைக்காலம் (24–30°C).",
            "recovery": "14 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Early Blight",
            "cause": "Fungus Alternaria solani",
            "symptoms": "Concentric 'target-board' dark brown rings on older lower leaves with yellow halos; sunken stem collar rot.",
            "immediate": "Prune off lower leaves up to 30 cm from soil surface. Apply organic mulch to stop soil splash.",
            "organic": "Spray neem oil (5ml/L) or Bacillus subtilis / Trichoderma viride (5g/L) every 7 days.",
            "chemical": "Apply Mancozeb 75% WP (2.5g/L) or Azoxystrobin 23% SC (1ml/L).",
            "prevention": "Stake plants, use drip irrigation, and practice 2-year rotation with non-solanaceous crops.",
            "weather": "Warm humid temperatures (24–29°C) with heavy morning dew.",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி ஆரம்பக் கருகல் (Early Blight)",
            "cause": "Alternaria solani பூஞ்சை",
            "symptoms": "பழைய கீழ் இலைகளில் வட்ட வட்டமான கரும்பழுப்பு புள்ளிகள் தோன்றி இலைகள் மஞ்சளாகி உதிரும்.",
            "immediate": "தரையை ஒட்டியுள்ள கீழ் இலைகளை அகற்றவும். மண் தெறிப்பதைத் தடுக்க நிலப்போர்வை இடவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது டிரைக்கோடெர்மா விரிடி (5 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "Mancozeb 75% WP (2.5 கிராம்/லி) அல்லது Azoxystrobin (1 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "சொட்டு நீர்ப்பாசனம் மற்றும் குச்சி நட்டு செடிகளை பராமரிக்கவும்.",
            "weather": "வெப்பமான மற்றும் பனி நிறைந்த வானிலை (24–29°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Late Blight",
            "cause": "Oomycete Phytophthora infestans",
            "symptoms": "Large, greasy greenish-black water-soaked blotches on leaves and stems; white fungal ring on underside; brown firm rot on fruit.",
            "immediate": "Uproot and bag severely infected plants immediately — do NOT compost. Warn neighboring farms.",
            "organic": "Preventive spray of Copper Oxychloride (3g/L) or Bordeaux mixture (1%).",
            "chemical": "Spray Metalaxyl + Mancozeb (2.5g/L) or Dimethomorph 50% WP (1g/L) every 5–7 days.",
            "prevention": "Avoid planting tomatoes near potatoes; ensure wide spacing and greenhouse humidity < 80%.",
            "weather": "Cool, rainy, overcast weather (15–22°C, >90% RH).",
            "recovery": "Urgent 5–7 day containment window",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி தாமதக் கருகல் (Late Blight)",
            "cause": "Phytophthora infestans பூஞ்சை",
            "symptoms": "இலைகள் மற்றும் தண்டுகளில் நீர் கோர்த்த கரும்பச்சை-பழுப்பு திட்டுகள்; பழங்கள் பழுப்பு நிறத்தில் அழுகும்.",
            "immediate": "கடுமையாக பாதிக்கப்பட்ட செடிகளை உடனடியாக பிடுங்கி எரிக்கவும்; உரக்குழியில் போட வேண்டாம்.",
            "organic": "போர்டோ கலவை (1%) அல்லது செம்பு ஆக்சிகுளோரைடு (3 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "Metalaxyl + Mancozeb (2.5 கிராம்/லி) அல்லது Dimethomorph (1 கிராம்/லி) 5-7 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "prevention": "உருளைக்கிழங்கு வயலுக்கு அருகில் தக்காளி பயிரிடுவதை தவிர்க்கவும்.",
            "weather": "குளிர்ந்த மழை மற்றும் மேகமூட்டமான வானிலை (15–22°C).",
            "recovery": "5–7 நாட்களுக்குள் தீவிர கட்டுப்பாடு அவசியம்",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Leaf Mold",
            "cause": "Fungus Passalora fulva (Cladosporium fulvum)",
            "symptoms": "Pale greenish-yellow spots on upper leaf surfaces with velvety olive-green to purple mold directly underneath.",
            "immediate": "Open greenhouse vents, prune lower leaves, and run fans to keep relative humidity below 85%.",
            "organic": "Spray potassium bicarbonate (5g/L) or neem oil + garlic extract weekly.",
            "chemical": "Apply Chlorothalonil (2g/L) or Difenoconazole 25% EC (0.5ml/L).",
            "prevention": "Steam-sterilize greenhouse benches and stakes between seasons; grow Cf-gene resistant hybrids.",
            "weather": "High humidity (>85%) and moderate temperatures (21–24°C).",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி இலை பூஞ்சை (Leaf Mold)",
            "cause": "Passalora fulva பூஞ்சை",
            "symptoms": "இலையின் மேல் பகுதியில் வெளிர் மஞ்சள் திட்டுகள் மற்றும் அடிப்பகுதியில் ஆலிவ்-பழுப்பு வெல்வெட் பூஞ்சை.",
            "immediate": "காற்றோட்டத்தை அதிகரிக்கவும்; கீழ் இலைகளை கவாத்து செய்யவும்.",
            "organic": "வேப்பெண்ணெய் + பூண்டு கரைசல் அல்லது பொட்டாசியம் பைகார்பனேட் தெளிக்கவும்.",
            "chemical": "Chlorothalonil (2 கிராம்/லி) அல்லது Difenoconazole (0.5 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "பசுமைக்குடிலில் ஈரப்பதம் 85%-க்கும் கீழ் இருக்குமாறு பராமரிக்கவும்.",
            "weather": "அதிக ஈரப்பதம் (>85%) மற்றும் மிதமான வெப்பம் (21–24°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Septoria Leaf Spot",
            "cause": "Fungus Septoria lycopersici",
            "symptoms": "Numerous small (2–4 mm) circular spots with dark brown margins and gray-tan centers dotted with black pycnidia.",
            "immediate": "Remove infected lower leaves immediately and mulch soil with straw or black plastic.",
            "organic": "Spray copper fungicide (2g/L) or Serenade (Bacillus subtilis) every 7 days.",
            "chemical": "Apply Mancozeb 75% WP (2.5g/L) or Chlorothalonil (2g/L).",
            "prevention": "Eradicate horse nettle and nightshade weeds; rotate crops for 2 years.",
            "weather": "Extended wet, humid weather (20–25°C) after first fruit set.",
            "recovery": "10–14 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி செப்டோரியா இலைப்புள்ளி",
            "cause": "Septoria lycopersici பூஞ்சை",
            "symptoms": "கீழ் இலைகளில் கருப்பு விளிம்பும் சாம்பல் நிற மையமும் கொண்ட எண்ணற்ற சிறிய வட்டப் புள்ளிகள்.",
            "immediate": "பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றி நிலப்போர்வை அமைக்கவும்.",
            "organic": "செம்பு பூஞ்சைக் கொல்லி (2 கிராம்/லி) 7 நாட்களுக்கு ஒருமுறை தெளிக்கவும்.",
            "chemical": "Mancozeb (2.5 கிராம்/லி) அல்லது Chlorothalonil (2 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "மணத்தக்காளி போன்ற களைகளை அகற்றவும்; 2 ஆண்டு பயிர் சுழற்சி செய்யவும்.",
            "weather": "காய் பிடிக்கும் பருவத்தில் பெய்யும் தொடர் மழை (20–25°C).",
            "recovery": "10–14 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Two-Spotted Spider Mites",
            "cause": "Arachnid Pest Tetranychus urticae",
            "symptoms": "Fine yellow/white stippling on upper leaves, bronze discoloration, and silky webbing under leaves.",
            "immediate": "Wash undersides of leaves with a strong jet of water; isolate heavily webbed plants.",
            "organic": "Spray neem oil (5ml/L) or insecticidal potassium soap; release predatory mites (Phytoseiulus persimilis).",
            "chemical": "Apply Abamectin 1.9% EC (0.5ml/L) or Spiromesifen 22.9% SC (1ml/L).",
            "prevention": "Keep field dust-free, mist foliage during dry heatwaves, and avoid broad-spectrum pyrethroids that kill beneficial bugs.",
            "weather": "Hot, dry, dusty conditions (>30°C, <50% RH).",
            "recovery": "7–10 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி செஞ்சிலந்தி பூச்சி (Spider Mites)",
            "cause": "Tetranychus urticae சிலந்திப் பூச்சி",
            "symptoms": "இலைகளில் நுண்ணிய மஞ்சள் புள்ளிகள் தோன்றி வெண்கல நிறமாக மாறும்; இலையின் அடியில் மெல்லிய நூல் வலை.",
            "immediate": "இலையின் அடிப்பகுதியில் தண்ணீரை வேகமாக பீய்ச்சி அடிக்கவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) அல்லது மீன் அமினோ அமிலம் தெளிக்கவும்.",
            "chemical": "Abamectin 1.9% EC (0.5 மி.லி/லி) அல்லது Spiromesifen (1 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "வறண்ட வெயில் காலத்தில் செடிகளில் ஈரப்பதம் குறையாமல் பராமரிக்கவும்.",
            "weather": "வெப்பமான மற்றும் வறண்ட வானிலை (>30°C).",
            "recovery": "7–10 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Target Spot",
            "cause": "Fungus Corynespora cassiicola",
            "symptoms": "Brown necrotic lesions with subtle concentric rings on leaves and deep sunken brown craters on ripening fruit.",
            "immediate": "Prune dense inner canopy and remove fallen infected fruit.",
            "organic": "Apply Trichoderma viride (5g/L) + neem oil spray weekly.",
            "chemical": "Spray Azoxystrobin 23% SC (1ml/L) or Pyraclostrobin + Metiram (2g/L).",
            "prevention": "Avoid locating tomato fields near cucumber, papaya, or rubber plantations.",
            "weather": "Warm humid conditions (24–32°C) with frequent mist.",
            "recovery": "12–16 days",
            "severity": "moderate",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி இலக்குப் புள்ளி (Target Spot)",
            "cause": "Corynespora cassiicola பூஞ்சை",
            "symptoms": "இலைகளில் வட்ட வடிவ பழுப்பு புள்ளிகள் மற்றும் பழங்களில் ஆழமான பழுப்பு நிற குழிகள்.",
            "immediate": "அடர்த்தியான இலைகளை கவாத்து செய்யவும்; அழுகிய பழங்களை அகற்றவும்.",
            "organic": "டிரைக்கோடெர்மா விரிடி (5 கிராம்/லி) மற்றும் வேப்பெண்ணெய் தெளிக்கவும்.",
            "chemical": "Azoxystrobin 23% SC (1 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "நல்ல காற்றோட்டம் மற்றும் சொட்டு நீர்ப்பாசனம் அமைக்கவும்.",
            "weather": "வெப்பமான மற்றும் ஈரப்பதமான வானிலை (24–32°C).",
            "recovery": "12–16 நாட்கள்",
            "severity": "moderate",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
            "cause": "Begomovirus transmitted by Whitefly (Bemisia tabaci)",
            "symptoms": "Severe upward cupping and curling of small leaves, bright yellow margins, bushy stunted growth, flower drop.",
            "immediate": "Rogue out and bury infected plants in plastic bags immediately. Install yellow sticky traps (15/acre).",
            "organic": "Spray Neem Seed Kernel Extract (NSKE 5%) or Verticillium lecanii (5g/L) targeting whitefly undersides.",
            "chemical": "Apply Imidacloprid 17.8% SL (0.5ml/L) or Diafenthiuron 50% WP (1g/L) for whitefly vector control.",
            "prevention": "Grow seedlings under 40-mesh insect-proof nylon net; plant 2 rows of barrier maize/sorghum around field.",
            "weather": "Hot dry weather favors rapid whitefly multiplication.",
            "recovery": "Viral infection is irreversible — protect healthy plants via vector control",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி மஞ்சள் இலை சுருட்டு வைரஸ் (TYLCV)",
            "cause": "வெள்ளை ஈ (Bemisia tabaci) மூலம் பரவும் வைரஸ்",
            "symptoms": "இலைகள் சிறியதாகி மேல்நோக்கி கிண்ணம் போல் சுருளும்; இலை ஓரங்கள் மஞ்சளாகும்; செடி குட்டையாகி பூக்கள் உதிரும்.",
            "immediate": "பாதிக்கப்பட்ட செடிகளை உடனடியாக பிடுங்கி புதைக்கவும். ஏக்கருக்கு 15 மஞ்சள் ஒட்டுப் பொறிகள் வைக்கவும்.",
            "organic": "வேப்பங்கொட்டை கரைசல் (NSKE 5%) அல்லது வெர்டிசிலியம் லெக்கானி (5 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "வெள்ளை ஈ கட்டுப்பாட்டிற்கு Imidacloprid (0.5 மி.லி/லி) அல்லது Diafenthiuron (1 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "வரப்பு ஓரங்களில் 2 வரிசை மக்காச்சோளம் தடுப்புப் பயிராக நடவும்; கொசுவலை நாற்றங்கால் அமைக்கவும்.",
            "weather": "வெப்பமான வறண்ட காலநிலை வெள்ளை ஈ பெருக்கத்திற்கு உகந்தது.",
            "recovery": "வைரஸ் பாதித்த செடி தேறாது — மற்ற செடிகளை வெள்ளை ஈயிலிருந்து காக்கவும்",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "en": {
            "name": "Tomato Mosaic Virus (ToMV)",
            "cause": "Tobamovirus (mechanically transmitted via hands, tools, seeds)",
            "symptoms": "Light and dark green mottled mosaic pattern on leaves, fern-like shoestring leaf distortion, internal browning of fruit.",
            "immediate": "Uproot infected plants carefully without touching adjacent vines. Wash hands with soap and dip tools in 10% bleach.",
            "organic": "Spray skim milk (10% solution) on plants before pruning/tying — milk proteins coat and inactivate virus particles.",
            "chemical": "No chemical virucide exists; apply micronutrient foliar spray (Zinc + Boron) to boost tolerance.",
            "prevention": "Prohibit smoking/tobacco handling in field; soak seeds in 10% Trisodium Phosphate (TSP) for 15 min.",
            "weather": "Spreads in all climates via human handling and pruning.",
            "recovery": "Manageable through strict sanitation",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "தக்காளி தேமல் வைரஸ் (Mosaic Virus)",
            "cause": "ToMV வைரஸ் (கைகள், கருவிகள் மற்றும் விதைகள் மூலம் பரவும்)",
            "symptoms": "இலைகளில் வெளிர் மற்றும் அடர் பச்சை நிற தேமல் திட்டுகள்; இலைகள் நூல் போல் சுருங்கும்.",
            "immediate": "பாதிக்கப்பட்ட செடிகளை பிற செடிகளில் படாமல் பிடுங்கி அழிக்கவும். கருவிகளை பிளீச்சிங் திரவத்தில் சுத்தம் செய்யவும்.",
            "organic": "கவாத்து செய்வதற்கு முன் 10% பால் கரைசலை செடிகளின் மேல் தெளித்தால் வைரஸ் பரவுவது தடுக்கப்படும்.",
            "chemical": "வைரஸுக்கு நேரடி இரசாயன மருந்து இல்லை; நுண்ணூட்டச்சத்து தெளிக்கவும்.",
            "prevention": "வயலில் புகையிலை பயன்படுத்துவதை தவிர்க்கவும்; விதை நேர்த்தி செய்யவும்.",
            "weather": "அனைத்து பருவங்களிலும் தொடுதல் மூலம் பரவும்.",
            "recovery": "சுகாதார முறைகள் மூலம் கட்டுப்படுத்தலாம்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "en": {
            "name": "Healthy Tomato Leaf",
            "cause": "No pathogen detected",
            "symptoms": "Deep green, aromatic compound leaves with healthy trichomes and strong flower trusses.",
            "immediate": "No action required.",
            "organic": "Apply Panchagavya (3%) and neem cake basal dressing for continuous immunity.",
            "chemical": "None required.",
            "prevention": "Prune suckers regularly, maintain staking, and water at root zone.",
            "weather": "Warm sunny days (21–28°C).",
            "recovery": "Optimal health",
            "severity": "none",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🍅"
        },
        "ta": {
            "name": "ஆரோக்கியமான தக்காளி இலை",
            "cause": "நோய் எதுவும் இல்லை",
            "symptoms": "அடர் பச்சை நிறத்தில் நறுமணமுள்ள ஆரோக்கியமான இலைகள்.",
            "immediate": "நடவடிக்கை தேவையில்லை.",
            "organic": "பஞ்சகவ்யா (3%) மற்றும் வேப்பம் புண்ணாக்கு இட்டு பராமரிக்கவும்.",
            "chemical": "தேவையில்லை.",
            "prevention": "பக்க கிளைகளை கவாத்து செய்து குச்சி நட்டு பராமரிக்கவும்.",
            "weather": "சீரான வெயில் காலம் (21–28°C).",
            "recovery": "முழு ஆரோக்கியம்",
            "severity": "none",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🍅"
        }
    },

    # ══════════════════════════════════════════════
    # REGIONAL INDIAN / TAMIL NADU STAPLE CROPS (Rice, Cotton, Sugarcane)
    # ══════════════════════════════════════════════
    "Rice___Leaf_Blast": {
        "crop": "Rice (Paddy)",
        "en": {
            "name": "Rice Leaf Blast (Paddy Blast)",
            "cause": "Fungus Magnaporthe oryzae (Pyricularia oryzae)",
            "symptoms": "Diamond or spindle-shaped lesions with gray-white centers and reddish-brown margins; can rot neck panicles.",
            "immediate": "Stop nitrogen top-dressing immediately. Maintain 2–3 cm standing water in paddy field.",
            "organic": "Foliar spray of Pseudomonas fluorescens (10g/L) at 30 and 45 DAT.",
            "chemical": "Spray Tricyclazole 75% WP (0.6g/L) or Isoprothiolane 40% EC (1.5ml/L).",
            "prevention": "Use blast-resistant varieties (e.g., CO-51, ADT-43), treat seeds with Pseudomonas, and split urea into 3–4 doses.",
            "weather": "Cool night temperatures (18–22°C), >90% humidity, and cloudy drizzle.",
            "recovery": "10–14 days",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌾"
        },
        "ta": {
            "name": "நெல் குலை நோய் (Rice Blast)",
            "cause": "Magnaporthe oryzae (Pyricularia) பூஞ்சை",
            "symptoms": "இலைகளில் கண் வடிவ (Spindle shape) புள்ளிகள் — நடுவில் சாம்பல் நிறமும் ஓரங்களில் செம்பழுப்பு நிறமும் இருக்கும்.",
            "immediate": "யூரியா (தழைச்சத்து) இடுவதை உடனடியாக நிறுத்தவும். வயலில் நீர் மட்டத்தை பராமரிக்கவும்.",
            "organic": "சூடோமோனாஸ் புளோரசன்ஸ் (10 கிராம்/லி) தெளிக்கவும்.",
            "chemical": "Tricyclazole 75% WP (0.6 கிராம்/லி) அல்லது Isoprothiolane (1.5 மி.லி/லி) தெளிக்கவும்.",
            "prevention": "வரப்புகளில் உள்ள புல் களைகளை அகற்றவும்; விதை நேர்த்தி செய்யவும்.",
            "weather": "குளிர்ந்த இரவு, பனி மற்றும் தொடர் தூறல் (>90% ஈரப்பதம்).",
            "recovery": "10–14 நாட்கள்",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌾"
        }
    },
    "Rice___Bacterial_Leaf_Blight": {
        "crop": "Rice (Paddy)",
        "en": {
            "name": "Rice Bacterial Leaf Blight (BLB)",
            "cause": "Bacterium Xanthomonas oryzae pv. oryzae",
            "symptoms": "Water-soaked yellowish stripes along leaf margins starting from tip, drying into wavy straw-colored blight.",
            "immediate": "Drain standing water from field for 3–4 days. Avoid field-to-field irrigation flow.",
            "organic": "Spray fresh cow dung extract (20% supernatant) filtered through muslin cloth.",
            "chemical": "Spray Copper Hydroxide (2g/L) + Streptocycline (0.1g/L) and apply Muriate of Potash (MOP).",
            "prevention": "Avoid clipping seedling tips during transplanting; use balanced NPK.",
            "weather": "Monsoon gales, heavy rain, and warm temperatures (25–34°C).",
            "recovery": "14 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🌾"
        },
        "ta": {
            "name": "நெல் பாக்டீரியா இலைக் கருகல் (BLB)",
            "cause": "Xanthomonas oryzae பாக்டீரியா",
            "symptoms": "இலை நுனியிலிருந்து விளிம்பு வழியாக மஞ்சள் நிற அலை போன்ற கோடுகள் பரவி வைக்கோல் போல் காய்ந்துவிடும்.",
            "immediate": "வயலில் உள்ள நீரை 3–4 நாட்களுக்கு வடித்து விடவும். ஒரு வயலிலிருந்து அடுத்த வயலுக்கு நீர் பாய்வதை தடுக்கவும்.",
            "organic": "20% பசுஞ்சாணக் கரைசலை வடிகட்டி தெளிக்கவும்.",
            "chemical": "செம்பு ஹைட்ராக்சைடு (2 கிராம்/லி) தெளிக்கவும்; பொட்டாஷ் உரம் இடவும்.",
            "prevention": "நாற்று நடும்போது நாற்றின் நுனியை கிள்ளுவதை தவிர்க்கவும்.",
            "weather": "புயல் காற்று மற்றும் கனமழை (25–34°C).",
            "recovery": "14 நாட்கள்",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🌾"
        }
    },
    "Cotton___Leaf_Curl_Disease": {
        "crop": "Cotton",
        "en": {
            "name": "Cotton Leaf Curl Virus (CLCuD)",
            "cause": "Begomovirus transmitted by Whitefly (Bemisia tabaci)",
            "symptoms": "Upward or downward curling of leaves, thickened dark-green veins on underside, cup-shaped leaf enations.",
            "immediate": "Remove early infected plants and eradicate Sida/Abutilon weeds on bunds.",
            "organic": "Spray Neem oil (5ml/L) + yellow sticky traps (20/acre).",
            "chemical": "Apply Flonicamid 50% WG (0.3g/L) or Pyriproxyfen 10% EC (1.5ml/L).",
            "prevention": "Avoid late sowing; grow Bt/hybrid varieties tolerant to CLCuD.",
            "weather": "High temperature (32–38°C) and dry spells.",
            "recovery": "Vector suppression within 7 days",
            "severity": "high",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "☁️"
        },
        "ta": {
            "name": "பருத்தி இலை சுருட்டு வைரஸ் (CLCuD)",
            "cause": "வெள்ளை ஈ மூலம் பரவும் Begomovirus",
            "symptoms": "இலைகள் மேல்நோக்கி சுருளும்; அடிப்பகுதி நரம்புகள் தடித்து கரும்பச்சையாக மாறும்.",
            "immediate": "ஆரம்பத்தில் பாதிக்கப்பட்ட செடிகள் மற்றும் துத்தி களைகளை அகற்றவும்.",
            "organic": "வேப்பெண்ணெய் (5 மி.லி/லி) தெளிக்கவும்; மஞ்சள் ஒட்டுப் பொறி வைக்கவும்.",
            "chemical": "Flonicamid 50% WG (0.3 கிராம்/லி) தெளிக்கவும்.",
            "prevention": "பருவம் தவறி விதைப்பதை தவிர்க்கவும்.",
            "weather": "அதிக வெப்பம் மற்றும் வறண்ட காலம் (32–38°C).",
            "recovery": "7 நாட்களில் வெள்ளை ஈ கட்டுப்பாடு",
            "severity": "high",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "☁️"
        }
    },
    "Sugarcane___Red_Rot": {
        "crop": "Sugarcane",
        "en": {
            "name": "Sugarcane Red Rot ('Cancer of Sugarcane')",
            "cause": "Fungus Colletotrichum falcatum",
            "symptoms": "Yellowing and drying of 3rd/4th crown leaves, reddish lesions on midrib; split cane shows red tissue with white cross-bands and sour alcoholic odor.",
            "immediate": "Dig out entire infected clump with roots and burn immediately. Bund the spot to stop irrigation water spread.",
            "organic": "Set-treatment with Trichoderma viride (10g/L) for 30 minutes before planting.",
            "chemical": "Dip seed setts in Carbendazim 50% WP (1g/L) or Thiophanate-methyl for 15 minutes.",
            "prevention": "Do not ratoon an infected field; rotate with paddy or green manure for 1 year.",
            "weather": "Waterlogging and monsoon humidity (25–32°C).",
            "recovery": "Clump removal & soil drenching",
            "severity": "critical",
            "sdg": "SDG 2 — Zero Hunger",
            "emoji": "🎋"
        },
        "ta": {
            "name": "கரும்பு செவ்வழுகல் நோய் (Red Rot)",
            "cause": "Colletotrichum falcatum பூஞ்சை",
            "symptoms": "குருத்து இலைகள் மஞ்சளாகி காயும்; நடு நரம்பில் சிவப்பு புள்ளிகள்; கரும்பை பிளந்தால் சிவப்பு நிறத்துடன் வெள்ளை குறுக்கு பட்டைகள் மற்றும் கள் வாடை வீசும்.",
            "immediate": "பாதிக்கப்பட்ட கரும்பு தூரை வேருடன் தோண்டி எடுத்து எரிக்கவும். பாசன நீர் வழியே பரவாமல் வரப்பு கட்டவும்.",
            "organic": "விதைக் கரணைகளை டிரைக்கோடெர்மா விரிடி (10 கிராம்/லி) கரைசலில் 30 நிமிடம் ஊறவைத்து நடவும்.",
            "chemical": "Carbendazim 50% WP (1 கிராம்/லி) கரைசலில் விதைக் கரணை நேர்த்தி செய்யவும்.",
            "prevention": "நோய் தாக்கிய வயலில் மறுதாம்பு விடக்கூடாது; நெல் பயிர் சுழற்சி செய்யவும்.",
            "weather": "நீர் தேக்கம் மற்றும் மழைக்காலம் (25–32°C).",
            "recovery": "தூர் அகற்றுதல் மற்றும் மண் நேர்த்தி",
            "severity": "critical",
            "sdg": "SDG 2 — பசியின்மை ஒழிப்பு",
            "emoji": "🎋"
        }
    }
}
