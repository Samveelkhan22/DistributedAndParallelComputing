import socket
import pickle

# Function to distribute tasks to slaves
def distribute_task(task, data):
    # Sample distribution logic: send task and data to each slave
    for slave_address in slave_addresses:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master_socket:
            master_socket.connect(slave_address)
            master_socket.sendall(pickle.dumps((task, data)))

# Sample slave addresses (replace with actual addresses)
slave_addresses = [('127.0.0.1', 5000), ('127.0.0.1', 5001)]

# Socket master server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 6000  # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master_server:
    # Bind the socket to the address
    master_server.bind((HOST, PORT))
    # Listen for incoming connections
    master_server.listen()

    print("Master server is listening...")

    while True:
        # Accept connections from slaves
        conn, addr = master_server.accept()
        with conn:
            print("Connected by", addr)
            # Receive task and data from slave
            task, data = pickle.loads(conn.recv(1024))
            # Process the task
            # For demonstration purposes, we'll just print the received data
            print("Task received:", task)
            print("Data received:", data)
