import pandas as pd
import pymongo

# 连接数据库
client = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format("admin", "admin123", '118.25.94.130', 27017))
db = client['Tieba']
table = db['tieba_2']

# 读取数据
data = pd.DataFrame(list(table.find()))

# 选择需要显示的字段
data = data[['title', 'author']]
# 打印输出
print(data)
