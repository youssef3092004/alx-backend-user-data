#!/usr/bin/env python3
import bycrypt
def _hash_password(password):
    return bycrypt.hashpw(password.encode('uft-8'), bycrypt.gensalt())
