import pyttsx3
engine = pyttsx3.init()
user=input("enter any thing to convert into speech:")
engine.say(user)
engine.runAndWait()