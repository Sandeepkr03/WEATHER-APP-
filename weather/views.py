import requests
from django.shortcuts import render

def weather_view(request):
    if request.method == 'POST':
        location = request.POST['location']
        try:
            api_key = '8cafc7513b9b4042a7251622232306'
            response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}')
            data = response.json()

            if 'current' in data:
                temperature = data['current']['temp_c']
                humidity = data['current']['humidity']

                context = {
                    'location': location,
                    'temperature': temperature,
                    'humidity': humidity,
                }
            else:
                error_message = 'Weather data not available for the provided location'
                context = {
                    'location': location,
                    'error_message': error_message,
                }
        except requests.exceptions.RequestException as e:
            error_message = f'Request error: {str(e)}'
            context = {
                'location': location,
                'error_message': error_message,
            }

        return render(request, 'weather.html', context)

    return render(request, 'weather.html')
