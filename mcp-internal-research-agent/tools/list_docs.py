from .mcp import register_tool, drive_api

@register_tool("/tools/list-docs")
def list_docs(params):
    """Return all Docs whose title contains “insurance”."""
    resp = drive_api.files().list(
        q="mimeType='application/vnd.google-apps.document' and name contains 'insurance'",
        fields="files(id, name)"
    ).execute()
    return {"docs": resp.get("files", [])}
