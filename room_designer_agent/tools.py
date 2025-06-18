# tools.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_room_design(room_type: str) -> dict:
    """
    Generates interior design styles for a given room type.

    Args:
        room_type (str): The type of room (e.g., "kitchen", "bedroom").

    Returns:
        dict: A dictionary with design suggestions or an error message.
    """
    prompt = (
        f"You are an expert interior designer. Suggest 3–5 design styles for a {room_type}. "
        "Each suggestion should include the name of the style and a short description."
    )

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        styles_text = response.text.strip()
        styles_list = [line.strip() for line in styles_text.split("\n") if line.strip()]

        return {
            "status": "success",
            "styles": styles_list
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to generate design ideas: {str(e)}"
        }

