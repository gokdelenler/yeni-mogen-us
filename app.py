import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://gokdelenler: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@github.com/gokdelenler/ekle1 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 ekle1.py &")
