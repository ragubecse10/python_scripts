import os
import subprocess

ret_code = subprocess.call(['ping', '-c', '5', '-W', '3', 'abc987.com'],stdout=open(os.devnull, 'w'),stderr=open(os.devnull, 'w'))
print ret_code
