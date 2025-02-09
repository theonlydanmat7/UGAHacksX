import os
from google.oauth2 import service_account

# Path to the Google Cloud Service Account JSON file
GOOGLE_CREDENTIALS_PATH = "sorastts-b83f3a190855.json"

# Load the credentials from the JSON file
credentials = service_account.Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH)

# You can now use these credentials to authenticate Google Cloud API clients
