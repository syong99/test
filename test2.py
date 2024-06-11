from pydub import AudioSegment
from faster_whisper import WhisperModel
import os
import soundfile as sf
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Whisper 모델 로드
model = WhisperModel("arc-r/faster-whisper-large-v2-Ko", device='cpu')

# FFmpeg 설정
AudioSegment.converter = 'C:\\ffmpeg\\bin\\ffmpeg.exe'

# 무음 구간
silence_duration = 1000  # 1초
some_silence = AudioSegment.silent(duration=silence_duration)

# 오디오 파일 로드
my_audio = AudioSegment.from_wav("voice_test.wav")

# 결과를 저장할 빈 오디오 세그먼트
empty = AudioSegment.empty()
orig_seg_list = []

# RTTM 파일 읽기 및 처리
with open('audio_test.rttm') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    line_arr = line.split()

    # 구간 정보
    seg_start = float(line_arr[3].replace('.',''))
    seg_duration = float(line_arr[4].replace('.',''))
    seg_speaker = line_arr[7]
    seg_end = seg_start + seg_duration

    # 구간 오디오 추출
    segment_audio = my_audio[int(seg_start * 1000):int(seg_end * 1000)]

    # 오디오 데이터를 메모리에서 직접 처리
    audio_data = np.array(segment_audio.get_array_of_samples(), dtype=np.float32) / (1 << 15)

    # Whisper 모델을 통한 텍스트 변환
    segments, _ = model.transcribe(audio_data, language="ko")
    segment_text = ''.join([seg.text for seg in segments])
    
    # 결과 텍스트 저장
    full_string = (
        f"start = {seg_start} | end = {seg_end} | duration = {seg_duration} | "
        f"speaker = {seg_speaker} | text = {segment_text}\n"
    )
    orig_seg_list.append(full_string)

# 텍스트 파일로 저장
with open('audio_test.txt', 'w', encoding='UTF-8') as f:
    f.writelines(orig_seg_list)

print(orig_seg_list)
