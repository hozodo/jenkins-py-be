from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello Henkins!"

def func01():
    return "Hello Jenkins!"

def func02():
    return "Hello Hudson!"

def func03():
    return "Hello Jenkins, Where is Hudson!, I think he is gone"