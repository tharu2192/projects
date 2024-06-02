
# Create your views here.


from django.shortcuts import render
import requests

def get_weather(city):
    api_key = 'f104b208f514f770ce576abf8b70d456'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def weather(request):
    city = request.GET.get('city', 'New York')  # Default to New York if city is not provided
    weather_data = get_weather(city)
    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon']
    }
    return render(request, 'weather_app/weather.html', context)
