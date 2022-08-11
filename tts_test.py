import pyttsx3 
tts = pyttsx3.init() 
voices = tts.getProperty('voices')

if(voices[1].name == 'Microsoft Maria Desktop - Portuguese(Brazil)'):
    tts.setProperty('voice', voices[1].id)
else:
    tts.setProperty('voice', 'brazil')

tts.say('4 horas da tarde de uma quarta-feira')
tts.runAndWait()