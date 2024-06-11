from faster_whisper import WhisperModel
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = WhisperModel("arc-r/faster-whisper-large-v2-Ko", device='cpu')

segments, info = model.transcribe("voice_test.wav")
with open('trans.txt', 'w', encoding='UTF-8') as f:
    for segment in segments:
        text = ("[%.2fs -> %.2fs] %s \n" % (segment.start, segment.end, segment.text))
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        f.write(text)