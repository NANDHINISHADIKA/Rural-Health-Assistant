import streamlit as st

st.set_page_config(page_title="Rural Health Assistant", page_icon="🚑", layout="centered")

languages = {
    "English": {
        "title": "🚑 Rural Health Assistant",
        "subtitle": "Enter your symptoms and get health guidance",
        "select_symptoms": "Select your symptoms",
        "check_button": "Check Health",
        "condition": "Possible Condition",
        "severity": "Severity",
        "remedy": "Home Remedy",
        "hospital": "Hospital to Visit",
        "emergency": "Emergency Numbers",
        "ambulance": "Ambulance: 108",
        "health_helpline": "Health Helpline: 104",
        "mild": "Mild",
        "moderate": "Moderate",
        "serious": "Serious - Visit Hospital Immediately"
    },
    "Tamil": {
        "title": "🚑 கிராம உடல்நல உதவியாளர்",
        "subtitle": "உங்கள் அறிகுறிகளை தேர்ந்தெடுத்து உடல்நல வழிகாட்டுதல் பெறுங்கள்",
        "select_symptoms": "உங்கள் அறிகுறிகளை தேர்ந்தெடுக்கவும்",
        "check_button": "உடல்நலம் சரிபார்க்கவும்",
        "condition": "சாத்தியமான நோய்",
        "severity": "தீவிரம்",
        "remedy": "வீட்டு வைத்தியம்",
        "hospital": "செல்ல வேண்டிய மருத்துவமனை",
        "emergency": "அவசர எண்கள்",
        "ambulance": "ஆம்புலன்ஸ்: 108",
        "health_helpline": "உடல்நல உதவி: 104",
        "mild": "லேசானது",
        "moderate": "மிதமானது",
        "serious": "தீவிரமானது - உடனே மருத்துவமனை செல்லுங்கள்"
    },
    "Hindi": {
        "title": "🚑 ग्रामीण स्वास्थ्य सहायक",
        "subtitle": "अपने लक्षण चुनें और स्वास्थ्य मार्गदर्शन पाएं",
        "select_symptoms": "अपने लक्षण चुनें",
        "check_button": "स्वास्थ्य जांचें",
        "condition": "संभावित बीमारी",
        "severity": "गंभीरता",
        "remedy": "घरेलू उपाय",
        "hospital": "जाने वाला अस्पताल",
        "emergency": "आपातकालीन नंबर",
        "ambulance": "एम्बुलेंस: 108",
        "health_helpline": "स्वास्थ्य हेल्पलाइन: 104",
        "mild": "हल्का",
        "moderate": "मध्यम",
        "serious": "गंभीर - तुरंत अस्पताल जाएं"
    },
    "Telugu": {
        "title": "🚑 గ్రామీణ ఆరోగ్య సహాయకుడు",
        "subtitle": "మీ లక్షణాలను ఎంచుకుని ఆరోగ్య మార్గదర్శకత్వం పొందండి",
        "select_symptoms": "మీ లక్షణాలను ఎంచుకోండి",
        "check_button": "ఆరోగ్యం తనిఖీ చేయండి",
        "condition": "సాధ్యమైన వ్యాధి",
        "severity": "తీవ్రత",
        "remedy": "ఇంటి చికిత్స",
        "hospital": "వెళ్ళాల్సిన ఆసుపత్రి",
        "emergency": "అత్యవసర నంబర్లు",
        "ambulance": "అంబులెన్స్: 108",
        "health_helpline": "ఆరోగ్య హెల్ప్‌లైన్: 104",
        "mild": "తేలికపాటి",
        "moderate": "మధ్యస్థం",
        "serious": "తీవ్రమైనది - వెంటనే ఆసుపత్రికి వెళ్ళండి"
    },
    "Malayalam": {
        "title": "🚑 ഗ്രാമീണ ആരോഗ്യ സഹായി",
        "subtitle": "നിങ്ങളുടെ ലക്ഷണങ്ങൾ തിരഞ്ഞെടുത്ത് ആരോഗ്യ മാർഗ്ഗനിർദ്ദേശം നേടുക",
        "select_symptoms": "നിങ്ങളുടെ ലക്ഷണങ്ങൾ തിരഞ്ഞെടുക്കുക",
        "check_button": "ആരോഗ്യം പരിശോധിക്കുക",
        "condition": "സാധ്യമായ രോഗം",
        "severity": "തീവ്രത",
        "remedy": "വീട്ടുവൈദ്യം",
        "hospital": "പോകേണ്ട ആശുപത്രി",
        "emergency": "അടിയന്തര നംബറുകൾ",
        "ambulance": "ആംബുലൻസ്: 108",
        "health_helpline": "ആരോഗ്യ ഹെൽപ്‌ലൈൻ: 104",
        "mild": "നേരിയ",
        "moderate": "മിതമായ",
        "serious": "ഗുരുതരം - ഉടനെ ആശുപത്രിയിൽ പോകുക"
    }
}

