#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for handling authentication in the API """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if the path requires authentication """
        if path in excluded_paths:
            return False
        if path is None:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'
        if path == excluded_path:
            return False
        if excluded_paths is None or not excluded_paths:
            return True
        return True


    def authorization_header(self, request=None) -> str:
        """ Retrieves the Authorization header from the request """
        if request is None:
            return None
        # Return the 'Authorization' header, or None if not present
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user based on the request """
        # Currently returning None, can be extended later with actual logic
        return None
