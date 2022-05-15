

from click import command
from flask import Flask, redirect
from flask import render_template
from flask import abort, request
import datetime
import os
import requests
from werkzeug.utils import secure_filename
import json
from flask_sock import Sock
from threading import Thread
import subprocess
import shlex

                 

def console(sock):
    shell_cmd=sock.receive()
    print(shell_cmd)
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        
        if line:
            sock.send(line)
            pass
        

app = Flask(__name__, template_folder='templates',
            static_folder='static', static_url_path='/')
sock = Sock(app)
path = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = 'static/'
@sock.route('/echo')
def echo(sock):

    while True:
        if not sock.connected:
            print('Client disconnected')
            break
        shell_cmd=sock.receive()
        print(shell_cmd)
        cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)

        while p.poll() is None:
            if not sock.connected:
                break
            p.stdin.flush()
            line = p.stdout.readline()
            line = line.strip()
            line=line.decode('utf-8')
            if line:
                sock.send(line)



@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
