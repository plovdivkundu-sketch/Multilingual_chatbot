from ollama_agent import chat_with_ollama
from stt import speech_to_text
from tts import text_to_speech
from utils.language_codes import SUPPORTED_LANGUAGES

def main():
    print("Welcome to the Multilingual Farmer Assistant (Type 'exit' to stop)\n")
    language = input(f"Choose language {list(SUPPORTED_LANGUAGES.keys())}: ").strip().lower()
    if language not in SUPPORTED_LANGUAGES:
        print("Language not supported.")
        return

    mode = input("Input mode? (text/voice): ").strip().lower()
    while True:
        if mode == 'voice':
            print("Please speak your question clearly...")
            user_query = speech_to_text(SUPPORTED_LANGUAGES[language])
            print(f"You said: {user_query}")
        else:
            user_query = input("Enter your question: ")

        if user_query.lower() == 'exit':
            break

        ollama_response = chat_with_ollama(user_query, language)
        print(f"Assistant: {ollama_response}")
        text_to_speech(ollama_response, language)

if __name__ == '__main__':
    main()
