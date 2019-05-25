
## 1.Cookie和Session的区别
如果你登录知乎，填写过用户名、密码下次进来的时候不想再填写了，那么你在第一次登录后，服务器就会发送给你的浏览器一个Cookie，Cookie中包含了你的用户名、密码，下次再次发送请求给知乎的时候，浏览器会自动给请求加上Cookie，这样服务器就能知道你是谁。这就是Cookie的机制。 

但是这种机制是不安全的，当你本地Cookie被别人获取后，就能直接使用你的账号了。于是出现了session机制：当你第一次以用户名、密码登录知乎时，知乎服务器会自己生成一条Session Id和sesson Value保存在服务器端，同时将Session Id作为Cookie中的一个键值对返回给浏览器，当你第二次请求知乎服务器的时候，请求会自动加上Session Id，那么服务器端收到Session Id后，会在服务器上查询是否有此Session Id,如果查询到，那么就匹配到相应的Session Value，也就是包含用户名密码的部分，这时候服务器就能识别出来你是那个用户了。

明确一点：Session Value中包含的是加密的用户名、密码等用户的Profile，是存放在服务器端，同事每一个Session Id都是有一个有效期的，这两点保证了安全性。

####  参考https://blog.csdn.net/nvliba/article/details/80521348