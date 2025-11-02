import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_tool(image_path: str) -> str:
    """Extract text from image using OCR."""
    text = pytesseract.image_to_string(Image.open(image_path))
    return text