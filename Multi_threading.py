import threading

# Function to calculate the sum of N numbers
def sum_of_numbers(numbers):
    result = sum(numbers)
    print("Sum of numbers:", result)

# Function to perform vector addition
def vector_addition(v1, v2):
    result = [x + y for x, y in zip(v1, v2)]
    print("Vector addition result:", result)

if __name__ == "__main__":
    # Sample data
    numbers = [1, 2, 3, 4, 5]
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Create threads for sum of numbers and vector addition
    sum_thread = threading.Thread(target=sum_of_numbers, args=(numbers,))
    vector_addition_thread = threading.Thread(target=vector_addition, args=(vector1, vector2))

    # Start threads
    sum_thread.start()
    vector_addition_thread.start()

    # Wait for threads to finish
    sum_thread.join()
    vector_addition_thread.join()
