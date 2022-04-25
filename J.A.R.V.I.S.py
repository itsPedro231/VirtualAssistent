import wolframalpha
import speech_recognition as sp
import pyttsx3 as tts
import os

recognizer = sp.Recognizer()
mic = sp.Microphone()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 145)
engine.setProperty('volume', 0.6)
psq = wolframalpha.Client('RJQ4PP-9W6U2V7785')
x = 0

def micInput():
  print('listening')
  try:
    with mic as source:
      audio = recognizer.listen(source, timeout=2)
      output1 = (recognizer.recognize_google(audio))
      print(output1)
  except:
    output1 = ' . '
  return output1        
  
def newNotes():
  tts.speak('what is the name of the note?')
  noteName = micInput()
  tts.speak('please tell me the note')
  noteContent = micInput()
  path = 'C:\jarvis_notes\\' + noteName + '.txt'
  newNote = open(path, 'w+')
  newNote.write(noteContent)
  newNote.close()

def deleteNotes():
  files = os.scandir('C:\jarvis_notes')
  tts.speak('which notes would you like to delete: ', files)

def readNotes():
  files = os.scandir('C:\jarvis_notes')
  content = 'available notes: ' + str(files)
  tts.speak(content)  

def notes():
  tts.speak('do you want to create, delete or display a note')
  
  output3 = micInput()
  output3 = output3.split()
  for x in output3:
      if x.lower() == 'create' or x.lower() == 'new' or x.lower == 'add':
        newNotes()
      elif x.lower() == 'delete':
        deleteNotes()
      elif x.lower() == 'display' or x.lower() == 'show':
        readNotes()  

while True:
  micResult1 = micInput().split()
  for x in micResult1:
    if x == 'jarvis' or x == 'Jarvis' or x == 'JARVIS':
      tts.speak('yes sir?')
      print("now")
      micResult2 = micInput()
      tempResult = micResult2
      tempResult = tempResult.split()
      print(tempResult)
      if isinstance(tempResult, list):
        for x in tempResult:
          print(x)
          if x.lower() == 'notes' or x.lower() == 'note':
            notes()
            break
          else:
            try:
              search = psq.query(micResult2)
              answer = (next(search.results).text)
              tts.speak(answer)
              print(answer)
              continue
            except:
              tts.speak("im sorry sir I couldnt find anything about that on my database")
              continue

    else: continue  
        

