import requests

# asking the user for city they would like to get the forecast for
city = input ("Enter City name: ")
print(city)


print("Showing the weather for "+ city)

url = 'https://wttr.in/{}'.format(city)

#using the request to get the URL
res = requests.get(url)

print(res.text)