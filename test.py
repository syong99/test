# step 1
from pyannote.audio import Pipeline

# 올바른 Hugging Face 액세스 토큰을 사용합니다.
access_token = "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"

# step 2
# 화자 분리 모델을 로드합니다.
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=access_token
)

# step3
# 오디오 파일 경로를 지정합니다.
audio_file = "voice_test.wav"

# step4
# 오디오 파일에서 화자 분리를 수행합니다.
diarization = pipeline(audio_file)

# step 5
# 다이어리제이션 결과를 RTTM 형식으로 저장합니다.
output_rttm = "audio_test.rttm"
with open(output_rttm, "w") as rttm_file:
    diarization.write_rttm(rttm_file)

print(f"{output_rttm} 파일이 저장되었습니다.")
