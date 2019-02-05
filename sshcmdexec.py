#!/usr/bin/python

import pxssh

class SshCmdExec(object):

	def __init__(self):
		self.hostname = None
		self.username = None
		self.password = None
		self.handle = None

	def login(self, hostname, username, password):
		self.hostname = hostname
		self.username = username
		self.password = password
		 
		try:                                                            
    			s = pxssh.pxssh()
    			#hostname = raw_input('hostname: ')
    			#username = raw_input('username: ')
    			#password = getpass.getpass('password: ')
    			s.login (hostname, username, password)
    			s.sendline ('uptime')  # run a command
    			s.prompt()             # match the prompt
    			print s.before         # print everything before the prompt.
    			s.sendline ('ls -l')
    			s.prompt()
    			print s.before
    			s.sendline ('df')
    			s.prompt()
    			print s.before
    			s.logout()
			self.handle = s
		except pxssh.ExceptionPxssh, e:
    			print "pxssh failed on login."
    			print str(e)
