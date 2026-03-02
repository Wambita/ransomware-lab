from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import string
from cryptography.hazmat.backends import default_backend

def generate_token(length: int = 24) -> str:
    """
    Generate a cryptographically secure random recovery token.
    
    Args:
        length (int): Length of the token (default 24).
        
    Returns:
        str: Secure random token consisting of uppercase letters and digits.
    """
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# predefined passoword
TOKEN = generate_token()
PASSWORD =  "Insert token here"
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


