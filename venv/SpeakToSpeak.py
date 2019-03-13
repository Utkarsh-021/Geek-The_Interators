from gtts import gTTS
import os
import speech_recognition as sr
import pyaudio

r=sr.Recognizer()

with sr.Microphone() as Audio_Source:
    print('Speak Anything...')
    audio=r.listen(Audio_Source)

try:

    mytext =r.recognize_google(audio)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("Aman.mp3")
    os.system("Aman.mp3")

except:
    print("Audio not clear...")