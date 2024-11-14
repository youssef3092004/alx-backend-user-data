from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Authentication """

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID """
        pass
