from gtts import gTTS
import os
import tempfile
from utils.language_codes import SUPPORTED_LANGUAGES

def text_to_speech(text, language):
    lang_code = SUPPORTED_LANGUAGES[language]
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_path = fp.name
        tts.save(temp_path)
        os.system(f'start {temp_path}' if os.name == 'nt' else f'mpg123 {temp_path}')
    except Exception as e:
        print("Text-to-Speech error:", str(e))

