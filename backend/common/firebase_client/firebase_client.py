import os

import firebase_admin
from firebase_admin import credentials


def init():
    try:
        gcp_firebase_project_id = os.environ.get('GCP_FIREBASE_PROJECT_ID')
        cred = credentials.ApplicationDefault()

        firebase_admin.initialize_app(credential=cred, options={
            'databaseURL': f'{gcp_firebase_project_id}.firebaseio.com/'
        })

    except Exception as e:
        print(e)
