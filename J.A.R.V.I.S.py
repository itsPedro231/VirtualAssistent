import wolframalpha
import speech_recognition as sp
import pyttsx3 as tts

recognizer = sp.Recognizer()
mic = sp.Microphone()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 145)
engine.setProperty('volume', 0.6)
psq = wolframalpha.Client('RJQ4PP-9W6U2V7785')
x = 0

def listen():
    with mic as source:
        try:
            audio = recognizer.listen(source)
            output1 = (recognizer.recognize_google(audio)).split()
            print(output1)
        except:
            x = 0
    return output1        

while x == 0:
    print('listening')
    output1 = listen()
    for y in output1:
        if y == 'jarvis' or y == 'Jarvis' or y == 'JARVIS':
            with mic as source:
                tts.speak('yes sir?')
                print("now")
                try:
                    output2 = listen()  
                except:
                    tts.speak('please try again')
                    print("try again")
                    continue
                try:
                    search = psq.query(output2)
                    answer = (next(search.results).text)
                    print(answer)
                    tts.speak(answer)
                except:
                    tts.speak("im sorry sir I couldnt find anything about that on my database")
                    continuea