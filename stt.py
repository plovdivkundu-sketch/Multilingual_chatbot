import speech_recognition as sr

def speech_to_text(language_code):
    # language_code example: 'en', 'hi', 'bn', 'pa'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not recognize your speech.")
        return ""
    except sr.RequestError:
        print("Network error. Speech recognition unavailable.")
        return ""
