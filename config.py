"""SnapSense AI - Configuration"""

APP_NAME = "SnapSense AI"
APP_TAGLINE = "See beyond the pixels 👁️✨"
APP_ICON = "👁️"
VERSION = "0.1.0"

# Groq model
VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Supported image formats
SUPPORTED_FORMATS = ["png", "jpg", "jpeg", "webp"]

# Mode definitions
MODES = {
    "general": {
        "name": "General Analysis",
        "icon": "🔮",
        "description": "Auto-detect and analyze any image intelligently",
        "color": "#a855f7",
    },
    "receipt": {
        "name": "Receipt Extractor",
        "icon": "🧾",
        "description": "Extract items, prices, totals from receipts",
        "color": "#22d3ee",
    },
    "notes": {
        "name": "Notes Reader",
        "icon": "📝",
        "description": "Read handwritten or typed notes and summarize",
        "color": "#f472b6",
    },
    "code": {
        "name": "Code Extractor",
        "icon": "💻",
        "description": "Extract code from screenshots and explain it",
        "color": "#4ade80",
    },
    "diagram": {
        "name": "Diagram Analyzer",
        "icon": "📊",
        "description": "Describe flowcharts, diagrams, and architectures",
        "color": "#fbbf24",
    },
}

# Output formats
OUTPUT_FORMATS = ["Markdown", "JSON", "Plain Text"]