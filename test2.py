from pydub import AudioSegment
from faster_whisper import WhisperModel
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = WhisperModel("arc-r/faster-whisper-large-v2-Ko", device='cpu')

AudioSegment.converter = 'C:\\ffmpeg\\bin\\ffmpeg.exe'

#some silence. Not really needed but add it to create some space between the segments
silence_duration = 1000
some_silence = AudioSegment.silent(duration=silence_duration) 

#my audio file from file
my_audio = AudioSegment.from_wav("voice.wav")

#an empty segemnt for new audio
empty = AudioSegment.empty()

orig_seg_list = []
new_seg_list = []

#read the RTTM file and process the contents
with open('audio_test.rttm') as f:
    lines = f.readlines()

for line in lines:
    line = line.replace('\r','').replace('\n','')
    line_arr = line.split(' ')
    
    #create variables we will need
    seg_start = int(line_arr[3].replace('.',''))
    seg_duration = int(line_arr[4].replace('.',''))
    seg_speaker = line_arr[7]
    seg_end = seg_start + seg_duration
    
    empty = empty.append(my_audio[seg_start:seg_end], crossfade=0)
    empty = empty.append(some_silence, crossfade=0)
    
    #prepare the text we will write to the original segmented start and end
    full_string = ("start = " + str(seg_start) + "|" + "end = "+str(seg_end)  + "|" + "during = " +str(seg_duration) + "|" + "speaker = " + str(seg_speaker) + "\n")
    orig_seg_list.append(full_string)
   
empty.export("voice.wav", format="wav")
with open('original_file.txt', 'w') as f:
    f.writelines(orig_seg_list)
    print(orig_seg_list)