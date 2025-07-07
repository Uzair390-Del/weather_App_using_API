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
        return response
    except requests.exceptions.RequestException as e:
        return f"An error Ocurred: {e}"
print(get_weather('London'))