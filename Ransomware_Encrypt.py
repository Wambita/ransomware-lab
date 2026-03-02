import  os
import hashlib

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import platform

# predefined passoword
PASSWORD = "my_secure_password"

def derive_key(password: str, salt: bytes)-> bytes:
    """Derive a key from the password using Scrypt KDF."""
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt the data using AES-256-CBC."""
    # Generate a random salt
    salt = os.urandom(16)
    
    # Derive a key from the password and salt
    key = derive_key(password, salt)
    
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the data to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return the salt, IV, and ciphertext concatenated together
    return salt + iv + ciphertext

def encrypt_file(file_path: str, password: str):
    """Encrypt and delete the file at the given path."""
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    encrypted_data = encrypt_data(file_data, password)
    new_file_path = file_path + ".enc"
    # Write the encrypted data back to the file
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)
    os.remove(file_path)
    print(f"Encrypted and deleted: {file_path} -> {new_file_path}")