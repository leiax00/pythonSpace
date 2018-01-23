# coding=utf-8
import socket
import telnetlib

host = '192.168.0.104'
port = 0
username = 'leiax00'
password = ''
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
