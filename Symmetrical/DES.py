from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad


def adjust_des_key(key):
    # Ensure the key is valid for Triple DES
    while len(key) < 24:  # Pad to 24 bytes
        key += b'\0'
    return DES3.adjust_key_parity(key[:24])


def des_encrypt_decrypt(data, key):
    key = adjust_des_key(key)  # Ensure key is valid

    # Create Triple DES cipher object
    cipher = DES3.new(key, DES3.MODE_CBC)

    # Encrypt the data
    iv = cipher.iv  # Store the initialization vector
    ciphertext = cipher.encrypt(pad(data, DES3.block_size))

    # Decrypt the data
    cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), DES3.block_size)

    return ciphertext, decrypted_data, iv
