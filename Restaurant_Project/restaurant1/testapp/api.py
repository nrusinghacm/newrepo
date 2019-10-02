import requests
import json

cities=['Bengaluru','Hyderabad','Mumbai','Delhi','Chennai']
citydetails=[]

headers = {
        "cache-control": "no-cache",
        "user-key": "17c5d22ee5ac8d2406d53afcde18a594"
}
for city in cities:
        url="https://developers.zomato.com/api/v2.1/cities?q="+city
        resp = requests.request("GET",url,headers=headers)
        txt = resp.text
        #print(type(txt))
        #obj = json.loads(txt)
        data = json.loads(txt)
        #print(type(obj))
        for item in data['location_suggestions']:
            print ( 'id is:' + str(item['id']))
            print ( 'name  : '+str(item['name']))
            print ("country_id : " + str(item['country_id']))
            print ( 'Country_name : '+ str(item['country_name']))
            print('#'*10)
