# coding=utf-8
import socket
import telnetlib

host = '127.0.0.1'
port = 0
username = 'admin'
password = 'lax123456'
timeout = 5000
socket
finish = ':~$ '
command = 'ls'

telnet = telnetlib.Telnet(host, port, timeout)

telnet.read_until('login: ')
telnet.write(username + '\n')

telnet.read_until('password: ')
telnet.write(password + '\n')

telnet.read_until(finish)
telnet.write(command + '\n')

telnet.read_until(finish)
telnet.close()
