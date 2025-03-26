import socket # networking
import threading # multithreading

# pretend to have env vars
HOST = "127.0.0.1"
PORT = 5005

# connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
print("Connected to the server.")

# function to handle receiving and printing messages
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Connection closed.")
            client.close()
            break

# run that function on a separate thread
thread = threading.Thread(target=receive_messages, args=(client,)) # i hate that comma
thread.start()

# read messages from keyboard, sending to network
while True:
    message = input("You: ")
    client.send(message.encode())
