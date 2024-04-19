'''
Module for testing.
'''
import time
import psutil

def measure_function_performance(func, *args, repetitions=10, **kwargs):
    """
    Measure the average time of compilation and memory usage of a specific function.

    Args:
    - func (function): The function to be measured.
    - repetitions (int): Number of times to repeat the execution for averaging.
    - *args, **kwargs: Any additional arguments and keyword arguments to pass to the function.

    Returns:
    - float: Average time of compilation in seconds.
    - float: Average memory usage in MiB.
    """
    compilation_times = []
    memory_usages = []

    for _ in range(repetitions):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        compilation_times.append(end_time - start_time)

        process = psutil.Process()
        mem_usage = process.memory_info().rss / (1024 ** 2)
        memory_usages.append(mem_usage)

    avg_compilation_time = sum(compilation_times) / repetitions
    avg_memory_usage = sum(memory_usages) / repetitions

    return avg_compilation_time, avg_memory_usage

def compare_versions_review(time1, memory1, time2, memory2):
    '''
    Prints results of comparing.
    '''
    print('Avarage results:')
    if time2 > time1:
        print(f'Version №1 is {time2-time1} faster.')
    else:
        print(f'Version №2 is {time1-time2} faster.')
    if memory2 > memory1:
        print(f'Version №1 is {memory2-memory1} more memory efficient.')
    else:
        print(f'Version №2 is {memory1-memory2} more memory efficient.')

def explain_review_solo(avg_time, avg_memory, reps):
    '''
    Just prints result with explaining.
    '''
    print(f"Average Compilation Time over {reps} repetitions: {avg_time:.4f} seconds")
    print(f"Average Memory Usage over {reps} repetitions: {avg_memory:.4f} MiB")

if __name__ == "__main__":
    #####################################################################################
    # Guys, edit this section as needed :)                                              #
    #####################################################################################

    REPETITIONS = 1000000
    # from acro_new import create_acronym as new
    # from acro_new import EXAMPLE as n
    # from acro_old import create_acronym as old
    from ceasar_new import caesar_encode as new
    from ceasar_new import EXAMPLE as n
    from ceasar_old import caesar_encode as old
    GROUPED_ARGS = True # if given all arguments as tuple change to True

    #####################################################################################
    # OUTPUT:                                                                           #
    #####################################################################################
    if GROUPED_ARGS:
        t1, m1 = measure_function_performance(old, *n, repetitions=REPETITIONS)
        t2, m2 = measure_function_performance(new, *n, repetitions=REPETITIONS)
    else:
        t1, m1 = measure_function_performance(old, n, repetitions=REPETITIONS)
        t2, m2 = measure_function_performance(new, n, repetitions=REPETITIONS)
    print('\nOld version:')
    explain_review_solo(t1, m1, REPETITIONS)
    print('\nNew version:')
    explain_review_solo(t2, m2, REPETITIONS)
    print('\nResults:')
    compare_versions_review(t1, m1, t2, m2)
