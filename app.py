from flask import Flask , redirect , request

app= Flask(__name__,"/static")

@app.route("/")

def MainPage_Blue():
    page=''
    with open("main_page.html","r",encoding='utf-8') as f:
        page=f.read()
    return page

@app.route("/error")
def error():
    page=''
    with open("404.html","r",encoding='utf-8') as f:
        page=f.read()
    return page

@app.route("/red")
def MainPage_Red():
    page=''
    with open("red.html","r",encoding="utf-8")as f:
        page=f.read()
    return page


@app.route("/green")
def MainPage_Green():
    page=''
    with open("green.html","r",encoding="utf-8")as f:
        page=f.read()
    return page

@app.route("/yellow")
def MainPage_Yellow():
    page=''
    with open("yellow.html","r",encoding="utf-8")as f:
        page=f.read()
    return page

if __name__=="__main__":
     app.run(host="0.0.0.0",port=81, debug=True)