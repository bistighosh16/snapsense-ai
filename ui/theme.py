"""Liquid Mercury Theme - SnapSense AI (v2 - with background!)"""

import base64
from pathlib import Path


def get_base64_image(image_path: str) -> str:
    """Convert local image to base64 for CSS embedding"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""


# Load the hero background image
HERO_BG_PATH = Path(__file__).parent.parent / "assets" / "backgrounds" / "hero-bg.jpg"
HERO_BG_BASE64 = get_base64_image(str(HERO_BG_PATH))


def get_liquid_mercury_css():
    """Generate the CSS with embedded background image"""

    bg_style = f"url('data:image/jpeg;base64,{HERO_BG_BASE64}')" if HERO_BG_BASE64 else "none"

    return f"""
<style>
    /* ============================================
       LIQUID MERCURY THEME v2 - SnapSense AI
       With Iridescent Background! 🌊💜✨
       ============================================ */

    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syncopate:wght@400;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {{
        --void-black: #000000;
        --deep-space: #0a0a12;
        --twilight-purple: #1a1428;
        --liquid-silver: #d4d8e0;
        --mirror-chrome: #ffffff;
        --holo-purple: #a78bfa;
        --iridescent-pink: #f0abfc;
        --chrome-blue: #93c5fd;
        --oil-cyan: #67e8f9;
    }}

    /* ============ FULL-PAGE SUBTLE BACKGROUND ============ */
    .stApp {{
        background:
            linear-gradient(180deg,
                rgba(0, 0, 0, 0.92) 0%,
                rgba(10, 10, 18, 0.95) 50%,
                rgba(0, 0, 0, 0.92) 100%),
            {bg_style};
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: var(--liquid-silver);
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ============ CHROME STAR PARTICLES ============ */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(1px 1px at 15% 20%, rgba(255, 255, 255, 0.9), transparent),
            radial-gradient(1px 1px at 85% 30%, rgba(240, 171, 252, 0.9), transparent),
            radial-gradient(2px 2px at 45% 60%, rgba(167, 139, 250, 0.8), transparent),
            radial-gradient(1px 1px at 65% 80%, rgba(255, 255, 255, 0.9), transparent),
            radial-gradient(1px 1px at 25% 90%, rgba(147, 197, 253, 0.8), transparent),
            radial-gradient(2px 2px at 90% 50%, rgba(255, 255, 255, 0.7), transparent),
            radial-gradient(1px 1px at 55% 15%, rgba(103, 232, 249, 0.8), transparent);
        opacity: 0.5;
        z-index: 0;
        pointer-events: none;
        animation: sparkle 4s ease-in-out infinite alternate;
    }}

    @keyframes sparkle {{
        0% {{ opacity: 0.2; }}
        100% {{ opacity: 0.6; }}
    }}

    /* ============ HIDE STREAMLIT DEFAULTS ============ */
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    .stDeployButton {{ display: none; }}

    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
    }}

    /* ============ TYPOGRAPHY ============ */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Syncopate', sans-serif !important;
        color: var(--mirror-chrome) !important;
        letter-spacing: 0.1em;
        font-weight: 700 !important;
    }}

    p, span, div, label {{
        color: var(--liquid-silver);
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ============ HERO HEADER - FULL BACKGROUND IMAGE ============ */
    .hero-container {{
        text-align: center;
        padding: 5rem 2rem;
        margin-bottom: 2rem;
        background:
            linear-gradient(135deg,
                rgba(0, 0, 0, 0.75) 0%,
                rgba(26, 20, 40, 0.65) 50%,
                rgba(0, 0, 0, 0.75) 100%),
            {bg_style};
        background-size: cover;
        background-position: center;
        border: 1px solid rgba(240, 171, 252, 0.3);
        border-radius: 28px;
        backdrop-filter: blur(2px);
        -webkit-backdrop-filter: blur(2px);
        box-shadow:
            0 12px 60px rgba(167, 139, 250, 0.3),
            0 0 120px rgba(240, 171, 252, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
    }}

    /* Iridescent shine sweep */
    .hero-container::after {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent 30%,
            rgba(255, 255, 255, 0.08) 45%,
            rgba(240, 171, 252, 0.12) 50%,
            rgba(255, 255, 255, 0.08) 55%,
            transparent 70%
        );
        animation: liquid-shine 6s linear infinite;
        pointer-events: none;
    }}

    @keyframes liquid-shine {{
        0% {{ transform: translateX(-100%) translateY(-100%) rotate(45deg); }}
        100% {{ transform: translateX(100%) translateY(100%) rotate(45deg); }}
    }}

    .hero-title {{
        font-family: 'Syncopate', sans-serif !important;
        font-size: 4.5rem !important;
        font-weight: 700 !important;
        margin: 0;
        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #f0abfc 20%,
            #a78bfa 40%,
            #93c5fd 60%,
            #67e8f9 80%,
            #ffffff 100%
        );
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.15em;
        position: relative;
        z-index: 2;
        animation: chrome-flow 6s ease infinite;
        filter: drop-shadow(0 0 40px rgba(240, 171, 252, 0.6));
    }}

    @keyframes chrome-flow {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}

    .hero-tagline {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        color: var(--mirror-chrome);
        margin-top: 1.5rem;
        letter-spacing: 0.5em;
        text-transform: uppercase;
        opacity: 0.85;
        position: relative;
        z-index: 2;
        font-weight: 300;
        text-shadow: 0 0 20px rgba(167, 139, 250, 0.6);
    }}

    .hero-astronaut {{
        font-size: 4rem;
        display: inline-block;
        animation: float-glow 5s ease-in-out infinite;
        margin: 0 1.5rem;
        filter: drop-shadow(0 0 30px rgba(240, 171, 252, 0.8));
        position: relative;
        z-index: 2;
    }}

    @keyframes float-glow {{
        0%, 100% {{
            transform: translateY(0px) rotate(-3deg);
            filter: drop-shadow(0 0 30px rgba(167, 139, 250, 0.6));
        }}
        50% {{
            transform: translateY(-25px) rotate(3deg);
            filter: drop-shadow(0 0 50px rgba(240, 171, 252, 0.9));
        }}
    }}

    /* ============ CHROME CARDS ============ */
    .chrome-card {{
        background:
            linear-gradient(135deg,
                rgba(167, 139, 250, 0.08) 0%,
                rgba(240, 171, 252, 0.05) 33%,
                rgba(147, 197, 253, 0.08) 66%,
                rgba(103, 232, 249, 0.05) 100%),
            linear-gradient(180deg, rgba(26, 20, 40, 0.75) 0%, rgba(10, 10, 18, 0.65) 100%);
        background-size: 200% 200%;
        border: 1px solid rgba(212, 216, 224, 0.25);
        border-radius: 20px;
        padding: 1.5rem;
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        box-shadow:
            0 8px 40px rgba(0, 0, 0, 0.6),
            0 0 80px rgba(167, 139, 250, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}

    .chrome-card:hover {{
        border-color: rgba(240, 171, 252, 0.5);
        transform: translateY(-4px);
        box-shadow:
            0 16px 60px rgba(167, 139, 250, 0.3),
            0 0 100px rgba(240, 171, 252, 0.2);
    }}

    /* ============ MODE PILL ============ */
    .mode-pill {{
        display: inline-block;
        padding: 0.8rem 2rem;
        background:
            linear-gradient(135deg,
                rgba(167, 139, 250, 0.25),
                rgba(240, 171, 252, 0.2),
                rgba(147, 197, 253, 0.25));
        background-size: 200% 200%;
        border: 1px solid rgba(240, 171, 252, 0.6);
        border-radius: 50px;
        font-family: 'Syncopate', sans-serif;
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--mirror-chrome);
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin: 0.5rem 0;
        box-shadow:
            0 0 40px rgba(167, 139, 250, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        animation: pill-shimmer 4s ease infinite;
        text-shadow: 0 0 15px rgba(240, 171, 252, 0.8);
        backdrop-filter: blur(20px);
    }}

    @keyframes pill-shimmer {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}

    /* ============ BUTTONS ============ */
    .stButton > button {{
        background:
            linear-gradient(135deg,
                rgba(167, 139, 250, 0.2),
                rgba(240, 171, 252, 0.15),
                rgba(147, 197, 253, 0.2));
        background-size: 200% 200%;
        color: var(--mirror-chrome) !important;
        border: 1px solid rgba(212, 216, 224, 0.4);
        border-radius: 14px;
        padding: 0.8rem 2rem;
        font-family: 'Syncopate', sans-serif !important;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        font-size: 0.75rem;
        transition: all 0.3s ease;
        box-shadow:
            0 4px 30px rgba(167, 139, 250, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
    }}

    .stButton > button:hover {{
        background-position: 100% 50%;
        border-color: rgba(240, 171, 252, 0.7);
        transform: translateY(-3px);
        box-shadow:
            0 8px 40px rgba(240, 171, 252, 0.5),
            0 0 60px rgba(167, 139, 250, 0.3);
    }}

    /* ============ DOWNLOAD BUTTONS ============ */
    .stDownloadButton > button {{
        background:
            linear-gradient(135deg,
                rgba(147, 197, 253, 0.2),
                rgba(167, 139, 250, 0.2),
                rgba(240, 171, 252, 0.2));
        background-size: 200% 200%;
        color: var(--mirror-chrome) !important;
        border: 1px solid rgba(147, 197, 253, 0.5);
        border-radius: 14px;
        font-family: 'Syncopate', sans-serif !important;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        font-size: 0.7rem;
        padding: 0.8rem 1.5rem;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }}

    .stDownloadButton > button:hover {{
        border-color: var(--iridescent-pink);
        transform: translateY(-3px);
        box-shadow: 0 8px 40px rgba(240, 171, 252, 0.5);
    }}

    /* ============ SELECTBOX ============ */
    .stSelectbox > div > div {{
        background: linear-gradient(135deg, rgba(26, 20, 40, 0.8), rgba(10, 10, 18, 0.7)) !important;
        border: 1px solid rgba(212, 216, 224, 0.3) !important;
        border-radius: 14px !important;
        color: var(--liquid-silver) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        backdrop-filter: blur(20px);
    }}

    .stSelectbox > div > div:hover {{
        border-color: rgba(240, 171, 252, 0.6) !important;
        box-shadow: 0 0 30px rgba(167, 139, 250, 0.3);
    }}

    /* ============ FILE UPLOADER ============ */
    [data-testid="stFileUploader"] {{
        background:
            linear-gradient(135deg,
                rgba(167, 139, 250, 0.08),
                rgba(240, 171, 252, 0.05),
                rgba(147, 197, 253, 0.08));
        border: 2px dashed rgba(240, 171, 252, 0.5);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.4s ease;
        backdrop-filter: blur(20px);
    }}

    [data-testid="stFileUploader"]:hover {{
        border-color: var(--iridescent-pink);
        background:
            linear-gradient(135deg,
                rgba(167, 139, 250, 0.15),
                rgba(240, 171, 252, 0.1),
                rgba(147, 197, 253, 0.15));
        box-shadow:
            0 0 60px rgba(240, 171, 252, 0.3),
            inset 0 0 40px rgba(167, 139, 250, 0.08);
    }}

    [data-testid="stFileUploader"] label {{
        color: var(--mirror-chrome) !important;
        font-family: 'Syncopate', sans-serif !important;
        letter-spacing: 0.2em;
        font-weight: 700;
    }}

    /* ============ ALERTS ============ */
    .stAlert {{
        background: linear-gradient(135deg, rgba(26, 20, 40, 0.85), rgba(10, 10, 18, 0.75)) !important;
        border: 1px solid rgba(167, 139, 250, 0.5) !important;
        border-radius: 14px !important;
        backdrop-filter: blur(30px);
        color: var(--liquid-silver) !important;
        box-shadow: 0 0 40px rgba(167, 139, 250, 0.2);
    }}

    /* ============ SPINNER ============ */
    .stSpinner > div {{
        border-top-color: var(--iridescent-pink) !important;
    }}

    /* ============ SIDEBAR ============ */
    [data-testid="stSidebar"] {{
        background:
            linear-gradient(180deg,
                rgba(0, 0, 0, 0.98) 0%,
                rgba(26, 20, 40, 0.98) 100%) !important;
        border-right: 1px solid rgba(167, 139, 250, 0.3);
        backdrop-filter: blur(40px);
        box-shadow: 4px 0 60px rgba(167, 139, 250, 0.15);
    }}

    [data-testid="stSidebar"] * {{
        color: var(--liquid-silver) !important;
    }}

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4 {{
        color: var(--mirror-chrome) !important;
        font-family: 'Syncopate', sans-serif !important;
        letter-spacing: 0.2em;
    }}

    /* ============ IMAGES ============ */
    [data-testid="stImage"] img {{
        border-radius: 20px;
        border: 1px solid rgba(240, 171, 252, 0.4);
        box-shadow:
            0 16px 60px rgba(0, 0, 0, 0.7),
            0 0 80px rgba(167, 139, 250, 0.25);
    }}

    /* ============ MARKDOWN CONTENT ============ */
    .stMarkdown {{
        color: var(--liquid-silver);
    }}

    .stMarkdown code {{
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.2), rgba(240, 171, 252, 0.15)) !important;
        color: var(--iridescent-pink) !important;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace !important;
        border: 1px solid rgba(240, 171, 252, 0.4);
    }}

    .stMarkdown pre {{
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.9), rgba(26, 20, 40, 0.8)) !important;
        border: 1px solid rgba(167, 139, 250, 0.4);
        border-radius: 14px;
        padding: 1.2rem;
        box-shadow: inset 0 0 30px rgba(167, 139, 250, 0.08);
    }}

    .stMarkdown pre code {{
        background: transparent !important;
        border: none;
        color: var(--liquid-silver) !important;
    }}

    .stMarkdown table {{
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(167, 139, 250, 0.4);
        background: linear-gradient(135deg, rgba(26, 20, 40, 0.7), rgba(10, 10, 18, 0.6));
    }}

    .stMarkdown th {{
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.3), rgba(240, 171, 252, 0.2)) !important;
        color: var(--mirror-chrome) !important;
        font-family: 'Syncopate', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        font-size: 0.75rem;
        padding: 1rem;
        font-weight: 700;
    }}

    .stMarkdown td {{
        color: var(--liquid-silver) !important;
        padding: 0.8rem 1rem;
        border-top: 1px solid rgba(167, 139, 250, 0.2);
    }}

    /* ============ SCANNING ANIMATION - CHROME PORTAL ============ */
    .scanning-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
        flex-direction: column;
        gap: 1.5rem;
    }}

    .radar {{
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background:
            radial-gradient(circle,
                rgba(240, 171, 252, 0.2) 0%,
                rgba(167, 139, 250, 0.1) 40%,
                transparent 70%);
        border: 2px solid rgba(240, 171, 252, 0.5);
        position: relative;
        box-shadow:
            0 0 80px rgba(167, 139, 250, 0.5),
            0 0 120px rgba(240, 171, 252, 0.3),
            inset 0 0 60px rgba(167, 139, 250, 0.15);
        animation: portal-pulse 2s ease-in-out infinite;
    }}

    @keyframes portal-pulse {{
        0%, 100% {{
            box-shadow:
                0 0 80px rgba(167, 139, 250, 0.5),
                0 0 120px rgba(240, 171, 252, 0.3);
        }}
        50% {{
            box-shadow:
                0 0 100px rgba(167, 139, 250, 0.7),
                0 0 160px rgba(240, 171, 252, 0.5);
        }}
    }}

    .radar::before {{
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 50%;
        height: 3px;
        background: linear-gradient(90deg,
            var(--iridescent-pink),
            var(--holo-purple),
            transparent);
        transform-origin: left center;
        animation: radar-spin 2s linear infinite;
        box-shadow: 0 0 15px rgba(240, 171, 252, 1);
    }}

    .radar::after {{
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 10px;
        height: 10px;
        background: var(--mirror-chrome);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 25px rgba(255, 255, 255, 1);
    }}

    @keyframes radar-spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}

    .scanning-text {{
        font-family: 'Syncopate', sans-serif;
        background: linear-gradient(135deg, #ffffff, #a78bfa, #f0abfc, #ffffff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        font-size: 0.9rem;
        font-weight: 700;
        animation: chrome-flow 3s ease infinite;
    }}

    /* ============ FOOTER ============ */
    .cosmic-footer {{
        text-align: center;
        padding: 3rem;
        margin-top: 4rem;
        border-top: 1px solid rgba(167, 139, 250, 0.3);
        font-family: 'Syncopate', sans-serif;
        color: var(--liquid-silver);
        letter-spacing: 0.25em;
        text-transform: uppercase;
        font-size: 0.75rem;
        opacity: 0.8;
    }}

    .cosmic-footer .heart {{
        background: linear-gradient(135deg, #a78bfa, #f0abfc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: inline-block;
        animation: heart-pulse 2s ease-in-out infinite;
        font-size: 1.3rem;
    }}

    @keyframes heart-pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.3); }}
    }}

    /* ============ TABS ============ */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0.5rem;
        background: transparent;
    }}

    .stTabs [data-baseweb="tab"] {{
        background: linear-gradient(135deg, rgba(26, 20, 40, 0.7), rgba(10, 10, 18, 0.5));
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 12px;
        color: var(--liquid-silver) !important;
        font-family: 'Syncopate', sans-serif !important;
        letter-spacing: 0.2em;
        padding: 0.5rem 1.5rem;
        font-weight: 700;
    }}

    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.4), rgba(240, 171, 252, 0.3)) !important;
        border-color: var(--iridescent-pink) !important;
        color: var(--mirror-chrome) !important;
    }}

    /* ============ SECTION DIVIDERS - IMPROVED READABILITY ============ */
    .section-divider {{
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin: 3rem 0 1.5rem 0;
    }}

    .section-divider .line {{
        flex: 1;
        height: 2px;
        background: linear-gradient(90deg,
            transparent,
            rgba(167, 139, 250, 0.6),
            rgba(240, 171, 252, 0.7),
            transparent);
        box-shadow: 0 0 10px rgba(240, 171, 252, 0.3);
    }}

    .section-divider .label {{
        font-family: 'Syncopate', sans-serif;
        background: linear-gradient(135deg, #ffffff, #a78bfa, #f0abfc);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        font-size: 1rem;
        font-weight: 700;
        animation: chrome-flow 4s ease infinite;
        text-shadow: 0 0 20px rgba(167, 139, 250, 0.5);
        padding: 0 1rem;
    }}
</style>
"""


def apply_chrome_nebula_theme():
    """Apply the Liquid Mercury theme to the Streamlit app"""
    import streamlit as st
    st.markdown(get_liquid_mercury_css(), unsafe_allow_html=True)