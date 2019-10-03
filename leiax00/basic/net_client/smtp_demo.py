# coding: utf-8
import smtplib

sm = smtplib.SMTP('smtp.python.is.cool')
sm.set_debuglevel(1)
sm.sendmail('a@python.is.cool', ('b@python.is.cool', 'c@python.is.cool'),
            ''' From: a@python.is.cool\r\nTo: b@python.is.cool, b@python.is.cool\r\n
            Subject: test msg\r\n\r\nxxxxxx\r\n.
            '''
            )
