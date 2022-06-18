
import yagmail
import os
from threading import Timer

# ! windsor yin 2022.06.18

def func():
    flag=file_detect()
    if flag == 1 :
        send_mail()

class RepeatingTimer(Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)

def file_detect():
    path = './Data0'      # 输入文件夹地址
    files = os.listdir(path)   # 读入文件夹
    num_file = len(files)       # 统计文件夹中的文件个数
    print(num_file)
    if num_file >= 3:
        flag = 1
    else:
        flag=0
    return flag

def send_mail():
    username = 'yinwenjie913@163.com'
    receiver1_name = '1403538271@qq.com'
    receiver2_name = '2016301200207@whu.edu.cn'
    yagmail.register(username, 'yinwenjie1998913')
    yag = yagmail.SMTP(username, host='smtp.163.com')
    mail_contents = '''Hello,
    代码出错了!!
    from python
    '''
    yag.send(to=[receiver1_name, receiver2_name],
             subject="我的提醒 from Python", contents=mail_contents)
    yag.close


if __name__ == "__main__":
    t = RepeatingTimer(10.0,func)
    t.start()

