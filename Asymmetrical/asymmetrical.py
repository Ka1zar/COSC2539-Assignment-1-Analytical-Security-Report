import secrets
from asym_performance import performance_test_rsa, performance_test_ecc, save_results_to_file

def generate_random_data(size):
    """Generate random data of the specified size in bytes."""
    return secrets.token_bytes(size)


# Test data to compare algorithms
test_data = [
    b"Short message.",  # Small data
    b"This is a larger message to test the algorithms.",    # Large data
    generate_random_data(50),  # Random data, 50 bytes
    generate_random_data(100),  # Random data, 100 bytes
]

performance_results = []

# Run performance tests
for data in test_data:
    rsa_time = performance_test_rsa(data)
    ecc_time = performance_test_ecc(data)
    performance_results.append((len(data), rsa_time, ecc_time))

# Save results to file
save_results_to_file("asymmetric_results.txt", performance_results)

# Print results
for data_size, rsa_time, ecc_time in performance_results:
    print(f"Data Size: {data_size} bytes | RSA Time: {rsa_time:.6f}s | ECC Time: {ecc_time:.6f}s")
