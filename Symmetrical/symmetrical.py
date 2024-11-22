from AES import aes_encrypt_decrypt
from DES import des_encrypt_decrypt
from sym_data import collect_test_data
from sym_performance import time_function, save_results_to_file

# Keys for AES and DES
aes_key = b"SecureAESKey123"  # 16 bytes for AES
des_key = b"SecureDESKey1234567890"  # 24 bytes for 3DES

# Collect test data
test_data = collect_test_data()

# Performance results storage
performance_results = []

for data in test_data:
    # AES encryption/decryption timing
    aes_time = time_function(aes_encrypt_decrypt, data, aes_key)

    # DES encryption/decryption timing
    des_time = time_function(des_encrypt_decrypt, data, des_key)

    # Append results (data size, AES time, DES time)
    performance_results.append((len(data), aes_time, des_time))

# Save results to file
save_results_to_file(performance_results)

# Print results
print("Symmetric Encryption Performance Results:")
for data_size, aes_time, des_time in performance_results:
    print(f"Data Size: {data_size} bytes | AES Time: {aes_time:.6f}s | DES Time: {des_time:.6f}s")
