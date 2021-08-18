import os

import firebase_admin
from firebase_admin import credentials


def init():
    try:
        project_id = "finantial-engine-fb-default-rtdb"
        cred = credentials.ApplicationDefault()

        firebase_admin.initialize_app(credential=cred, options={
            'databaseURL': 'https://finantial-engine-fb-default-rtdb.firebaseio.com/'
        })

    except Exception as e:
        print(e)
