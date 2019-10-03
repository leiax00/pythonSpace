# coding: utf-8
from ftplib import FTP

f = FTP('192.168.1.105')
f.login('ubuntu', 'root')
f.cwd('/')
result = f.dir('/home/ubuntu')
print(result)
result = f.nlst('/home/ubuntu')
print(result)
f.cwd('/home/ubuntu')
f.rename('a.txt', 'aaa.txt')
f.quit()
