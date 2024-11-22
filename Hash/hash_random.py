import hashlib
import os
import timeit

# Generate a large random byte sequence (1 MB)
large_data = os.urandom(1024 * 1024)  # 1 MB


# Function to hash large data with MD5
def hash_large_md5():
    return hashlib.md5(large_data).hexdigest()


# Function to hash large data with SHA-256
def hash_large_sha256():
    return hashlib.sha256(large_data).hexdigest()


# Open a file to save results
with open("large_data_hashing_results.txt", "w") as file:
    file.write("Hashing Large Data (1 MB)\n")
    file.write("=" * 50 + "\n")

    # Measure MD5 time
    md5_time = timeit.timeit(hash_large_md5, number=10)
    # Measure SHA-256 time
    sha256_time = timeit.timeit(hash_large_sha256, number=10)

    # Write the results to the file
    file.write(f"MD5 Time (10 runs): {md5_time:.6f} seconds\n")
    file.write(f"SHA-256 Time (10 runs): {sha256_time:.6f} seconds\n")

print("Results saved to 'large_data_hashing_results.txt'")
