from .mcp import register_tool, docs_api

def extract_text(elements):
    text = ""
    for el in elements:
        if "paragraph" in el:
            for run in el["paragraph"]["elements"]:
                if tr := run.get("textRun"):
                    text += tr.get("content", "")
    return text

@register_tool("/tools/get-doc")
def get_doc(params):
    doc_id = params.get("doc_id")
    if not doc_id:
        raise ValueError("Missing 'doc_id'")
    doc = docs_api.documents().get(documentId=doc_id).execute()
    content = doc["body"]["content"]
    return {"text": extract_text(content)}
