#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Basic Authentication Class """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header[6:]
        return None
