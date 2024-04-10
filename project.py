from googleapiclient.discovery import build
from google.oauth2 import service_account
import io
from googleapiclient.http import MediaIoBaseDownload

# Define your credentials and API scope
# SCOPES = ['https://www.googleapis.com/auth/drive']
SCOPES = ['https://www.googleapis.com/auth/drive']
# project@my-project-final-year-418009.iam.gserviceaccount.com
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Replace with your service account credentials file

def download_file(file_id, file_name):
    # Authenticate and build the service
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # Download the file
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

if __name__ == "__main__":
    file_id = '1H-ymbdNZQONkYLtTo7Ere5H2MW-KkaGP'  # Replace with the ID of the file you want to download
    file_name = "Blink.ino"  # Replace with the desired name of the downloaded file
    download_file(file_id, file_name)
