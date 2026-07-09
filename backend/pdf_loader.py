import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a normal PDF.

    OCR support has been removed for the Render deployment
    to reduce memory usage.
    """

    document = fitz.open(pdf_path)

    full_text = ""

    for page in document:

        text = page.get_text()

        if text.strip():

            full_text += text

    document.close()

    if not full_text.strip():

        print("❌ No selectable text found in PDF.")

        return ""

    print("✅ Text extracted successfully")

    return full_text