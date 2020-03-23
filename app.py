from flask import Flask

app = Flask("PyRoute Server")

@app.route('/')
def hello_world():
    print('lol')
    return 'hello world'
