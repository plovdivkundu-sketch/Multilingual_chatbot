import requests
import json

def chat_with_ollama(prompt, language):
    payload = {
    "model": "llama3",
    "messages": [
        {
            "role": "system",
            "content": f"You are a helpful farming assistant. Reply only in {language}. Be specific and keep your answers concise and not too long."
        },
        {"role": "user", "content": prompt}
    ]
}


    response = requests.post("http://localhost:11434/api/chat", json=payload, stream=True)
    result_text = ""

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                json_data = json.loads(decoded_line)
                part = json_data.get("message", {}).get("content", "") if "message" in json_data else json_data.get("response", "")
                result_text += part
            except json.JSONDecodeError:
                continue

    return result_text
