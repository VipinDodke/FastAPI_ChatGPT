import fitz  # PyMuPDF
import io

def extract_text(file_bytes: bytes) -> str:
    doc = fitz.open("pdf", file_bytes)
    return "\n".join(page.get_text() for page in doc)
