from dotenv import load_dotenv
import os

load_dotenv()

# Google Docs & Drive (service-account JSON)
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Google Gemini API Key
GEMINI_API_KEY             = os.getenv("GEMINI_API_KEY")

# Google Docs IS
GOOGLE_DOC_ID              = os.getenv("GOOGLE_DOC_ID")

# Google Custom Search Engine (CSE)
CSE_ID                     = os.getenv("CSE_ID")
CSE_API_KEY                = os.getenv("CSE_API_KEY")
