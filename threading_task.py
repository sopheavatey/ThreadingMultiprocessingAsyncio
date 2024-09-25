import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Starting I/O task for {file_name} (duration: {duration} seconds)...")
    time.sleep(duration)  # Simulate the time delay for the I/O task
    print(f"Completed I/O task for {file_name}.")

def run_io_tasks():
    # Simulate downloading or processing 5 files with different durations
    file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
    durations = [3, 2, 4, 1, 5]  # Simulated durations for each task (in seconds)

    threads = []
    
    for file_name, duration in zip(file_names, durations):
        # Create a new thread for each I/O task
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All I/O tasks completed.")
