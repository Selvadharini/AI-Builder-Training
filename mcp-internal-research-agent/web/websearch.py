import requests
from config import CSE_ID, CSE_API_KEY
import os

def google_search(query, num=5):
    resp = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={
          "q": query,
          "cx": CSE_ID,
          "key": CSE_API_KEY,
          "num": num
        }
    ).json()
    return [
      {"title":i["title"], "link":i["link"], "snippet":i["snippet"]}
      for i in resp.get("items", [])
    ]

GOOGLE_DOC_ID = os.getenv("GOOGLE_DOC_ID")