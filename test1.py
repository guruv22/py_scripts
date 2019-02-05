#!/usr/bin/python

import getpass

from sshcmdexec import SshCmdExec

sess = SshCmdExec()
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
sess.login(hostname, username, password)
