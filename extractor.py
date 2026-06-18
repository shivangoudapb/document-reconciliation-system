import os
import json

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_document(pdf_path):

    uploaded_file = client.files.upload(
        file=pdf_path
    )

    prompt = """
Extract all information from this document.

Return ONLY valid JSON.

{
  "document_type": "",
  "order_number": "",
  "customer": "",
  "items": [
    {
      "sku": "",
      "description": "",
      "quantity": 0,
      "unit_price": 0
    }
  ]
}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    text = response.text

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)