# T1 - Sistemas Distribuídos: Videoconferência
# Professor Doutor Fredy João Valente

# Integrantes do Grupo: 
# Bruno de Silveira Biaziolli - 760318
# Pedro Henrique Borges - 804071
# Rodrigo Takizawa Yamauchi - 800226
# Vinicius Marques Rodrigues - 790717
# 15/07/2024

import zmq

def broker():
    context = zmq.Context()

    # Socket para receber mensagens dos publicadores
    frontend = context.socket(zmq.SUB)
    frontend.bind("tcp://*:5555")
    #frontend.setsockopt_string(zmq.SUBSCRIBE, "texto", encoding='utf-8')
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")
    #frontend.setsockopt_string(zmq.SUBSCRIBE, "voz")

    # Socket para enviar mensagens aos assinantes
    backend = context.socket(zmq.PUB)
    backend.bind("tcp://*:5556")

    try:
        zmq.proxy(frontend, backend)
    except KeyboardInterrupt:
        print("Stopping...")

if __name__ == "__main__":
    broker()
