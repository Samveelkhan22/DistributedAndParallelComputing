import multiprocessing

# Function to calculate the sum of N numbers
def sum_of_numbers(numbers):
    total_sum = sum(numbers)
    print("Local sum:", total_sum)

# Function to perform vector addition
def vector_addition(v1, v2):
    result_vector = [x + y for x, y in zip(v1, v2)]
    print("Local vector addition result:", result_vector)

if __name__ == "__main__":
    # Sample data
    numbers = [1, 2, 3, 4, 5]
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Create processes for sum of numbers and vector addition
    sum_process = multiprocessing.Process(target=sum_of_numbers, args=(numbers,))
    vector_addition_process = multiprocessing.Process(target=vector_addition, args=(vector1, vector2))

    # Start processes
    sum_process.start()
    vector_addition_process.start()

    # Wait for processes to finish
    sum_process.join()
    vector_addition_process.join()
