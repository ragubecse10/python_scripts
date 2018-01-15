#!/usr/bin/env python

import sys, paramiko


hostname = "localhost"
password = "test1234"
command = "cat /proc/uptime | awk '{print $1}'"

username = "ragu"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print round(float(stdout.read())/3600,2),

finally:
    client.close()
