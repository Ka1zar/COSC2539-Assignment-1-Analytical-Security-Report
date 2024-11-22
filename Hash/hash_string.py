import hashlib
import timeit

# Function to hash using MD5
def hash_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

# Function to hash using SHA-256
def hash_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# List of strings to test
data_samples = [
    "What's up!",
    "This is a test string.",
    "1234567890",
    "Ever meet a fellow by the name of Hill?",
    "Data collection example for cryptography"
]

# Measure hashing time for each string
for data in data_samples:
    md5_time = timeit.timeit(lambda: hash_md5(data), number=1000)  # Repeat 1000 times
    sha256_time = timeit.timeit(lambda: hash_sha256(data), number=1000)
    print(f"Input: {data}")
    print(f"MD5 Time (1000 runs): {md5_time:.6f} seconds")
    print(f"SHA-256 Time (1000 runs): {sha256_time:.6f} seconds")
    print("-" * 50)

# Open a file to save results
with open("Hash_string_results.txt", "w") as file:
    file.write("Hashing Speed Test Results\n")
    file.write("=" * 50 + "\n")

    for data in data_samples:
        # Measure MD5 time
        md5_time = timeit.timeit(lambda: hash_md5(data), number=1000)
        # Measure SHA-256 time
        sha256_time = timeit.timeit(lambda: hash_sha256(data), number=1000)

        # Write the results to the file
        file.write(f"Input: {data}\n")
        file.write(f"MD5 Time (1000 runs): {md5_time:.6f} seconds\n")
        file.write(f"SHA-256 Time (1000 runs): {sha256_time:.6f} seconds\n")
        file.write("-" * 50 + "\n")

print("Results saved to 'Hash_string_results.txt'")
