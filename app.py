from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<h2>Here is an interesting xkcd cartoon for you: </h2>" \
           '<img src="https://cdn.shopify.com/s/files/1/0697/4249/3893/files/6c2a15bc59c706e2a5da7ebeb4050a8a995ef5c3_ARTBK_16C2S_26TN_0251.jpg?v=1775931609">'
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)