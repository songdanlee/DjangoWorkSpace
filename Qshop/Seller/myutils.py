import random


# 随机生成指定位数0-9a-zA-Z的验证码
def random_code(len=4):

    string = "".join([str(i) for i in range(0,10)])+"".join([chr(i)+chr(i).lower() for i in range(65,90)])
    return "".join([random.choice(string) for i in range(len)])


import json
import requests
from Qshop.settings import DING_URL


def sendDing(content,to="15037609692"):
    DING_URL = """https://oapi.dingtalk.com/robot/send?access_token=90b5894a1615f70278806be3dd9ce6cd7e959bc1093df9a3b2845e22ede24279"""
    headers = {
        "Content-Type": "application/json",
        "Charset": "utf-8"
    }
    requests_data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
            ],
            "isAtAll": True
        }
    }
    if to:
        requests_data["at"]["atMobiles"].append(to)
        requests_data["at"]["isAtAll"] = False
    else:
        requests_data["at"]["atMobiles"].clear()
        requests_data["at"]["isAtAll"] = True
    sendData = json.dumps(requests_data)
    response = requests.post(url=DING_URL, headers=headers, data=sendData)
    content = response.json()
    return content


import smtplib
from email.mime.text import MIMEText


class MailSender():

    def __init__(self,sender,recever,content,password,subject="",server="smtp.163.com",port=994):
        """
        :param sender: 发送方邮箱
        :param recever: 接收方邮箱 ,字符串存储 ','分割
        :param content: 发送正文
        :param password: 发送方授权码
        :param subject: 主题可以为空
        :param server: 邮件服务器地址
        :param port: 邮件服务器端口
        """
        self.subject = subject
        self.recever = "15037609692@163.com,"+recever
        self.content = content
        self.sender = sender
        self.password = password
        self.server = server
        self.port = port

        self.message = MIMEText(content, "plain", "utf-8")
        self.message["Subject"] = subject
        self.message["From"] = sender
        self.message["To"] = recever



    def send(self):
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
        smtp.login(self.sender, self.password)
        try:
            smtp.sendmail(self.sender, self.recever.split(","), self.message.as_string())

        except Exception as e:
            print(e)
        finally:
            if smtp:
                smtp.close()

import datetime

# 返回当月的datetime对象
def datetime_now():
    # now = datetime.datetime.now()
    now = datetime.datetime(2019,12,1)

    start = datetime.datetime(now.year,now.month,1)
    if now.month == 12:
        end = datetime.datetime(now.year+1,1,1)
    else:
        end = datetime.datetime(now.year,now.month+1,1)

    return start,end


if __name__ == '__main__':
    datetime_now()