import itchat
import requests

KEY = 'e4ac50ac3556477088af279fabae6982'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots = ['——By Black', '——By Youyou']
    reply = get_response(msg['Text'])
    return reply or defaultReply


itchat.auto_login(enableCmdQR=2)
itchat.run()
