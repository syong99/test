from gtts import gTTS
import playsound

fileName = "ttsFole.mp3"

text = STT.GetSpeechText()
print("음성 : " + text)
TTS.SpeakText(text)

def SpeakText(text):
    SaveMp3File(text)
    playsound.playsound(fileName)
    print(text)

def SaveMp3File(text):
    tts = gTTS(text=text, lang='ko')
    tts.save(fileName)