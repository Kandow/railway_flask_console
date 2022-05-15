from re import T
from socket import timeout
import time
import os
import subprocess
import threading
import shlex
# shell_cmd='cd /'
# cmd = shlex.split(shell_cmd)
# print(cmd)
# p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)

# while p.poll() is None:

#     p.stdin.flush()
#     line = p.stdout.readline()
#     line = line.strip()
#     line=line.decode('utf-8')
#     if line:
#         print(line)
def console():
    cmd=input('input command:')
    cmd = shlex.split(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE,timeout=10)
    while True:
        time.sleep(0.1)
        if not p.poll() is None:
            console()
        line = p.stdout.readline()
        line = line.strip()
        line=line.decode('utf-8')
        if line:
            print(line)
console() 