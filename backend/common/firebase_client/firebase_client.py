from typing import Union

from firebase_admin import db

from common.firebase_client import firebase_client_base


class FirebaseClientBase(firebase_client_base.FirebaseClientBase):
    """
    Firebase client interface
    """

    def set_value(self, path: str, values: Union[dict, str]):
        db.reference(path).set(values)

    def get_value(self, path: str) -> object:
        return db.reference(path).get()

    def update_value(self, path: str, values: dict):
        db.reference(path).update(values)

    def delete(self, path: str):
        db.reference(path).delete()