symptom_db = {
    "fever": {
        "condition": {"English": "Viral Fever / Malaria", "Tamil": "வைரல் காய்ச்சல் / மலேரியா", "Hindi": "वायरल बुखार / मलेरिया", "Telugu": "వైరల్ జ్వరం / మలేరియా", "Malayalam": "വൈറൽ പനി / മലേറിയ"},
        "severity": "moderate",
        "remedy": {"English": "Drink plenty of water, rest, take paracetamol", "Tamil": "அதிகமாக தண்ணீர் குடிக்கவும், ஓய்வு எடுக்கவும்", "Hindi": "खूब पानी पिएं, आराम करें, पेरासिटामोल लें", "Telugu": "చాలా నీరు తాగండి, విశ్రాంతి తీసుకోండి", "Malayalam": "ധാരാളം വെള്ളം കുടിക്കുക, വിശ്രമിക്കുക"},
        "hospital": {"English": "Primary Health Centre (PHC)", "Tamil": "முதல்நிலை சுகாதார மையம்", "Hindi": "प्राथमिक स्वास्थ्य केंद्र", "Telugu": "ప్రాథమిక ఆరోగ్య కేంద్రం", "Malayalam": "പ്രാഥമിക ആരോഗ്യ കേന്ദ്രം"}
    },
    "headache": {
        "condition": {"English": "Migraine / Tension Headache", "Tamil": "ஒற்றைத் தலைவலி", "Hindi": "माइग्रेन / तनाव सिरदर्द", "Telugu": "మైగ్రేన్ / తలనొప్పి", "Malayalam": "മൈഗ്രേൻ / തലവേദന"},
        "severity": "mild",
        "remedy": {"English": "Rest in dark room, drink water, apply cold compress", "Tamil": "இருண்ட அறையில் ஓய்வு, தண்ணீர் குடிக்கவும்", "Hindi": "अंधेरे कमरे में आराम करें, पानी पिएं", "Telugu": "చీకటి గదిలో విశ్రాంతి, నీరు తాగండి", "Malayalam": "ഇരുണ്ട മുറിയിൽ വിശ്രമിക്കുക, വെള്ളം കുടിക്കുക"},
        "hospital": {"English": "Nearest Clinic", "Tamil": "அருகில் உள்ள கிளினிக்", "Hindi": "नजदीकी क्लिनिक", "Telugu": "సమీప క్లినిక్", "Malayalam": "അടുത്തുള്ള ക്ലിനിക്"}
    },
    "cough": {
        "condition": {"English": "Common Cold / Bronchitis", "Tamil": "சாதாரண சளி / மூச்சுக்குழாய் அழற்சி", "Hindi": "सामान्य सर्दी / ब्रोंकाइटिस", "Telugu": "సాధారణ జలుబు / బ్రాంకైటిస్", "Malayalam": "സാധാരണ ജലദോഷം / ബ്രോങ്കൈറ്റിസ്"},
        "severity": "mild",
        "remedy": {"English": "Honey with ginger tea, steam inhalation, rest", "Tamil": "தேன் + இஞ்சி தேநீர், நீராவி பிடிக்கவும்", "Hindi": "शहद अदरक चाय, भाप लें, आराम करें", "Telugu": "తేనె అల్లం టీ, ఆవిరి పీల్చండి", "Malayalam": "തേൻ ഇഞ്ചി ചായ, ആവി പിടിക്കുക"},
        "hospital": {"English": "Nearest Clinic", "Tamil": "அருகில் உள்ள கிளினிக்", "Hindi": "नजदीकी क्लिनिक", "Telugu": "సమీప క్లినిక్", "Malayalam": "അടുത്തുള്ള ക്ലിനിക്"}
    },
    "chest pain": {
        "condition": {"English": "Heart Attack / Angina", "Tamil": "மாரடைப்பு / நெஞ்சு வலி", "Hindi": "दिल का दौरा / एनजाइना", "Telugu": "గుండెపోటు / ఆంజినా", "Malayalam": "ഹൃദയാഘാതം / ആൻജൈന"},
        "severity": "serious",
        "remedy": {"English": "Call 108 immediately! Do not delay!", "Tamil": "உடனே 108 அழையுங்கள்! தாமதிக்காதீர்கள்!", "Hindi": "तुरंत 108 कॉल करें! देर न करें!", "Telugu": "వెంటనే 108 కి కాల్ చేయండి!", "Malayalam": "ഉടൻ 108 വിളിക്കുക! വൈകരുത്!"},
        "hospital": {"English": "Government Hospital Emergency", "Tamil": "அரசு மருத்துவமனை அவசர சிகிச்சை", "Hindi": "सरकारी अस्पताल आपातकाल", "Telugu": "ప్రభుత్వ ఆసుపత్రి అత్యవసర విభాగం", "Malayalam": "സർക്കാർ ആശുപത്രി അടിയന്തര വിഭാഗം"}
    },
    "stomach pain": {
        "condition": {"English": "Gastritis / Food Poisoning", "Tamil": "வயிற்று வலி / உணவு விஷம்", "Hindi": "गैस्ट्राइटिस / फूड पॉइजनिंग", "Telugu": "గ్యాస్ట్రైటిస్ / ఆహార విషం", "Malayalam": "ഗ്യാസ്ട്രൈറ്റിസ് / ഭക്ഷണ വിഷബാധ"},
        "severity": "moderate",
        "remedy": {"English": "Drink ORS, avoid spicy food, rest", "Tamil": "ORS குடிக்கவும், காரமான உணவை தவிர்க்கவும்", "Hindi": "ORS पिएं, मसालेदार खाना न खाएं", "Telugu": "ORS తాగండి, కారమైన ఆహారం తినవద్దు", "Malayalam": "ORS കുടിക്കുക, എരിവുള്ള ഭക്ഷണം ഒഴിവാക്കുക"},
        "hospital": {"English": "Primary Health Centre (PHC)", "Tamil": "முதல்நிலை சுகாதார மையம்", "Hindi": "प्राथमिक स्वास्थ्य केंद्र", "Telugu": "ప్రాథమిక ఆరోగ్య కేంద్రం", "Malayalam": "പ്രാഥമിക ആരോഗ്യ കേന്ദ്രം"}
    },
    "vomiting": {
        "condition": {"English": "Dehydration / Food Poisoning", "Tamil": "நீர்ச்சத்து குறைபாடு", "Hindi": "डिहाइड्रेशन / फूड पॉइजनिंग", "Telugu": "డీహైడ్రేషన్ / ఆహార విషం", "Malayalam": "നിർജ്ജലീകരണം / ഭക്ഷണ വിഷബാധ"},
        "severity": "moderate",
        "remedy": {"English": "Sip ORS frequently, avoid solid food for 2 hours", "Tamil": "ORS கொஞ்சம் கொஞ்சமாக குடிக்கவும்", "Hindi": "ORS धीरे-धीरे पिएं, 2 घंटे ठोस खाना न खाएं", "Telugu": "ORS నెమ్మదిగా తాగండి", "Malayalam": "ORS പതുക്കെ കുടിക്കുക"},
        "hospital": {"English": "Primary Health Centre (PHC)", "Tamil": "முதல்நிலை சுகாதார மையம்", "Hindi": "प्राथमिक स्वास्थ्य केंद्र", "Telugu": "ప్రాథమిక ఆరోగ్య కేంద్రం", "Malayalam": "പ്രാഥമിക ആരോഗ്യ കേന്ദ്രം"}
    },
    "diabetes symptoms": {
        "condition": {"English": "Diabetes / High Blood Sugar", "Tamil": "நீரிழிவு நோய்", "Hindi": "मधुमेह / हाई ब्लड शुगर", "Telugu": "మధుమేహం", "Malayalam": "പ്രമേഹം"},
        "severity": "moderate",
        "remedy": {"English": "Avoid sugar, drink water, check blood sugar level", "Tamil": "சர்க்கரை தவிர்க்கவும், தண்ணீர் குடிக்கவும்", "Hindi": "चीनी से बचें, पानी पिएं, ब्लड शुगर जांचें", "Telugu": "చక్కెర తినవద్దు, నీరు తాగండి", "Malayalam": "പഞ്ചസാര ഒഴിവാക്കുക, വെള്ളം കുടിക്കുക"},
        "hospital": {"English": "Primary Health Centre (PHC)", "Tamil": "முதல்நிலை சுகாதார மையம்", "Hindi": "प्राथमिक स्वास्थ्य केंद्र", "Telugu": "ప్రాథమిక ఆరోగ్య కేంద్రం", "Malayalam": "പ്രാഥമിക ആരോഗ്യ കേന്ദ്രം"}
    },
    "snake bite": {
        "condition": {"English": "Venomous Snake Bite", "Tamil": "விஷ பாம்பு கடி", "Hindi": "जहरीले सांप का काटना", "Telugu": "విషపు పాము కాటు", "Malayalam": "വിഷ പാമ്പ് കടി"},
        "severity": "serious",
        "remedy": {"English": "Call 108 immediately! Keep calm, do not move the bitten area", "Tamil": "உடனே 108 அழையுங்கள்! அமைதியாக இருங்கள்", "Hindi": "तुरंत 108 कॉल करें! शांत रहें, काटी जगह न हिलाएं", "Telugu": "వెంటనే 108 కి కాల్ చేయండి! శాంతంగా ఉండండి", "Malayalam": "ഉടൻ 108 വിളിക്കുക! ശാന്തമായിരിക്കുക"},
        "hospital": {"English": "Government Hospital Emergency - Anti-venom available", "Tamil": "அரசு மருத்துவமனை — விஷ எதிர்ப்பு மருந்து கிடைக்கும்", "Hindi": "सरकारी अस्पताल — एंटी-वेनम उपलब्ध", "Telugu": "ప్రభుత్వ ఆసుపత్రి — యాంటీ వెనమ్ అందుబాటులో ఉంది", "Malayalam": "സർക്കാർ ആശുപത്രി — ആന്റി വെനം ലഭ്യമാണ്"}
    },
    "eye problem": {
        "condition": {"English": "Conjunctivitis / Eye Infection", "Tamil": "கண் தொற்று / சிவப்பு கண்", "Hindi": "आंख का संक्रमण / कंजक्टिवाइटिस", "Telugu": "కంటి సంక్రమణ / నేత్ర రోగం", "Malayalam": "കണ്ണ് അണുബാധ / കൺജങ്ക്ടിവൈറ്റിസ്"},
        "severity": "moderate",
        "remedy": {"English": "Wash eyes with clean water, avoid touching eyes, use eye drops", "Tamil": "சுத்தமான தண்ணீரில் கண்களை கழுவுங்கள்", "Hindi": "साफ पानी से आंखें धोएं, आंखें न छुएं", "Telugu": "శుభ్రమైన నీటితో కళ్ళు కడగండి", "Malayalam": "ശുദ്ധമായ വെള്ളത്തിൽ കണ്ണ് കഴുകുക"},
        "hospital": {"English": "Eye Clinic / PHC", "Tamil": "கண் கிளினிக் / முதல்நிலை சுகாதார மையம்", "Hindi": "आंख क्लिनिक / PHC", "Telugu": "కంటి క్లినిక్ / PHC", "Malayalam": "കണ്ണ് ക്ലിനിക് / PHC"}
    },
    "back pain": {
        "condition": {"English": "Muscle Strain / Spine Problem", "Tamil": "தசை வலி / முதுகெலும்பு பிரச்சனை", "Hindi": "मांसपेशी खिंचाव / रीढ़ की समस्या", "Telugu": "కండర నొప్పి / వెన్నెముక సమస్య", "Malayalam": "പേശി വലിവ് / നട്ടെല്ല് പ്രശ്നം"},
        "severity": "mild",
        "remedy": {"English": "Rest, apply warm compress, gentle stretching", "Tamil": "ஓய்வு எடுக்கவும், சூடான ஒத்தடம் கொடுக்கவும்", "Hindi": "आराम करें, गर्म सेंक लगाएं, हल्की स्ट्रेचिंग करें", "Telugu": "విశ్రాంతి, వేడి కాపడం, తేలికపాటి వ్యాయామం", "Malayalam": "വിശ്രമിക്കുക, ചൂടുള്ള കഴുകൽ, നേരിയ വ്യായാമം"},
        "hospital": {"English": "Nearest Clinic", "Tamil": "அருகில் உள்ள கிளினிக்", "Hindi": "नजदीकी क्लिनिक", "Telugu": "సమీప క్లినిక్", "Malayalam": "അടുത്തുള്ള ക്ലിനിക്"}
    },
    "diarrhea": {
        "condition": {"English": "Diarrhea / Stomach Infection", "Tamil": "வயிற்றுப்போக்கு", "Hindi": "दस्त / पेट का संक्रमण", "Telugu": "విరేచనాలు / కడుపు సంక్రమణ", "Malayalam": "വയറിളക്കം / വയർ അണുബാധ"},
        "severity": "moderate",
        "remedy": {"English": "Drink ORS, eat banana and rice, avoid oily food", "Tamil": "ORS குடிக்கவும், வாழைப்பழம் சாப்பிடவும்", "Hindi": "ORS पिएं, केला और चावल खाएं, तैलीय खाना न खाएं", "Telugu": "ORS తాగండి, అరటిపండు మరియు అన్నం తినండి", "Malayalam": "ORS കുടിക്കുക, വാഴപ്പഴവും ചോറും കഴിക്കുക"},
        "hospital": {"English": "Primary Health Centre (PHC)", "Tamil": "முதல்நிலை சுகாதார மையம்", "Hindi": "प्राथमिक स्वास्थ्य केंद्र", "Telugu": "ప్రాథమిక ఆరోగ్య కేంద్రం", "Malayalam": "പ്രാഥമിക ആരോഗ്യ കേന്ദ്രം"}
    }
}

