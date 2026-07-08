import fitz
import easyocr
import numpy as np

# ----------------------------------------
# Load EasyOCR Reader (loads once)
# ----------------------------------------

reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF.

    Strategy:
    1. Try normal text extraction.
    2. If no text is found, use OCR.
    """

    document = fitz.open(pdf_path)

    full_text = ""

    # ----------------------------------------
    # First Try: Normal PDF Text
    # ----------------------------------------

    for page in document:

        text = page.get_text()

        if text.strip():
            full_text += text

    # ----------------------------------------
    # If Text Found
    # ----------------------------------------

    if full_text.strip():

        document.close()

        print("✅ Normal PDF detected")

        return full_text

    print("📷 Scanned PDF detected")
    print("Running OCR...")

    # ----------------------------------------
    # OCR Extraction
    # ----------------------------------------

    full_text = ""

    for page in document:

        pix = page.get_pixmap(dpi=300)

        image = np.frombuffer(
            pix.samples,
            dtype=np.uint8
        ).reshape(
            pix.height,
            pix.width,
            pix.n
        )

        results = reader.readtext(
            image,
            detail=0
        )

        full_text += "\n".join(results)
        full_text += "\n"

    document.close()

    print("✅ OCR Completed")

    return full_text