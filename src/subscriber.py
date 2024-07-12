import zmq
import pyaudio

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

def subscriber_texto():
    socket.setsockopt_string(zmq.SUBSCRIBE, "texto")
    
    while True:
        message = socket.recv_string()
        print(f"Received text message: {message}")
        
def subscriber_audio():
    socket.setsockopt_string(zmq.SUBSCRIBE, "audio")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=1024)

    while True:
        data = socket.recv()
        stream.write(data)

if __name__ == "__main__":
    # subscriber_texto()
    subscriber_audio()