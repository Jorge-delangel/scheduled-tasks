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
from twilio.rest import Client

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
#Open Weather credentials
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get(OWN_API_KEY)


#Twilio credentials
account_sid = os.environ.get(ASID)
auth_token = os.environ.get(AUTH_TOKEN)
my_twilio_num = os.environ.get(TWILIO_PHONE_NUMBER)


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
        msg=f"Subject:eather forecast\n\nBring your umbrella with you" 
else:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Weather forecast\n\nIt's a sunny day, Enjoy!"
