from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for handling authentication in the API """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if the path requires authentication """
        # If the path is in excluded_paths, return False (no authentication required)
        # Otherwise, return True (authentication required)
        if path in excluded_paths:
            return False
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
