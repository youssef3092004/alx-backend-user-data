#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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
        """ Decodes the value of a base64 string """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decode_byets = base64.b64decode(
                base64_authorization_header)  # decode base64 to bytes
            return decode_byets.decode('utf-8')  # decode bytes to utf-8 string
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the
        Base64 decoded value
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        x = decoded_base64_authorization_header
        for i in range(len(x)):
            if x[i] == ':':
                return x[:
                         i], x[i + 1:]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None
        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        if self.authorization_header(request) is None:
            return None
        encoded = self.extract_base64_authorization_header(
            self.authorization_header(request))
        if encoded is None:
            return None
        decoded = self.decode_base64_authorization_header(encoded)
        if decoded is None:
            return None
        email, pwd = self.extract_user_credentials(decoded)
        if email is None or pwd is None:
            return None
        return self.user_object_from_credentials(email, pwd)
