#!/usr/bin/env python3
""" Authentication Module """

import bcrypt


def _hash_password(password) -> bytes:
    """ Returns a salted hash of the input password """
    hashed_password = bcrypt.hashpw(password.encode('uft-8'),
                                     bycrypt.gensalt())
    return hashed_password
