import time
from RSA import rsa_generate_keys, rsa_encrypt_decrypt
from ECC import ecc_generate_keys, ecc_sign_verify

def performance_test_rsa(data):
    """Measure time for RSA encryption and decryption."""
    private_key, public_key = rsa_generate_keys()
    start_time = time.time()
    rsa_encrypt_decrypt(data, public_key, private_key)
    end_time = time.time()
    return end_time - start_time

def performance_test_ecc(data):
    """Measure time for ECC signing and verifying."""
    private_key, public_key = ecc_generate_keys()
    start_time = time.time()
    ecc_sign_verify(data, private_key, public_key)
    end_time = time.time()
    return end_time - start_time

def save_results_to_file(filename, results):
    """Save performance results to a text file with descriptive labels."""
    with open(filename, 'w') as file:
        # Add a header explaining the content
        file.write("Asymmetric Encryption Performance Test Results\n")
        file.write("===========================================\n\n")

        # Add column headers
        file.write("Data Size (bytes) | RSA Time (seconds) | ECC Time (seconds)\n")
        file.write("-" * 50 + "\n")

        # Add the results
        for i, (data_size, rsa_time, ecc_time) in enumerate(results):
            label = f"Random Data {i+1}" if i > 0 else "Static Message"
            file.write(f"{label:<15} | {data_size:<17} | {rsa_time:<17.6f} | {ecc_time:<17.6f}\n")

    print(f"Results saved to {filename}")

