import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import mails


cred = credentials.Certificate("acs-flutter-firebase-adminsdk-39nhe-3e21c34b17.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

mails = mails.get_mails()
# print(mails)

data = {}

for i, mail in enumerate(mails):
	data[f"{i}"] = mail+'@gtu.edu.tr'

db.collection("res").document("staff_mails").set(data)