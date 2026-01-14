import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the password using bcrypt.
    Returns the hashed password (bytes).
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed


def verify_password(password: str, hashed_password: bytes) -> bool:
    """
    Verifies a password against an existing bcrypt hash.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
