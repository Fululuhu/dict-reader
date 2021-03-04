from gtts import gTTS

tts = gTTS('hello', lang='en')

print(tts.get_urls())
