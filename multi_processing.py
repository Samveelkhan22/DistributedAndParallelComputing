import multiprocessing

# Function to calculate the sum of N numbers
def sum_of_numbers(numbers, result):
    result.value = sum(numbers)

# Function to perform vector addition
def vector_addition(v1, v2, result):
    result.value = [x + y for x, y in zip(v1, v2)]

if __name__ == "__main__":
    # Sample data
    numbers = [1, 2, 3, 4, 5]
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Shared variable for storing results
    shared_sum = multiprocessing.Value('i')  # 'i' for integer
    shared_vector = multiprocessing.Array('i', len(vector1))  # 'i' for integer

    # Create processes for sum of numbers and vector addition
    sum_process = multiprocessing.Process(target=sum_of_numbers, args=(numbers, shared_sum))
    vector_addition_process = multiprocessing.Process(target=vector_addition, args=(vector1, vector2, shared_vector))

    # Start processes
    sum_process.start()
    vector_addition_process.start()

    # Wait for processes to finish
    sum_process.join()
    vector_addition_process.join()

    # Get results from shared variables
    total_sum = shared_sum.value
    result_vector = list(shared_vector)

    print("Sum of numbers:", total_sum)
    print("Vector addition result:", result_vector)
