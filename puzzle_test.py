import time
import psutil
from new_puzzle import validate_board as func2
from old_puzzle import validate_board as func1
def measure_performance(func, *args, repetitions=100, **kwargs):
    """
    Measure the average time and memory usage of a function.

    Args:
    - func (function): The function to be measured.
    - *args, **kwargs: Any additional arguments and keyword arguments to pass to the function.
    - repetitions (int): Number of times to repeat the execution for averaging.

    Returns:
    - float: Average time of execution in seconds.
    - float: Average memory usage in MiB.
    """
    times = []
    memories = []

    for _ in range(repetitions):
        start_time = time.time()
        process = psutil.Process()
        func(*args, **kwargs)
        end_time = time.time()

        times.append(end_time - start_time)
        memories.append(process.memory_info().rss / (1024 ** 2))

    avg_time = sum(times) / repetitions
    avg_memory = sum(memories) / repetitions

    return avg_time, avg_memory

def compare_performance(func1, func2, input_data):
    """
    Compare the performance of two functions.

    Args:
    - func1 (function): First function to test.
    - func2 (function): Second function to test.
    - input_data (list): List of input data for testing.

    Returns:
    - dict: Dictionary containing the average time and memory usage for each function.
    """
    results = {'Function 1': {'Time': None, 'Memory': None},
               'Function 2': {'Time': None, 'Memory': None}}

    avg_time, avg_memory = measure_performance(func1, *input_data)
    results['Function 1']['Time'] = avg_time
    results['Function 1']['Memory'] = avg_memory

    avg_time, avg_memory = measure_performance(func2, *input_data)
    results['Function 2']['Time'] = avg_time
    results['Function 2']['Memory'] = avg_memory

    return results

# Example usage:
input_data = [
    [\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     925 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
]
]

results = compare_performance(func1, func2, input_data)
print("Comparison Results:")
print(f"Old puzzle: Average Time = {results['Function 1']['Time']:.6f} seconds, Average Memory = {results['Function 1']['Memory']:.6f} MiB")
print(f"New puzzle: Average Time = {results['Function 2']['Time']:.6f} seconds, Average Memory = {results['Function 2']['Memory']:.6f} MiB")
