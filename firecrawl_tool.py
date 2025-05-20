import requests
import os
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def resumir_url_com_firecrawl(url):
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "url": url
    }

    try:
        print(f"Fetching content from: {url}")
        response = requests.get(
            "https://api.firecrawl.dev/api/v1/fetch",
            params=params,
            headers=headers
        )

        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text[:200]}...")  # Debug line
        
        if response.status_code == 200:
            data = response.json()
            if "text" in data:
                return data["text"]
            elif "content" in data:
                return data["content"]
            else:
                print(f"Unexpected response structure: {data.keys()}")
                return "No content could be extracted from the page."
        else:
            error_message = f"Error fetching: {response.status_code} - {response.text}"
            print(error_message)
            return error_message
    except Exception as e:
        error_message = f"Request error: {str(e)}"
        print(error_message)
        return error_message


