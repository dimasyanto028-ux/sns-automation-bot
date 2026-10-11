# build b4d31b67f6
# (auto) 199303
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
