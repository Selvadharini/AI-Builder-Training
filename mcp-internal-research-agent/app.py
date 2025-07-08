import os
from flask import Flask
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_APPLICATION_CREDENTIALS
from tools import mcp

# Load credentials for Docs & Drive
creds = service_account.Credentials.from_service_account_file(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
    scopes=[
      "https://www.googleapis.com/auth/documents.readonly",
      "https://www.googleapis.com/auth/drive.metadata.readonly",
    ]
)
mcp.docs_api  = build("docs",  "v1", credentials=creds)
mcp.drive_api = build("drive", "v3", credentials=creds)

app = Flask(__name__)
mcp.attach_routes(app)

if __name__ == "__main__":
    app.run(port=8000)