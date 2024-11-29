import socket
import pickle

# Function to perform tasks assigned by master
def perform_task(task, data):
    # Perform the task (for demonstration purposes, we'll just print the received data)
    print("Task:", task)
    print("Data:", data)

# Socket slave server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 5000  # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as slave_server:
    # Connect to master
    slave_server.connect((HOST, 6000))

    # Sample task and data (replace with actual tasks and data)
    task = "Sample Task"
    data = [1, 2, 3, 4, 5]

    # Send task and data to master
    slave_server.sendall(pickle.dumps((task, data)))

    # Receive acknowledgment from master (optional)
    ack = slave_server.recv(1024)
    print("Acknowledgment received:", ack)

    # Perform assigned task
    perform_task(task, data)
