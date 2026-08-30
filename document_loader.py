import os
import glob
from pypdf import PdfReader


DOCUMENT_FOLDER = "documents"


def extract_pdf_text(pdf_path):
    """
    Extract text from a PDF page by page.
    Returns a list of dictionaries containing text,
    source filename, and page number.
    """

    records = []

    try:
        reader = PdfReader(pdf_path)

        for page_number, page in enumerate(
            reader.pages,
            start=1
        ):
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""

            text = text.strip()

            if text:
                records.append(
                    {
                        "text": text,
                        "source": os.path.basename(pdf_path),
                        "page": page_number
                    }
                )

    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")

    return records


def load_documents(document_folder=DOCUMENT_FOLDER):
    """
    Load all PDF documents from the documents folder.
    """

    os.makedirs(
        document_folder,
        exist_ok=True
    )

    all_records = []

    pdf_files = glob.glob(
        os.path.join(
            document_folder,
            "*.pdf"
        )
    )

    for pdf_file in pdf_files:

        records = extract_pdf_text(
            pdf_file
        )

        all_records.extend(
            records
        )

    return all_records


def get_full_page_text(
    source,
    page_number,
    document_folder=DOCUMENT_FOLDER
):
    """
    Retrieve the complete text of a specific page
    from the original PDF.
    """

    source_file = os.path.join(
        document_folder,
        source
    )

    try:

        reader = PdfReader(
            source_file
        )

        if (
            page_number >= 1
            and page_number <= len(reader.pages)
        ):

            page = reader.pages[
                page_number - 1
            ]

            return (
                page.extract_text() or ""
            ).strip()

    except Exception as e:

        print(
            f"Source extraction error: {e}"
        )

    return ""