"""Reusable UI components for Chrome Nebula theme"""

import streamlit as st


def render_hero():
    """Render the cosmic hero header"""
    st.markdown("""
    <div class="hero-container">
        <div>
            <span class="hero-astronaut">🧑‍🚀</span>
            <span class="hero-title">SNAPSENSE AI</span>
            <span class="hero-astronaut">🛸</span>
        </div>
        <p class="hero-tagline">Vision AI • See Beyond the Pixels</p>
    </div>
    """, unsafe_allow_html=True)


def render_mode_pill(mode_name: str, icon: str):
    """Render a cosmic mode pill"""
    st.markdown(f"""
    <div style="text-align: center;">
        <span class="mode-pill">{icon} {mode_name} ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)


def render_section_divider(label: str):
    """Render a cosmic section divider"""
    st.markdown(f"""
    <div class="section-divider">
        <div class="line"></div>
        <div class="label">{label}</div>
        <div class="line"></div>
    </div>
    """, unsafe_allow_html=True)


def render_scanning_animation():
    """Render the radar scanning animation"""
    st.markdown("""
    <div class="scanning-container">
        <div class="radar"></div>
        <div class="scanning-text">📡 Scanning Image • Vision AI Processing</div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the cosmic footer"""
    st.markdown("""
    <div class="cosmic-footer">
        Made with <span class="heart">💜</span> in the void by <strong>Vivi</strong> 🧑‍🚀✨
        <br><br>
        <span style="opacity: 0.5;">Transmitted from Earth • Powered by Groq Vision</span>
    </div>
    """, unsafe_allow_html=True)


def render_stats_bar(mode: str, image_name: str, size_kb: float):
    """Render a stats bar showing analysis info"""
    st.markdown(f"""
    <div class="chrome-card" style="display: flex; justify-content: space-around; text-align: center;">
        <div>
            <div style="font-family: 'Orbitron', sans-serif; font-size: 0.75rem; color: #64ffda; letter-spacing: 0.15em;">MODE</div>
            <div style="font-family: 'Orbitron', sans-serif; color: #e8ecf1; font-weight: 600; margin-top: 0.3rem;">{mode.upper()}</div>
        </div>
        <div>
            <div style="font-family: 'Orbitron', sans-serif; font-size: 0.75rem; color: #64ffda; letter-spacing: 0.15em;">FILE</div>
            <div style="font-family: 'Space Grotesk', sans-serif; color: #e8ecf1; margin-top: 0.3rem;">{image_name[:20]}</div>
        </div>
        <div>
            <div style="font-family: 'Orbitron', sans-serif; font-size: 0.75rem; color: #64ffda; letter-spacing: 0.15em;">SIZE</div>
            <div style="font-family: 'Space Grotesk', sans-serif; color: #e8ecf1; margin-top: 0.3rem;">{size_kb:.1f} KB</div>
        </div>
        <div>
            <div style="font-family: 'Orbitron', sans-serif; font-size: 0.75rem; color: #64ffda; letter-spacing: 0.15em;">STATUS</div>
            <div style="font-family: 'Orbitron', sans-serif; color: #64ffda; margin-top: 0.3rem;">● ONLINE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)