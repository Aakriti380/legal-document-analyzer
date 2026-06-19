from pypdf import PdfReader

def extract_pages(pdf_path):

    reader = PdfReader(pdf_path)

    pages = []

    for idx, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if page_text:

            pages.append({
                "page_number": idx + 1,
                "text": page_text
            })

    return pages 