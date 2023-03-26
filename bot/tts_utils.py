from gtts import gTTS

def text_to_speech(text, filename):
    tts = gTTS(text)
    tts.save(filename)