import requests
#API details
API_KEY= "dca6f46042d35fdd3995e73f36d92364"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"
# function to get weather data
def get_weather(city):
    try:
        # construct request url
        url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response= requests.get(url)
        if response.status_code==200:
            data= response.json()
            weather= {
                "City": data["name"],
                "Temperature": data['main']["temp"],
                "Weather": data['weather'][0]['description'],
                "Humidity": data['main']['humidity']
            }
            return weather
        elif response.status_code==404:
            return "City not found, Please check the name and try again.."
        else:
            return "Error fetching data. Please try again later.."
        # return response
    except requests.exceptions.RequestException as e:
        return f"An error Ocurred: {e}"

def main():
    print("Weather App")
    while True:
        city=input("\n Enter City name (or type exit):")
        if city.lower()== 'exit':
            break
        return get_weather(city)
        if isinstance(result, dict):
            print(f"\n weather in {result['city']}:")
            print(f"\n Teperature: {result['Temperature']}*C")
            print(f"\n Weather: {result['Weather']}")
            print(f"\n Humidity: {result['Humidity']}%")
        else:
            print(result)
if __name__ == "__main__":
    main()



# print(get_weather('London'))