import concurrent.futures

# Function to calculate the sum of N numbers
def sum_of_numbers(numbers):
    return sum(numbers)

# Function to perform vector addition
def vector_addition(v1, v2):
    return [x + y for x, y in zip(v1, v2)]

if __name__ == "__main__":
    # Sample data
    numbers = [1, 2, 3, 4, 5]
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Multi-tasking using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Calculate sum of numbers
        sum_future = executor.submit(sum_of_numbers, numbers)
        # Perform vector addition
        vector_addition_future = executor.submit(vector_addition, vector1, vector2)

        # Get results
        total_sum = sum_future.result()
        result_vector = vector_addition_future.result()

        print("Sum of numbers:", total_sum)
        print("Vector addition result:", result_vector)
