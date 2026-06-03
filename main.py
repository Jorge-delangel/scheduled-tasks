# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import smtplib
import os
import requests

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get(MY_EMAIL)
MY_PASSWORD = os.environ.get(MY_PASSWORD)
#Open Weather credentials
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b0aeeb3c52450f8cbb21a532c122dfee"

parameters = {
    "lat": 53.344101,
    "lon": -6.267490,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Weather forecast\n\nBring your umbrella with you; It's gonna be raining"
        )
