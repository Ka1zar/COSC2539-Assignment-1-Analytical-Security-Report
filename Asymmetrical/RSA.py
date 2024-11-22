from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

def rsa_generate_keys():
    """Generate RSA private and public keys."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt_decrypt(data, public_key_bytes, private_key_bytes):
    """Encrypt and decrypt data using RSA keys."""
    public_key = RSA.import_key(public_key_bytes)
    private_key = RSA.import_key(private_key_bytes)

    # Encrypt with the public key
    cipher_rsa = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    ciphertext = cipher_rsa.encrypt(data)

    # Decrypt with the private key
    cipher_rsa = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)
    plaintext = cipher_rsa.decrypt(ciphertext)

    return ciphertext, plaintext