lang = st.selectbox("🌐 Select Language / மொழி தேர்வு / भाषा चुनें", list(languages.keys()))
L = languages[lang]
st.title(L["title"])
st.subheader(L["subtitle"])
st.divider()

symptom_options = list(symptom_db.keys())
selected_symptoms = st.multiselect(L["select_symptoms"], symptom_options)

if st.button(L["check_button"], use_container_width=True):
    if selected_symptoms:
        for symptom in selected_symptoms:
            data = symptom_db[symptom]
            severity = data["severity"]

            st.markdown("---")
            st.markdown("### " + symptom.upper())
            st.write("**" + L["condition"] + ":** " + data["condition"][lang])

            if severity == "mild":
                st.success(L["severity"] + ": " + L["mild"])
            elif severity == "moderate":
                st.warning(L["severity"] + ": " + L["moderate"])
            else:
                st.error(L["severity"] + ": " + L["serious"])

            st.info(L["remedy"] + ": " + data["remedy"][lang])
            st.write("🏥 " + L["hospital"] + ": " + data["hospital"][lang])

        st.divider()
        st.subheader("🚨 " + L["emergency"])
        st.error("🚑 " + L["ambulance"])
        st.error("📞 " + L["health_helpline"])
    else:
        st.warning("Please select at least one symptom!")