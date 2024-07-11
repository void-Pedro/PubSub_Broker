import zmq

def subscriber_texto():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.setsockopt_string(zmq.SUBSCRIBE, "texto")
    
    while True:
        message = socket.recv_string()
        print(f"Received text message: {message}")

if __name__ == "__main__":
    subscriber_texto()
