from datetime import datetime


def str_to_datetime(date: str):
    if date is None:
        return None
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
