import socket # networking
import threading # multithreading

# pretending to have env vars
HOST = "127.0.0.1"
PORT = 5005

# global data
clients = []

# Broadcasts messages from one user to all others
def broadcast(data, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(data.encode())
            except:
                print("Connection closed.")
                clients.remove(client)

# Handles receiving data from individual clients
def handle_client(conn, addr):
    # log the connection
    print(f"New connection from {addr}.")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received from {addr}: {data}")
            broadcast(data, conn)
        except:
            break
        conn.close()
        clients.remove(conn)


# Main function, starts the server and accepts connections
def start_server():
    # start the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # no clue what the arguments do
    server.bind((HOST, PORT)) # it wants them like a tupple apparently
    server.listen()
    print(f"Server listening on {HOST}:{PORT}.")

    # await connections
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
