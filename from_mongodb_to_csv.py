
##从Mongodb中导出数据保存到csv文件中
import csv

import pymongo


def file_to_csv():
    MONGODB = "172.25.2.60"
    DBPORT = 27017
    conn = pymongo.MongoClient(MONGODB, DBPORT)
    db = conn["eTensorDB"]
    _table = db["industry-news"]
    #本地生成的文件
    strFile = 'D:/industry-news.csv'
    #需要选取的字段
    headList = ['title', 'Time_Stamp', 'caption',
                'hour', 'industry', 'key', 'label',
                'link', 'query', 'time', 'website']

    csvFile3 = open(strFile, 'w', newline='',encoding='utf-8')
    writer2 = csv.writer(csvFile3)
    #插入表头
    writer2.writerow(headList)
    #从find的数据库中找到需要的字段
    for One in _table.find():
        OneList =[One['title'], One['Time_Stamp'],One['caption'], One['hour'],
        One['industry'],
        One['key'], One['label'],
        One['link'], One['query'],
        One['time'], One['website']]

        Two_List = []
        for One2 in OneList:
            One2= One2
            aaa = str(One2).replace('\xa0', '')
            Two_List.append(aaa)
        print(Two_List)

        writer2.writerow(Two_List)
    csvFile3.close()

file_to_csv()