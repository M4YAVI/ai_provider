import os

import PyPDF2
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Get your Gemini API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Set your GEMINI_API_KEY in the .env file.")

# Create the GenAI client
client = genai.Client(api_key=api_key)  # You can also omit api_key if set in env

# Extract text from PDF
pdf_path = r"C:\Users\sange\Downloads\Principles2 cover (1)-merged.pdf"
with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    pdf_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            pdf_text += page_text + "\n"

# Compose your prompt
prompt = f"Summarize the main points of this PDF document:\n\n{pdf_text}"

# Use Gemini 2.5 Flash model (or 'gemini-2.5-pro' for higher quality)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
