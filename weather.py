import requests

location = input("Enter your City:")
url = "https://api.weatherapi.com/v1/current.json?key=00d7a1fd076245dfb1f100017262410&q={location}"


response = requests .get (url)

print (response.status_code)
if response.status_code == 200:
    data=response.json()
    print (data ["current"] ["temp_c"])
    print(data ["current"]["condition"] ["text"])
    print (f"in {location}, the temperature is {data["current"] ["temp_c"]} degrees celcius, and the weather is {data ["current"] ["condition"] ["text"]} ")


