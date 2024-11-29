import socket
import pickle

# Function to calculate the sum of N numbers
def sum_of_numbers(numbers):
    result = sum(numbers)
    return result

# Socket server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432  # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen()

    print("Server is listening...")

    # Accept connections from clients
    conn, addr = server_socket.accept()
    with conn:
        print("Connected by", addr)
        # Receive data from client
        data = conn.recv(1024)
        numbers = pickle.loads(data)
        # Calculate sum of numbers
        total_sum = sum_of_numbers(numbers)
        # Send result back to client
        conn.sendall(pickle.dumps(total_sum))
