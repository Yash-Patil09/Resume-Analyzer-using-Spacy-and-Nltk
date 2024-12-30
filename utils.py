import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join(page.extract_text() for page in reader.pages)
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens
