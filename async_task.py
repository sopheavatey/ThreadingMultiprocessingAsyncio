import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    """Asynchronously write data to a file."""
    print(f"Starting to write to {filename} (simulated duration: {duration} seconds)...")
    
    # Simulate file writing time using asyncio.sleep
    await asyncio.sleep(duration)
    
    # Write data to file asynchronously
    async with aiofiles.open(filename, 'w') as file:
        await file.write(data)
    
    print(f"Completed writing to {filename}.")

async def run_async_tasks():
    """Run multiple asynchronous file-writing tasks."""
    prime_data = [
        ('primes1.txt', 'Prime numbers: 2, 3, 5, 7, 11, ...', 2),
        ('primes2.txt', 'Prime numbers: 13, 17, 19, 23, 29, ...', 3),
        ('primes3.txt', 'Prime numbers: 31, 37, 41, 43, 47, ...', 1),
        ('primes4.txt', 'Prime numbers: 53, 59, 61, 67, 71, ...', 4),
        ('primes5.txt', 'Prime numbers: 73, 79, 83, 89, 97, ...', 5),
    ]
    
    # Create tasks for writing to multiple files concurrently
    tasks = [
        async_write_to_file(filename, data, duration)
        for filename, data, duration in prime_data
    ]
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)
    print("All asynchronous file-writing tasks completed.")
