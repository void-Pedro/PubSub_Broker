#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from random import randint

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
tempoTotal = 0
qtdMsgs = 0

while True:
    #  Wait for next request from client
    message = socket.recv()
    # inicio = time.time()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(randint(1, 10))

    #  Send reply back to client
    # fim = time.time()
    # tempoTotal += fim - inicio
    qtdMsgs += 1
    # tempoMedio = tempoTotal / qtdMsgs
    print(f"Tempo: {fim-inicio}, {qtdMsgs} mensagens totais")
    print(f"Tempo Médio: {tempoMedio}")
    print(f"Tempo Total: {tempoTotal}")
    socket.send(b"World")
    
