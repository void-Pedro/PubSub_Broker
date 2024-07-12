import zmq
import pyaudio
import time
import sys

CHUNK = 1024
RATE = 44100

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5555")

def send_text():
    while True:
        message = "texto This is a text message"
        socket.send_string(message)
        time.sleep(1)
    
def send_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

    while True:
        data = stream.read(1024)
        socket.send(data)
        time.sleep(0.01)

if __name__ == "__main__":
    send_text()
    # send_audio()
