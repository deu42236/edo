import datetime as dt
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from edookitScraper import *
calID = "f3a94d107e225350eb5cb8c8ff8d13f53066acdb96206823d492fddd73c163ff@group.calendar.google.com"

print(all_lessons())
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
  creds = None

  if os.path.exists("token.js"):
    creds = Credentials.from_authorized_user_file("token.json")

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh.token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
      creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    event = {
      "summary": "Hodina",                             #finalList[i][1]
      "location": "Ucebna",                            #finalList[i][3]
      "description": "ucitel",                         #finalList[i][2]               
      "colorId": 6,
      "start": {
        #year, month, day, hour, minute, second
        "dateTime": "2024-05-31T09:00:00",
        "timeZone": "Europe/Prague",
      },
      "end":{
        "dateTime": "2024-05-31T11:00:00",
        "timeZone": "Europe/Prague",
      },
      }
    event = service.events().insert(calendarId=calID, body=event).execute()
    event = {
      "summary": "Hodina",
      "location": "Ucebna",
      "description": "ucitel",
      "colorId": 6,
      "start": {
        #year, month, day, hour, minute, second
        "dateTime": "2024-05-30T09:00:00",
        "timeZone": "Europe/Prague",
      },
      "end":{
        "dateTime": "2024-05-30T11:00:00",
        "timeZone": "Europe/Prague",
      },
      }
    #event = service.events().insert(calendarId="primary", body=event).execute()

    print(f"Event created: {event.get('htmlLink')}")

  except HttpError as error:
    print("An error occurred:", error)
if __name__ == "__main__":
  main()