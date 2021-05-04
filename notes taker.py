import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)
try:
    text=r.recognize_google(audio)
except:
    print("i couldnt understand")
with open("json","a") as file:
    file.write("\n"  +text)
