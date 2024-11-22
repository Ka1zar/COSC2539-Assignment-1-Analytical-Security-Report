from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt_decrypt(data, key):
    # Ensure the key length is 16 bytes for AES-128
    key = key.ljust(16, b'\0')

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)

    # Encrypt the data
    iv = cipher.iv  # Store the initialization vector
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    # Decrypt the data
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)

    return ciphertext, decrypted_data, iv
