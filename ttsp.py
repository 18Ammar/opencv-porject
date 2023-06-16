import pyttsx3
import speech_recognition
import speech_recognition as sr
import pyaudio

class AI():
    __name = ""
    __skill = []


    def __init__(self ,name = None):

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:

            self.__name = name
        print("listening")

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,value):
        sentence = "hello, my name is " + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    
    def listen(self):
        print("say something")
        with self.m as source:
            audio = self.r.listen(source)

        print("got it ")

        try:
            phrase = self.r.recognize_google(audio,show_all=False,language="")
            if "goodbye" in phrase :
                sentence = "alright"
                self.engine.say(sentence)
                self.engine.runAndWait()
            else:
                sentence = "ok , you said " + phrase
                self.engine.say(sentence)
                self.engine.runAndWait()


        except:
            print("sorry ")
            self.engine.say("sorry didn't  catch that ")
            self.engine.runAndWait()

        print("you said ",phrase)
        return phrase

