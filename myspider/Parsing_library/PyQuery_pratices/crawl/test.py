import requests
from bs4 import BeautifulSoup

headers = {
    'user-Aagent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    ,
    'accept-encoding': 'gzip,deflate,br',

    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-04-01'
    ,
    ':authority': 'flights.ctrip.com',
    ':method': 'GET',
    ':path': '/itinerary/api/poi/get',
    ':scheme': 'https',
    'accept': '*/*'

}
login_url = 'https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-04-01'

respones = requests.get(login_url, headers)
soup = BeautifulSoup(respones, 'lxml')
print(soup)
