import requests

def weather_Finder():

    api_key = '5b1901873783446a969160045240401'
    base = 'https://api.weatherapi.com/v1/current.json'


    print('Rules:\nIf country, capital informtaion will be displayed \nNo abbreviations city/country should be entire name (Ex: USA must be United States of America)\n')
    location = input('Enter the location (city or country): ')
    headers = {
        'key': api_key,
        'q': location
    }


    response = requests.get(base, params=headers)

    # provides the temperature, wind, precipitation & humidity of location
    if response.status_code == 200:
        print('\n**Data according to www.weatherapi.com**\n')
        data = response.json()


        location_name = data['location']['name']
        location_region = data['location']['region']
        location_country = data['location']['country']
        temperature_metric = data['current']['temp_c']
        temperature_imperial = data['current']['temp_f']
        wind_metric = data['current']['wind_kph']
        wind_imperial =data['current']['wind_mph']
        precipitation = data['current']['precip_mm']
        humidity = data['current']['humidity']
        data_update =data['current']['last_updated']


        print(f"Data last updated: {data_update}")
        print(f'Location Name: {location_name} {location_region}, {location_country}')
        print(f'Temperature: {temperature_metric}°C / {temperature_imperial}°F')
        print(f'Wind: {wind_metric}kph / {wind_imperial}mph')
        print(f'Precipitation: {precipitation}mm')
        print(f'Humidity: {humidity}')

    else:
        print('Error')


weather_Finder()


