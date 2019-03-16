## 获取携程机票信息

get_source(start_city, end_city, start_time, another_start_city=None, anoter_end_city=None,
                   another_start_time=None, end_time=None, single_trip=True, multipass=None)
# 参数

## 对于单程来说：

start_city:出发城市
end_city:目的城市
start_time:出发时间
其他参数为默认值None

###例如
source = xiecheng.get_source("北京", '上海', "2019-04-02")


##对于往返来说：

start_city:出发城市
end_city:目的城市
start_time:出发时间
another_start_city：默认值None
anoter_end_city:默认值None
another_start_time:默认值None
end_time:返回时间
single_trip:传入False
multipass:默认值None

###例如
source = xiecheng.get_source("北京", '上海', "2019-04-02", None, None, None, "2019-04-04", False, False)


##对于多程

start_city:出发城市1
end_city:目的城市1
start_time:出发时间1
another_start_city：出发城市2
anoter_end_city:目的城市2
another_start_time:出发时间2
end_time:默认值None
single_trip:默认值
multipass:传入True

### 例如
source = xiecheng.get_source("北京", '上海', "2019-04-02", "广州", "南京", "2019-04-04", None, None, True)
