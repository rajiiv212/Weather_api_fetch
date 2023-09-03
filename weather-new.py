import requests
import pandas as pd
import easygui

api_key = '42cd6963072b6d7f9b2a3197b320a7a6'
api_endpoint = 'http://api.openweathermap.org/data/2.5/weather'

JJ = easygui.fileopenbox()
df = pd.read_csv(JJ)
#Press Alt + tab 
# for fileopenbox

print(df.head())

df['temp'] = ''
df['humidity'] = ''
df['temp_min'] = ''
df['temp_max'] = ''
df['pressure'] = ''
df['lon'] = ''
df['lat'] = ''
df['sys'] = ''
df['country'] = ''
df['name'] = ''
df['humidity'] = ''
df['weather'] = ''
df['description'] = ''

print(df.head())

for i in range(0, 48):
    row = df.iloc[i]
    url = f"{api_endpoint}?q={row['Name of City']}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df.at[i, 'temp'] = data['main']['temp']
        df.at[i, 'humidity'] = data['main']['humidity']
        df.at[i, 'temp_min'] = data['main']['temp_min']
        df.at[i, 'temp_max'] = data['main']['temp_max']
        df.at[i, 'pressure'] = data['main']['pressure']
        df.at[i, 'lon'] = data['coord']['lon']
        df.at[i, 'lat'] = data['coord']['lat']
        df.at[i, 'sys'] = data['sys']
        df.at[i, 'name'] = data['name']
        df.at[i, 'weather'] = data['weather'][0]['main']
        df.at[i, 'description'] = data['weather'][0]['description']
        df.at[i, 'Status'] = 'Success'
        print(f"Success to retrieve data for index {i}, Name of City: {row['Name of City']}, Status Code: {response.status_code}")
    else:
        print(f"Failed to retrieve data for index {i}, Name of City: {row['Name of City']}, Status Code: {response.status_code}")
        df.at[i, 'Status'] = 'Failed'
    print(i)
    j = i


print(df.head())

df.to_csv('weather_output_data.csv', index=False)

print("Api-Hit Done")

# print(f"Api-Hit Done. Output file created."