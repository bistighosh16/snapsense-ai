"""Mode registry"""

from modes import general_mode, receipt_mode, notes_mode, code_mode, diagram_mode

MODE_PROMPTS = {
    "general": general_mode.PROMPT,
    "receipt": receipt_mode.PROMPT,
    "notes": notes_mode.PROMPT,
    "code": code_mode.PROMPT,
    "diagram": diagram_mode.PROMPT,
}

def get_prompt(mode: str) -> str:
    """Get the prompt for a specific mode"""
    return MODE_PROMPTS.get(mode, MODE_PROMPTS["general"])