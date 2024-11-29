# Parallel and Distributed Computing: 

This repository demonstrates various parallel and distributed programming techniques using Python. The project includes implementations of multiprocessing, multithreading, socket programming, and distributed task execution. Below is a detailed description of each file and its functionality.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [File Descriptions](#file-descriptions)
   - [Local_variables.py](#local_variablespy)
   - [MSA_Master.py](#msa_masterpy)
   - [MSA_Slave.py](#msa_slavepy)
   - [multi_processing.py](#multi_processingpy)
   - [Multi_tasking.py](#multi_taskingpy)
   - [Multi_threading.py](#multi_threadingpy)
   - [Socket_programming_server.py](#socket_programming_serverpy)
   - [Socket_programming_client.py](#socket_programming_clientpy)
3. [Requirements](#requirements)
4. [Contributing](#contributing)
5. [License](#license)

---

## Project Overview

This project explores different methodologies for executing tasks in parallel and distributing them across processes, threads, and networked systems. These implementations are crucial for optimizing computational efficiency and demonstrating inter-process and inter-system communication.

---

## File Descriptions

### Local_variables.py
This script demonstrates **local multiprocessing** by:
- Calculating the sum of a list of numbers.
- Performing vector addition between two vectors.
It uses the `multiprocessing` module to create separate processes for each task, showcasing how local parallelism can be implemented.

---

### MSA_Master.py
This script serves as the **master server** for a distributed task management system:
- Distributes tasks and data to connected slave nodes.
- Listens for incoming connections from slave nodes and processes their responses.
- Utilizes the `socket` module for communication and `pickle` for data serialization.

---

### MSA_Slave.py
This script acts as a **slave node** in the distributed system:
- Connects to the master server.
- Sends predefined tasks and data for demonstration purposes.
- Receives acknowledgment and prints the assigned task and data for verification.

---

### multi_processing.py
This script demonstrates the use of **shared memory** in multiprocessing:
- Calculates the sum of numbers and performs vector addition.
- Uses `multiprocessing.Value` and `multiprocessing.Array` to share results between processes.
It highlights how shared variables can be used to manage state across multiple processes.

---

### Multi_tasking.py
This script implements **multi-tasking** using the `concurrent.futures` module:
- Calculates the sum of numbers and performs vector addition using a `ThreadPoolExecutor`.
- Provides a simple and efficient way to manage multiple tasks concurrently without manually managing threads.

---

### Multi_threading.py
This script showcases **multi-threading** using the `threading` module:
- Creates separate threads to calculate the sum of numbers and perform vector addition.
- Demonstrates basic thread creation, execution, and synchronization using `join()`.

---

### Socket_programming_server.py
This script implements a **socket server** that:
- Listens for incoming connections from clients.
- Receives a list of numbers from the client, calculates their sum, and sends the result back.
- Uses the `socket` module for server-side network communication and `pickle` for data serialization.

---

### Socket_programming_client.py
This script acts as a **socket client** that:
- Connects to the server.
- Sends two vectors to the server for processing.
- Receives the result of vector addition from the server and prints it.

---

## Requirements

- Python 3.7 or later
- Modules:
  - `multiprocessing`
  - `concurrent.futures`
  - `threading`
  - `socket`
  - `pickle`

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, feature enhancements, or general improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
