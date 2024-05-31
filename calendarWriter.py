import datetime as dt
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from edookitScraper import *
from edoWorking import *
calID = "f3a94d107e225350eb5cb8c8ff8d13f53066acdb96206823d492fddd73c163ff@group.calendar.google.com"

lessons = (all_lessons())
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
  #dont touch this part
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
    #there you can

    for i in lessons:
        if format_check(i[0]) and format_check(i[1]):
          event = {
          "summary": i[3],
          "location": i[5],
          "description": i[4],
          "colorId": 6,
          "start": {
              #year, month, day, hour, minute, second
              "dateTime": i[0],
              "timeZone": "Europe/Prague",
          },
          "end":{
              "dateTime": i[1],
              "timeZone": "Europe/Prague",
          },
          }
          event = service.events().insert(calendarId=calID, body=event).execute()
          print("good")
        else:
          print("bad")

  except HttpError as error:
    print("An error occurred:", error)
if __name__ == "__main__":
  main()