import requests
import pytest

time = requests.get("http://127.0.0.1:5000/time")
print(time.status_code)
print("Time:")
print(time.text)

date = requests.get("http://127.0.0.1:5000/date")
print(date.status_code)
print("Date:")
print(date.text)

input_age = {'date': "11/20/1998", 'units': "years"}
age_diff = requests.post("http://127.0.0.1:5000/age", json = input_age)
print(age_diff.status_code)
print(f" Age in years: {age_diff.text}")

breakfast_hours = requests.get("http://127.0.0.1:5000/until_next_meal/breakfast")
print(breakfast_hours.status_code)
print("Hours till breakfast:")
print(breakfast_hours.text)

lunch_hours = requests.get("http://127.0.0.1:5000/until_next_meal/lunch")
print(lunch_hours.status_code)
print("Hours till lunch:")
print(lunch_hours.text)

dinner_hours = requests.get("http://127.0.0.1:5000/until_next_meal/dinner")
print(dinner_hours.status_code)
print("Hours till dinner:")
print(dinner_hours.text)
