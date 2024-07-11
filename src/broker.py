import zmq

def broker():
    context = zmq.Context()

    # Socket para receber mensagens dos publicadores
    frontend = context.socket(zmq.SUB)
    frontend.bind("tcp://*:5555")
    frontend.setsockopt_string(zmq.SUBSCRIBE, "texto")

    # Socket para enviar mensagens aos assinantes
    backend = context.socket(zmq.PUB)
    backend.bind("tcp://*:5556")

    zmq.proxy(frontend, backend)

if __name__ == "__main__":
    broker()
