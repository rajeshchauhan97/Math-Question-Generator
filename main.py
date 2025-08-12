import os
import re
import json
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import PROMPT
from doc_creator import create_word_document
from image_generator import create_placeholder_image

# Load environment variables
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Configure output directories
OUTPUT_DIR = "output"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ----------------------------
# Core Logic
# ----------------------------
def generate_questions_with_gemini():
    """Generates questions using Gemini API with proper error handling."""
    if not GEMINI_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print("Sending prompt to Gemini...")
    try:
        response = model.generate_content(PROMPT)
        if not response.text:
            raise ValueError("Empty response from Gemini API")
        
        # Clean and parse the JSON response
        cleaned_response = re.sub(r"^```json\s*|\s*```$", "", response.text.strip(), flags=re.MULTILINE)
        questions = json.loads(cleaned_response)
        
        if not isinstance(questions, list) or len(questions) != 2:
            raise ValueError("Invalid question format returned by Gemini")
            
        return questions
        
    except Exception as e:
        print(f"Error generating questions: {str(e)}")
        return None

def main():
    print("Starting question generation...")
    
    # Step 1: Generate questions
    questions = generate_questions_with_gemini()
    if not questions:
        print("Failed to generate questions. Exiting.")
        return
    
    # Step 2: Generate images and documents for each question individually
    for i, question in enumerate(questions, start=1):
        # Generate a unique path for each image
        image_prompt = question.get('image_description', question.get('question', ''))
        image_path = os.path.join(IMAGES_DIR, f"q{i}_image.png")
        
        create_placeholder_image(image_prompt, image_path)
        question['image_path'] = image_path
        
        # Generate a unique path for each document
        doc_path = os.path.join(OUTPUT_DIR, f"question_{i}_document.docx")
        create_word_document([question], doc_path)
        print(f"\nDocument successfully created at: {doc_path}")

    print("Check the output folder for generated files.")

if __name__ == "__main__":
    main()