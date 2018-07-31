ssh-keygen -t rsa -C "youremail@example.com"  #生成密钥

密钥位置：C:\Users\ZHJ\.ssh

在github创建远程库pythoncode

本地pythoncode与github进行关联： 
	git remote add origin git@github.com:BlackJibert/pythoncode.git

将本地内容推送到github
 git push -u origin master


 每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；