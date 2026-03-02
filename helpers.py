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
