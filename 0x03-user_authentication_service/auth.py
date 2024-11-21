#!/usr/bin/env python3
import bycrypt
def _hash_password(password) -> bytes:
    """ Returns a salted hash of the input password """
    hashed_password = bycrypt.hashpw(password.encode('uft-8'), bycrypt.gensalt())
    return hashed_password
