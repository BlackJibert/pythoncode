
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
html = requests.get(url,headers = headers).text

doc =pq(html)

items = doc('.explore-tab .feed-item').items()
for item in items:
	question = item.find('h2').text()
	author = item.find('.author-link-line').text()
	answer = pq(item.find('.content').html()).text()
	file = open('explort.txt','a',encoding = 'utf-8')
	file.write('\n'.join([question,author,answer]))
	file.write('\n'+ '='*50 +'\n')
	file.close()