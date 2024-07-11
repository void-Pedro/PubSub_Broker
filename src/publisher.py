import zmq

def subscriber_text():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, "texto")

    while True:
        message = socket.recv_string()
        print(f"Received text message: {message}")

if __name__ == "__main__":
    subscriber_text()
