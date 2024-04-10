from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time

# Authenticate with Google Drive API using credentials file
gauth = GoogleAuth()
gauth.LoadCredentialsFile(r"C:\Users\vaibh\OneDrive\Desktop\Hardware controller\client_secret_491473471330-jc5midjl15cfhoidmck4djum0adc363m.apps.googleusercontent.com.json")  # Path to your credentials file
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile(r"C:\Users\vaibh\OneDrive\Desktop\Hardware controller\client_secret_491473471330-jc5midjl15cfhoidmck4djum0adc363m.apps.googleusercontent.com.json")  # Save the credentials back to the file

# Connect to Google Drive
drive = GoogleDrive(gauth)

# ID of the folder to watch for changes
folder_id = '1YzQSV0OePMtwK0DfGcVONKBqxylTXHha'  # Replace with your folder ID

# Dictionary to store the last modified time of files
last_modified_times = {}

def download_file(file_id, destination_folder):
    file = drive.CreateFile({'id': file_id})  # Use the file_id parameter instead of hardcoding
    file.GetContentFile(destination_folder + file['title'])



def watch_folder(folder_id, destination_folder):
    while True:
        folder = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
        for file in folder:
            if file['id'] not in last_modified_times or file['modifiedDate'] > last_modified_times[file['id']]:
                print(f"New file detected: {file['title']}")
                download_file(file['id'], destination_folder)
                last_modified_times[file['id']] = file['modifiedDate']
        time.sleep(10)  # Check for new files every 10 seconds

# Replace 'your_folder_id_here' with your actual folder ID
folder_id = '1YzQSV0OePMtwK0DfGcVONKBqxylTXHha'

# Replace 'your_destination_folder_path' with your actual destination folder path
destination_folder = r"C:\Users\vaibh\OneDrive\Desktop\Arduino codes"


if __name__ == "__main__":
    watch_folder(folder_id, r"C:\Users\vaibh\OneDrive\Desktop\Arduino codes\\")  # Replace with your local folder path
