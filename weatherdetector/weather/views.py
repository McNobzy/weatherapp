from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=6d37b9447a358bf294dbff22507e1ed0').read()
        json_data = json.loads(res)
        int_temp = json_data['main']['temp']
        data = {
            'city':city,
            'country_code': (json_data['sys']['country']),
            # 'coordinate': json_data['coord']['lon'], ' ',json_data['coord']['lat'],
            'temp': (json_data['main']['temp']),
            'pressure': (json_data['main']['pressure']),
            'humidity': (json_data['main']['humidity']),
            'int_temp': int_temp
        }
    else:
        city = ''
        data = {},
    return render(request, 'index.html', {'data':data})