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
