import requests

BASE_URL = "http://127.0.0.1:8000"


def health():
    """
    Check backend status.
    """
    try:
        response = requests.get(f"{BASE_URL}/health")
        return response.status_code == 200
    except Exception:
        return False


def chat(question, document):
    """
    Send a question to the backend.
    """

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "question": question,
            "document": document
        }
    )

    response.raise_for_status()

    return response.json()


def upload(file):
    """
    Upload a PDF to the backend.
    """

    files = {
        "file": (
            file.name,
            file.getvalue(),
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

    response.raise_for_status()

    return response.json()


def dashboard():
    """
    Fetch dashboard statistics.
    """

    response = requests.get(
        f"{BASE_URL}/dashboard"
    )

    response.raise_for_status()

    return response.json()


def get_documents():
    """
    Fetch all available indexed documents.
    """

    response = requests.get(
        f"{BASE_URL}/documents"
    )

    response.raise_for_status()

    return response.json()["documents"]