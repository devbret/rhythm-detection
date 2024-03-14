import librosa
import numpy as np
import json

audio_paths = [
    'path/to/your/audio/files/song1.mp3',
    'path/to/your/audio/files/song2.mp3',
]

all_rhythm_data = {}

for audio_path in audio_paths:
    y, sr = librosa.load(audio_path, sr=None)

    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    rhythm_data = {
        "onset_times": onset_times.tolist()
    }

    filename = audio_path.split('/')[-1]
    all_rhythm_data[filename] = rhythm_data

with open('all_rhythm_data.json', 'w') as outfile:
    json.dump(all_rhythm_data, outfile)

print("All rhythm data has been written to all_rhythm_data.json")
