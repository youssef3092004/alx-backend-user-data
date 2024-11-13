#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Basic Authentication Class """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decode_byets = base64.b64decode(
                base64_authorization_header)  # decode base64 to bytes
            return decode_byets.decode('utf-8')  # decode bytes to utf-8 string
        except Exception:
            return None
