import time
import requests
import os

# Authorize
auth = os.environ.get("STRAVA_API")
auth = "Bearer 262b29f91c087435dcbaa77fb60139f2fdd2cdca"

before = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
after = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
page = 56 # Integer | Page number. Defaults to 1. (optional)
perPage = 56 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

url = "https://www.strava.com/api/v3/athlete"
try: 
    # List Athlete Activities
    api_response = requests.get(url = url, headers = {"Authorization": auth})
    print(api_response.text)
except:
    print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities:")