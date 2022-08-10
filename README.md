# 🌦 SansWeather
---
### Link: https://sansweather.herokuapp.com
Python-DJango based weather app+openWeatherAPI

## 📒 Description

This app is created using python django framework which gives out the weather details of the specified city on the html template. openWeatherAPI is used in this project to access the url in which the request is passed and served on the rendered template. The city name is passed as a POST request to the def index(): function to get the appropiate data from api url.
(units=metric is passed in url after cityname to get the metric scale conversion of the default units specified in the api)

## 📝 Requirements:-

- asgiref==3.5.2
- Django==4.0.5
- gunicorn==20.1.0
- sqlparse==0.4.2
- django-heroku==0.3.1

## 📸 Screenshots

<img width="1440" alt="Screenshot 2022-07-03 at 1 40 54 AM" src="https://user-images.githubusercontent.com/80622561/177014913-fed9d4a3-9d22-4828-95df-74b5c5a5fe68.png">
