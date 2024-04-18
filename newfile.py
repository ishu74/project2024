import pyrebase

# Firebase configuration
config = {
  "apiKey": "AIzaSyBGIdFvRQyfmfDK1U3k3JyAbslRbUYWaaA",
  "authDomain": "project24-f588a.firebaseapp.com",
  "projectId": "project24-f588a",
  "databaseURL" : "https://project24-f588a-default-rtdb.firebaseio.com",
  "storageBucket": "project24-f588a.appspot.com",
  "messagingSenderId": "1046264485880",
  "appId": "1:1046264485880:web:660f23a79f38141b6ba80d",
  "measurementId": "G-DVZGDSDT8E"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Define the path of the file in Firebase Storage
file_path = "path/in/firebase/storage/file.pdf"

# Define the local path where you want to save the downloaded file
local_path = "/path/to/save/downloaded_file.pdf"

# Download the file from Firebase Storage
storage.child(file_path).download(local_path)
