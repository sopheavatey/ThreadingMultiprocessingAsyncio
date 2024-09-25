import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#  Function to check prime numbers in a chunk of numbers
def check_prime_chunk(numbers):
    return [num for num in numbers if is_prime(num)]

# Function to find prime numbers in a range using multiprocessing
def find_primes_in_range(numbers, chunk_size):
    # Divide numbers into chunks
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Use multiprocessing Pool to process chunks in parallel
    with multiprocessing.Pool() as pool:
        result_chunks = pool.map(check_prime_chunk, chunks)
    
    # Flatten the list of results
    primes = [prime for chunk in result_chunks for prime in chunk]
    return primes
