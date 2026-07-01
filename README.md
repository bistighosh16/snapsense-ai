# 🧑‍🚀 SnapSense AI

> **See Beyond the Pixels** — Multi-modal AI vision system that transforms any image into structured intelligence.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-a78bfa?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_4_Scout-f0abfc?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-93c5fd?style=for-the-badge)

**[🚀 Live Demo](https://snapsense-ai.streamlit.app/)** • **[✨ Features](#-features)**

</div>

---

## 🌊 About

**SnapSense AI** is a multi-modal vision intelligence platform that analyzes any image and extracts structured, actionable information. Built with cutting-edge vision AI (Llama 4 Scout), wrapped in a stunning **Liquid Mercury** UI with iridescent chrome aesthetics.

Drop a **receipt**, **handwritten note**, **code screenshot**, **flowchart**, or ANY image — and SnapSense will intelligently analyze it based on the selected mode.

---

## ✨ Features

### 🎯 5 Specialized Analysis Modes

- 🔮 **General Analysis** — Auto-detect and analyze any image intelligently
- 🧾 **Receipt Extractor** — Extract items, prices, totals, tax, and vendor info
- 📝 **Notes Reader** — Read handwritten/typed notes with structured summaries
- 💻 **Code Extractor** — Extract code from screenshots + explanations + issue detection
- 📊 **Diagram Analyzer** — Describe flowcharts, architectures, and diagrams

### 🎨 Premium UI/UX

- 🌊 **Liquid Mercury Theme** — Iridescent chrome aesthetics
- ✨ **Holographic animations** — Chrome flow, radar scanning, floating elements
- 💎 **Glass morphism** — Frosted panels with subtle depth
- 🧑‍🚀 **Astronaut mascot** — Because vision AI feels like space tech!
- 📱 **Responsive** — Works beautifully on any screen size

### 🚀 Powerful Backend

- ⚡ **Groq Vision API** — Powered by Llama 4 Scout (17B parameters)
- 🎯 **Mode-specific prompts** — Optimized for each analysis type
- 📥 **Multiple export formats** — Markdown, JSON, Plain Text
- 🖼️ **Multi-format support** — PNG, JPG, JPEG, WEBP

---


## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.11 |
| **Framework** | Streamlit |
| **AI Model** | Groq (Llama 4 Scout - Vision) |
| **Image Processing** | Pillow, PyMuPDF |
| **Styling** | Custom CSS (Liquid Mercury Theme) |
| **Fonts** | Syncopate, Space Grotesk, JetBrains Mono |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Groq API key ([get one free](https://console.groq.com))

### Installation

**Clone the repo:**
git clone https://github.com/bistighosh16/snapsense-ai.git
cd snapsense-ai


**Create virtual environment:**
py -3.11 -m venv venv
venv\Scripts\activate


**Install dependencies:**
pip install -r requirements.txt


**Setup environment variables:**

Create a `.env` file:
GROQ_API_KEY=your_groq_api_key_here


**Run the app:**
streamlit run app.py



Open [http://localhost:8501](http://localhost:8501) in your browser! 🚀

---

## 📁 Project Structure
snapsense-ai/
├── app.py # Main Streamlit application
├── config.py # Configuration and mode definitions
├── requirements.txt # Python dependencies
├── .env # Environment variables (not committed)
│
├── core/
│ ├── vision_engine.py # Groq Vision API integration
│ ├── image_processor.py # Image processing utilities
│ ├── output_formatter.py # Output formatting
│ └── pdf_handler.py # PDF handling
│
├── modes/
│ ├── general_mode.py # General analysis prompt
│ ├── receipt_mode.py # Receipt extraction prompt
│ ├── notes_mode.py # Notes reading prompt
│ ├── code_mode.py # Code extraction prompt
│ └── diagram_mode.py # Diagram analysis prompt
│
├── ui/
│ ├── theme.py # Liquid Mercury CSS theme
│ ├── components.py # Reusable UI components
│ └── animations.py # Animation effects
│
└── assets/
└── backgrounds/
└── hero-bg.jpg # Hero background image

text


---

## 🎨 Design Philosophy

**Liquid Mercury** theme was born from the vision that AI should feel:
- 🌊 **Fluid** — Analysis should flow naturally
- 💎 **Premium** — Quality tools deserve quality design
- ✨ **Iridescent** — Reflecting the many facets of intelligence
- 🧑‍🚀 **Cosmic** — Because vision AI is genuinely futuristic

---

## 🎯 Use Cases

- 🧾 **Expense tracking** — Snap receipts and get structured data
- 📚 **Study notes** — Digitize handwritten notes instantly
- 💻 **Code review** — Extract code from screenshots and analyze it
- 📊 **Documentation** — Convert diagrams to descriptions
- 🔍 **Content analysis** — Understand any image intelligently

---

## 🛣️ Roadmap

- [ ] Batch processing (multiple images at once)
- [ ] Image comparison mode
- [ ] Multi-language OCR support
- [ ] PDF page-by-page analysis
- [ ] History/session management
- [ ] API endpoint for programmatic access

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- ⭐ Star the repo if you love it!

---

## 📜 License

MIT License — feel free to use, modify, and distribute!

---

## 🙏 Acknowledgments

- **Groq** — For the incredible vision AI API
- **Streamlit** — For making beautiful data apps possible
- **Meta AI** — For the Llama 4 Scout vision model

---

## 👩‍💻 Author

**Vivi** — [@bistighosh16](https://github.com/bistighosh16)

- 🏆 National Hardware Hackathon Winner
- 🌟 Open Source Contributor
- 📦 PyPI Publisher ([NeonUI](https://pypi.org/project/neonui/))
- 💜 Building AI tools that make life easier

---

<div align="center">

**Made with 💜 in the void by Vivi** 🧑‍🚀✨

*Transmitted from Earth • Powered by Groq Vision*

</div>
