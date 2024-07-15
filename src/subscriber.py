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
import sys
import cv2
import numpy as np

CHUNK = 1024
RATE = 44100

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

# Função recebe texto
def subscriber_text():
    socket.setsockopt_string(zmq.SUBSCRIBE, "texto")
    
    while True:
        message = socket.recv_string()
        print(f"Received text message: {message}")
        
# Função recebe audio        
def subscriber_audio():
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)
    print("Receiving audio...")
    try:
        while True:
            data = socket.recv()
            #print(data)
            stream.write(data)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

# Função recebe vídeo
def subscriber_video():
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    cv2.namedWindow("Received Video", cv2.WINDOW_AUTOSIZE)
    print("Receiving video...")
    try:
        while True:
            buffer = socket.recv()
            np_arr = np.frombuffer(buffer, dtype=np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if frame is not None:
                cv2.imshow("Received Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        cv2.destroyAllWindows()

# Escolher via comentário 
if __name__ == "__main__":
    # subscriber_text()
    # subscriber_audio()
    subscriber_video()
