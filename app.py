import streamlit as st
import html
import textwrap

# -------------------------------
# 🔑 PIN SETUP — Change this to your secret
# -------------------------------
CORRECT_PIN = "slayer"
# -------------------------------

# Initialize auth state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Hide Streamlit UI only after auth
if st.session_state.authenticated:
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# 🔒 PIN GATE — fully styled to match your theme
if not st.session_state.authenticated:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;500&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #fbeaf2 0%, #e5f6ff 100%);
            font-family: 'Poppins', sans-serif;
        }
        .pin-container {
            max-width: 450px;
            margin: 30vh auto;
            text-align: center;
            padding: 2rem;
        }
        .pin-title {
            font-family: 'Dancing Script', cursive;
            font-size: 3.4rem;
            color: #7a5f8c;
            margin-bottom: 1.2rem;
            text-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }
        .pin-instruction {
            font-size: 1.15rem;
            color: #5a5a72;
            margin-bottom: 1.5rem;
            line-height: 1.5;
        }
        .stButton>button {
            background: #e0b3d0;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 0.6rem 1.8rem;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
        }
        .stButton>button:hover {
            background: #d099c0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="pin-container">', unsafe_allow_html=True)
    st.markdown('<div class="pin-title">🔐 For Shar Only</div>', unsafe_allow_html=True)
    st.markdown('<div class="pin-instruction">Only the chosen one gets past this door… what’s the magic code?</div>', unsafe_allow_html=True)
    
    pin = st.text_input("PIN", type="password", label_visibility="collapsed")
    if st.button("Unlock", use_container_width=True):
        if pin == CORRECT_PIN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Wrong PIN! Only Shar knows the code.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 🎂 MAIN SITE (after PIN)
# -------------------------------
else:
    # -------------------------------
    # 🎀 MESSAGE (unchanged, just escaped safely)
    # -------------------------------
    SHAR_MESSAGE = """happy birthday <3

it’s kinda wild when i think about how we even became friends. i remember watching your youtube at first and just loving your whole vibe — the way you talked, the energy you had, the softness and warmth

i did and then one day out of nowhere… you dm me. like actually you. i still remember how random it felt but also how it immediately made sense. we didn’t even plan it, didn’t force anything — somehow we just ended up becoming friends, and honestly i’m so glad it happened the way it did.

you’ve always had this happy, friendly, wholesome personality that makes people feel safe and comfortable around you. even on days you don’t feel your best, you still manage to bring this softness into the world without trying. i love that about you, and i hope you never lose that part of yourself. 

i hope today treats you gently. i hope you laugh a lot, feel loved, feel celebrated, and feel like the genuinely good person you are. happy birthday, shar! have the best one <3
"""

    # ✅ Verified working playlist (keep or change if needed)
    SPOTIFY_PLAYLIST_EMBED_URL = "https://open.spotify.com/embed/playlist/6kxbJp3taOSkEf3mUjdeUM"


    # ✅ Clean GitHub image URLs (images starting with shar1.jpg as requested)
    BASE_IMG = "https://raw.githubusercontent.com/thesiddheshh/sharturns18/main/images"
    PHOTO_URLS = [
        f"{BASE_IMG}/shar1.jpg",
        f"{BASE_IMG}/shar2.jpg",
        f"{BASE_IMG}/shar3.jpg",
        f"{BASE_IMG}/shar4.jpg",
        f"{BASE_IMG}/shar5.jpg",
        f"{BASE_IMG}/shar6.jpg",
        f"{BASE_IMG}/shar7.jpg",
    ]

    # -------------------------------
    # 🎨 CSS — clean, pastel
    # -------------------------------
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;500&family=Homemade+Apple&display=swap');

        .stApp {
            background: linear-gradient(135deg, #fbeaf2 0%, #e5f6ff 100%);
            font-family: 'Poppins', sans-serif;
            padding: 0;
            margin: 0;
        }

        .main-content {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
        }

        .shar-title {
            font-family: 'Dancing Script', cursive;
            font-size: 4.2rem;
            color: #7a5f8c;
            text-align: center;
            margin-bottom: 1.8rem;
            text-shadow: 0 2px 6px rgba(0,0,0,0.08);
            animation: fadeIn 1.2s ease-out;
        }

        .message-card {
            background: url('https://www.toptal.com/designers/subtlepatterns/patterns/letter-paper.png'), #fff9f5;
            background-size: 150px;
            border-radius: 12px;
            padding: 2.4rem;
            margin-bottom: 2.2rem;
            box-shadow: 0 8px 24px rgba(160, 130, 190, 0.25);
            font-family: 'Homemade Apple', cursive;
            font-size: 1.35rem;
            line-height: 1.8;
            color: #5a5a72;
            position: relative;
            animation: floatIn 1s ease-out;
            text-align: left;
            border: 1px solid #f7e9f1;
        }

        .section-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.4rem;
            color: #8a6d9d;
            text-align: center;
            margin: 1.8rem 0 1.2rem;
        }

        .photo-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
            gap: 16px;
            margin-top: 0.8rem;
        }

        .photo-item {
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            aspect-ratio: 1 / 1;
        }

        .photo-item:hover {
            transform: scale(1.06);
        }

        .photo-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border: 3px solid #fff;
            border-radius: 16px;
        }

        .spotify-embed {
            display: flex;
            justify-content: center;
            margin: 1.2rem 0;
        }

        .decoration {
            position: fixed;
            z-index: -1;
            opacity: 0.6;
        }

        .heart-1 { top: 10%; left: 5%; font-size: 24px; color: #e0b3d0; animation: float 8s ease-in-out infinite; }
        .heart-2 { top: 70%; right: 8%; font-size: 18px; color: #b3e0d1; animation: float 10s ease-in-out infinite reverse; }
        .star-1 { top: 20%; right: 12%; font-size: 14px; color: #c7b3e0; animation: twinkle 4s infinite; }
        .star-2 { bottom: 15%; left: 10%; font-size: 16px; color: #d0b3e0; animation: twinkle 5s infinite 1s; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes floatIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 1; }
        }

        @media (max-width: 600px) {
            .shar-title { font-size: 3.2rem; }
            .message-card { padding: 1.6rem; font-size: 1.2rem; }
            .section-title { font-size: 2rem; }
            .photo-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }
        }
    </style>

    <div class="decoration heart-1">♥</div>
    <div class="decoration heart-2">♥</div>
    <div class="decoration star-1">✧</div>
    <div class="decoration star-2">✧</div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # 🎂 Layout
    # -------------------------------
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown('<div class="shar-title">Happy Birthday, Shar!</div>', unsafe_allow_html=True)

    # ✅ Safe, full handwritten font — no <p> artifact
    safe_message = html.escape(textwrap.dedent(SHAR_MESSAGE)).replace("\n", "<br/>")
    st.markdown(f'<div class="message-card"><p style="font-family: \'Homemade Apple\', cursive; font-size: 1.35rem; line-height: 1.8; color: #5a5a72; margin: 0;">{safe_message}</p></div>', unsafe_allow_html=True)

    # Music
    st.markdown('<div class="section-title">lil playlist to make your day </div>', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="spotify-embed">
        <iframe style="border-radius:12px" src="{SPOTIFY_PLAYLIST_EMBED_URL}" 
        width="100%" height="152" frameBorder="0" allow="clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
    ''', unsafe_allow_html=True)

    # Photos
    st.markdown('<div class="section-title">memories with you </div>', unsafe_allow_html=True)
    st.markdown('<div class="photo-grid">', unsafe_allow_html=True)
    for url in PHOTO_URLS:
        st.markdown(f'<div class="photo-item"><img src="{url}" alt="Shar"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
