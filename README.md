# Multilingual Farming AI Assistant Backend

This is a FastAPI backend application that integrates with Ollama local LLM models to provide a multilingual farming assistant AI chatbot. It accepts farming queries from clients and returns helpful advice in various languages.

---

## Features

- Built with FastAPI for a fast, robust API.
- Uses Ollama for local large language model chat completion.
- Supports input in multiple languages (English, Hindi, Bengali, Punjabi).
- Provides concise, specific farming advice.
- CORS enabled for frontend integration.

---

## Installation

1. Clone the repository:
git clone <your-repo-url>
cd <repo-folder>

text

2. Create a Python virtual environment and activate:
python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

text

3. Install dependencies:
pip install -r requirements.txt

text

---

## Running the Backend

Start the FastAPI server with uvicorn:

uvicorn backend:app --host 0.0.0.0 --port 5000 --reload

text

The backend will be available at: `http://localhost:5000/api/chat`

---

## API Endpoint

### POST `/api/chat`

Send a JSON POST request with:

- `message` (string): Your farming question or query.
- `language` (string, optional): Language code, e.g., `"english"`, `"hindi"`.

Example request body:

{
"message": "How to improve wheat production?",
"language": "english"
}

text

Example response:

{
"response": "Improving wheat production requires a combination of good agricultural practices..."
}

text

---

## Frontend Integration

You can connect any frontend to this backend. For a simple test, send POST requests to `/api/chat`.

---

## Notes

- Ensure Ollama local server is running and accessible at `http://localhost:11434`.
- Modify `backend.py` to adjust Ollama model or API endpoint if needed.
- In production, tighten CORS policy for security.

---

## License

MIT License © 2025 Your Name

---

## Contact

For questions or contributions, open an issue or contact [your-email@example.com].