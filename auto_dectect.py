
import yagmail
import os
from threading import Timer

# ! windsor yin 2022.06.18
global flag_num 
flag_num = 0

def func():
    global flag_num 
    temp_flag = flag_num
    flag_num=file_detect(temp_flag)
    if flag_num >= 1 and flag_num < 4 :
        print('发送邮件')
        send_mail()

class RepeatingTimer(Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)

def file_detect(flag):
    path = './Data0'      # 输入文件夹地址
    files = os.listdir(path)   # 读入文件夹
    num_file = len(files)       # 统计文件夹中的文件个数
    if num_file >= 3:
        flag = flag + 1
        print('自动检测程序运行中:异常' )
    else:
        flag=0
        print('自动检测程序运行中:正常' )
    return flag

def send_mail():
    username = 'yinwenjie913@163.com'
    receiver1_name = '1403538271@qq.com'
    receiver2_name = 'liuyiwuhan@whu.edu.cn'
    yagmail.register(username, 'yinwenjie1998913')
    yag = yagmail.SMTP(username, host='smtp.163.com')
    mail_contents = '''Hello,
    江夏流星雷达软件出错了!!
    from python
    '''
    yag.send(to=[receiver1_name],
             subject="我的提醒 from Python", contents=mail_contents)
    yag.close


if __name__ == "__main__":
    t = RepeatingTimer(30.0,func)
    t.start()

