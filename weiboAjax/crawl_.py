from urllib.parse import urlencode
from pymongo import MongoClient
import requests

from pyquery import PyQuery as pq
# base_url来表示请求的Url的前半部分
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host':'m.weibo.cn',
    'Refer':'https://m.weibo.cn/u/2830678474',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    #构造参数字典，其中，type,value,和containerid是固定参数，page是可变参数
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }

    #调用urlencode()将参数转化为URl的GET参数，和base_url合并成新的URL，用requests请求这个链接
    #加入headers参数
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

#解析方法，从中提取有用的信息，可以先遍历cards，然后获取mblog的各个信息，赋值为一个新的字典返回即可
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            try:
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo
            except Exception as e:
                print(e)

#添加一个方法保存到mongodb
client = MongoClient()
db = client['weibo']
collection = db['weibo']
def save_to_mongo(result):
    if collection.insert(result):
        print('Save to MongoDB')

if __name__== '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
