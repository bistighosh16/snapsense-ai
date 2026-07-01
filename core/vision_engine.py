import base64
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class VisionEngine:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        self.model = "meta-llama/llama-4-scout-17b-16e-instruct"  # Vision-capable model

    def encode_image(self, image_bytes: bytes) -> str:
        """Convert image bytes to base64 string"""
        return base64.b64encode(image_bytes).decode("utf-8")

    def analyze_image(self, image_bytes: bytes, prompt: str):
        """Send image + prompt to Groq Vision model"""

        base64_image = self.encode_image(image_bytes)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content