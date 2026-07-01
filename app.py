"""SnapSense AI - Main Application"""

import streamlit as st
from core.vision_engine import VisionEngine
from modes import get_prompt
from config import APP_NAME, APP_ICON, MODES
from ui.theme import apply_chrome_nebula_theme
from ui.components import (
    render_hero,
    render_mode_pill,
    render_section_divider,
    render_scanning_animation,
    render_footer,
    render_stats_bar,
)

# ============ PAGE CONFIG ============
st.set_page_config(
    page_title="SnapSense AI - Vision Intelligence",
    page_icon="🧑‍🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============ APPLY THEME ============
apply_chrome_nebula_theme()

# ============ SIDEBAR ============
with st.sidebar:
    st.markdown("### 🧑‍🚀 MISSION CONTROL")
    st.markdown("---")

    st.markdown("#### 🎯 SELECT MODE")
    mode_options = {f"{data['icon']} {data['name']}": key for key, data in MODES.items()}
    selected_label = st.selectbox(
        "Analysis Mode",
        list(mode_options.keys()),
        label_visibility="collapsed",
    )
    selected_mode = mode_options[selected_label]

    st.markdown(f"**{MODES[selected_mode]['icon']} {MODES[selected_mode]['name']}**")
    st.caption(MODES[selected_mode]['description'])

    st.markdown("---")
    st.markdown("### 📡 SYSTEM STATUS")
    st.markdown("**Model:** Llama 4 Scout")
    st.markdown("**Provider:** Groq")
    st.markdown("**Version:** 0.1.0")
    st.markdown("**Status:** 🟢 ONLINE")

    st.markdown("---")
    st.markdown("### 🌌 MODES AVAILABLE")
    for key, data in MODES.items():
        st.markdown(f"{data['icon']} **{data['name']}**")

    st.markdown("---")
    st.caption("🧑‍🚀 Transmitted from Earth")

# ============ MAIN CONTENT ============
render_hero()

# Show current mode
render_mode_pill(MODES[selected_mode]['name'], MODES[selected_mode]['icon'])

# Upload section
render_section_divider("📸 IMAGE UPLINK")

uploaded_file = st.file_uploader(
    "Upload an image for analysis",
    type=["png", "jpg", "jpeg", "webp"],
    help="Drop an image here or click to browse. Vision AI will analyze it based on the selected mode.",
)

if uploaded_file:
    image_bytes = uploaded_file.getvalue()
    size_kb = len(image_bytes) / 1024

    # Stats bar
    st.markdown("<br>", unsafe_allow_html=True)
    render_stats_bar(MODES[selected_mode]['name'], uploaded_file.name, size_kb)

    # Analysis section
    render_section_divider("🔬 VISION ANALYSIS")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("#### 📸 SOURCE IMAGE")
        st.image(uploaded_file, use_container_width=True)

    with col2:
        st.markdown("#### 🧠 AI ANALYSIS")

        # Show scanning animation
        placeholder = st.empty()
        with placeholder.container():
            render_scanning_animation()

        try:
            engine = VisionEngine()
            prompt = get_prompt(selected_mode)
            result = engine.analyze_image(image_bytes, prompt)

            # Clear scanning animation
            placeholder.empty()

            # Display result
            st.markdown(result)

            # Download section
            render_section_divider("📥 EXPORT DATA")

            col_a, col_b, col_c = st.columns(3)

            with col_a:
                st.download_button(
                    "📄 Markdown",
                    data=result,
                    file_name=f"snapsense_{selected_mode}.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            with col_b:
                st.download_button(
                    "📋 Plain Text",
                    data=result,
                    file_name=f"snapsense_{selected_mode}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

            with col_c:
                import json
                json_data = json.dumps({
                    "mode": selected_mode,
                    "file": uploaded_file.name,
                    "analysis": result,
                }, indent=2)
                st.download_button(
                    "🔧 JSON",
                    data=json_data,
                    file_name=f"snapsense_{selected_mode}.json",
                    mime="application/json",
                    use_container_width=True,
                )

        except Exception as e:
            placeholder.empty()
            st.error(f"🚨 Transmission failed: {str(e)}")

else:
    # Empty state
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="chrome-card" style="text-align: center; padding: 3rem;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🛸</div>
        <div style="font-family: 'Orbitron', sans-serif; color: #64ffda; letter-spacing: 0.2em; font-size: 1.1rem;">
            AWAITING IMAGE UPLINK
        </div>
        <div style="color: #c0c5ce; margin-top: 1rem; font-size: 0.9rem;">
            Upload an image above to begin vision analysis
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============ FOOTER ============
render_footer()