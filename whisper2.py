import speech_recognition as sr

text = STT.GetSpeechText()
print("음성 : " + text)

def GetSpeechText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성 인식 중...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language='ko-KR')
    except sr.UnknownValueError:
        print("음성 인식 불가")
    except sr.RequestError as e:
        print("Google Web Speech API 에러 발생: {0}".format(e))