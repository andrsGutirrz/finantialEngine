"""TODO TO BE IMPLEMENTED"""
from common.firebase_client import firebase_client_base


class FirebaseClientMock(firebase_client_base.FirebaseClientBase):
    """
    Firebase client mock
    """

    def set_value(self, path: str, values: dict):
        pass

    def get_value(self, path: str) -> dict:
        pass

    def update_value(self, path: str, values: dict):
        pass

    def delete(self, path: str):
        pass
