import os
from langchain.text_splitter import CharacterTextSplitter
from google.oauth2 import service_account
from googleapiclient.discovery import build

GOOGLE_DOC_ID = "1pPTFV8JTaBWzOZeyfYrI-eOtjL-1B70zykz2LzIitQo"
GOOGLE_CREDS_PATH = os.path.join(os.path.dirname(__file__), "../google_creds.json")


def load_policies(chunk_size=1000, chunk_overlap=200):
    """
    Fetches the Google Doc, extracts its text, and splits into chunks.
    Returns a list of dicts: {"id": "doc_chunk<i>", "text": "<chunk text>", "source": "google_doc"}
    """
    # Authenticate with Google Docs API
    creds = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDS_PATH,
        scopes=["https://www.googleapis.com/auth/documents.readonly"]
    )
    service = build("docs", "v1", credentials=creds)
    doc = service.documents().get(documentId=GOOGLE_DOC_ID).execute()

    # Extract text from the document
    def extract_text(elements):
        text = ""
        for value in elements:
            if "paragraph" in value:
                for elem in value["paragraph"]["elements"]:
                    if "textRun" in elem:
                        text += elem["textRun"]["content"]
        return text

    full_text = extract_text(doc.get("body", {}).get("content", []))

    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(full_text)
    docs = []
    for i, chunk in enumerate(chunks):
        docs.append({
            "id": f"google_doc_chunk{i}",
            "text": chunk,
            "source": "google_doc"
        })
    return docs
