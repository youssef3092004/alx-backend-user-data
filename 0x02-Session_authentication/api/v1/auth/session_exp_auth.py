#!/usr/bin/env python3
""" Module of Session Exp Auth """
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Exp Auth """

    def __init__(self):
        """ Constructor """
        SESSION_DURATION = getenv('SESSION_DURATION')
        try:
            session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0

    def create_session(self, user_id=None):
        """ Create a Session ID """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        created_at = session_dict.get('created_at')
        if 'created_at' not in session_dict:
            return None
        expierd_date = created_at + timedelta(seconds=self.session_duration)
        if expierd_date < datetime.now():
            return None
        return session_dict.get('user_id')
