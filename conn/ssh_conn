# coding=utf-8

import paramiko

ip = '192.168.0.106'
port = 22
username = 'leiax00'
password = 'admin'

command = 'ls -al'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)
print '连接成功!!!'
stdin, stdout, stderr = ssh.exec_command(command)

for std in stdout.readlines():
    print std
ssh.close()
