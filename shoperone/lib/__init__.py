import hashlib

def _hash_password(password):
    return hashlib.sha256(password).hexdigest()

