import timeit

def time_function(func, *args, repeat=100):
    return timeit.timeit(lambda: func(*args), number=repeat)

def save_results_to_file(results, filename="symmetric_results.txt"):
    with open(filename, "w") as file:
        file.write("Symmetric Encryption Performance Results\n")
        file.write("=" * 50 + "\n")
        file.write("Data Size (bytes) | AES Time (s) | DES Time (s)\n")
        file.write("-" * 50 + "\n")
        for data_size, aes_time, des_time in results:
            file.write(f"{data_size:15} | {aes_time:.6f} | {des_time:.6f}\n")
