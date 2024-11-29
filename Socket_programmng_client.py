import socket
import pickle

# Function to perform vector addition
def vector_addition(v1, v2):
    result = [x + y for x, y in zip(v1, v2)]
    return result

# Socket client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# Sample data
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to server
    client_socket.connect((HOST, PORT))
    # Send data to server
    client_socket.sendall(pickle.dumps(vector1))
    client_socket.sendall(pickle.dumps(vector2))

    # Receive result from server
    data = client_socket.recv(1024)
    result_vector = pickle.loads(data)

    print("Vector addition result:", result_vector)
