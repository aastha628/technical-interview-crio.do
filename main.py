import requests
from utils import Utils

city, start_date, end_date = Utils.take_input()
token = "1f381c8b0af1955d40ae9971ccdbb09b"
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={token}'
it_will_rain = False

r = requests.get(url)
data = r.json()

start_date = Utils.convert_dates(start_date)
end_date = Utils.convert_dates(end_date)

for item in data['list']:
    current_date = Utils.convert_dates(item['dt_txt'])
    
    if current_date>=start_date and current_date<=end_date:
        if 'rain' in item:
            print("ShouldTakeUmbrella")
            it_will_rain=True
            break
        
if not it_will_rain:
    print("NoNeedOfUmbrella")
