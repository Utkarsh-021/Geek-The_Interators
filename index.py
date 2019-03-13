from flask import Flask,render_template,request
import pymysql as ps
import func as ort
import speech_recognition as sr
import jsonify

r=sr.Recognizer()
app=Flask(__name__)

@app.route("/SpeechToText")
def SpeechToText():
    with sr.Microphone() as Audio_Source:
        print('Speak Anything...')
        audio = r.listen(Audio_Source)
    try:
        mytext = r.recognize_google(audio)
    except:
        print("Audio not clear...")
    return jsonify(result=mytext)

@app.route("/")
def appointment():
    return render_template("index.html")
app.run(debug=True)