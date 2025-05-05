""""
https://api.coindesk.com/v1/bpi/currentprice/USD.json
https://api.coindesk.com/v1/bpi/currentprice.json

To send http request, we need to use requests

module:requests
pip install requests

"""
import requests
response=requests.get('http://maps.googleapis.com/maps/api/directions/json')
json_Info=response.json()
print(json_Info)



