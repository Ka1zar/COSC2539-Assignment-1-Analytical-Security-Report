from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

def ecc_generate_keys():
    """Generate ECC private and public keys."""
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

def ecc_sign_verify(data, private_key, public_key):
    """Sign data with ECC private key and verify with public key."""
    h = SHA256.new(data)

    # Sign the data
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)

    # Verify the signature
    verifier = DSS.new(public_key, 'fips-186-3')
    verifier.verify(h, signature)
    return signature
