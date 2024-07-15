# T1 - Sistemas Distribuídos: Videoconferência
# Professor Doutor Fredy João Valente

# Integrantes do Grupo: 
# Bruno de Silveira Biaziolli - 760318
# Pedro Henrique Borges - 804071
# Rodrigo Takizawa Yamauchi - 800226
# Vinicius Marques Rodrigues - 790717
# 15/07/2024

import zmq
import pyaudio
import time
import sys
import cv2

CHUNK = 1024
RATE = 44100

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5555")

# Função mandar texto
def send_text():
    while True:
        message = "texto"
        socket.send_string(message)
        time.sleep(1)

# Função mandar áudio    
def send_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)#
    try:
        while True:
            data = stream.read(1024)
            socket.send(data)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

# Função mandar vídeo
def send_video():
    captureVideo = cv2.VideoCapture(0)
    try:
        while captureVideo.isOpened():
            ret, frame = captureVideo.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            socket.send(buffer)
            time.sleep(0.04)  # Aproximadamente 25 fps (1/0.04)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        captureVideo.release()

# Escolher via comentário 
if __name__ == "__main__":
    # send_text()
    # send_audio()
    send_video()
