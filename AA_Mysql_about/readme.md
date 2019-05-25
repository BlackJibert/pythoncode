# 安装mysql
- sudo apt-get update
- sudo apt-get -y mysql-server mysql-client
若上述步骤出现失败:
- 参考:https://blog.csdn.net/weixx3/article/details/80782479
- 或者参考:崔庆才网络爬虫第29页.
-重置mysql root用户的密码,参考:https://www.cnblogs.com/woshimrf/p/ubuntu-install-mysql.html
# 启动,关闭,重启mysql服务
- sudo service mysql start/stop/restart

# 连接mysql的root用户
- mysql -u root -p
接着输入密码:'123456'
