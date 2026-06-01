# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os
import requests

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
MY_LAT = 53.288612 # Your latitude
MY_LONG = -6.164032 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5:
        if MY_LONG -5 < iss_longitude < MY_LONG + 5:
            return True
        return None
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if sunrise > time_now.hour > sunset:
    if is_iss_close:
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Space station alert\n\nLook up the ISS in sight!\n"
                    f"ISS Latitude: {iss_latitude}\nISS Longitude: {iss_longitude}"
            )
