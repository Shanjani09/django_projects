import requests as req
apiKey="3a4c9ae3f6084910895271d398e71f3f"
city="Narsapuram"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
response=req.get(url)
if response.status_code==200:
    weather_data=response.json()
    temp=weather_data['main']['temp']
    weatherDetails=weather_data['weather'][0]['description']
    print(f"Temperature in {city} is {temp}k")
    tempC=temp-273.5
    print(f"Temperature in {city} is {tempC}C")
    print(f"Weather in {city} is {weatherDetails}")
else:
    print("Failed to get info")