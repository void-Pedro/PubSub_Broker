import zmq
import pyaudio
import sys

CHUNK = 1024
RATE = 44100

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
    stream = audio.open(format=audio.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                input=False,
                output=True,
                frames_per_buffer=CHUNK)
    print("Receiving audio...")
    
    try:
        while True:
            data = socket.recv()
            stream.write(data)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

if __name__ == "__main__":
    # subscriber_texto()
    subscriber_audio()