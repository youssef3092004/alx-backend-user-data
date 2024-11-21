#!/usr/bin/env python3
""" Authentication Module """

import bcrypt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password
