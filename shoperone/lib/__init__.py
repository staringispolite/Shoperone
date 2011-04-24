import hashlib

"""
  Defines how we hash passwords. Nothing fancy for now.
  Params: password string
  Returns: hashed password as an ascii hex string
"""
def _hash_password(password):
    return hashlib.sha256(password).hexdigest()

