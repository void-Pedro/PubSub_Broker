import zmq
import pyaudio
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5555")

def send_text():
    while True:
        message = socket.recv_string()
        print(f"Received text message: {message}")
    
def send_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    while True:
        data = stream.read(1024)
        socket.send(data)
        time.sleep(0.01)

if __name__ == "__main__":
    send_text()
    # send_audio()
