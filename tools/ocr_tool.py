import pytesseract
from PIL import Image

def ocr_tool(image_path: str) -> str:
    """Extract text from image using OCR."""
    text = pytesseract.image_to_string(Image.open(image_path))
    return text