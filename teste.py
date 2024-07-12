import sys

import pyaudio

RECORD_SECONDS = 5
CHUNK = 1024
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print(p)
