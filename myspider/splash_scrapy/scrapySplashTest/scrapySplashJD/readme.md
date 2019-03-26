# 根据关键字爬去京东
使用splash+scrapy 

第一步：
    运行splash:
        docker run -p 8050:8050 scrapyinghub/splash
     可以在本地localhost:8050进行检验

第二步：
    在setttings.py文件中进行如下配置：
    
    SPLASH_URL = 'http://localhost:8050'
    DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
    HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
    
    MONGO_URI = 'localhost'
    MONGO_DB = 'JD'
    
    KEYWORDS = ['iPad']
    MAX_PAGE = 3
    
    