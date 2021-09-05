class FirebaseClientBase:
    """
    Firebase client interface
    """

    def set_value(self, path: str, values: dict):
        pass

    def get_value(self, path: str) -> dict:
        pass

    def update_value(self, path: str, values: dict):
        pass

    def delete(self, path: str):
        pass
