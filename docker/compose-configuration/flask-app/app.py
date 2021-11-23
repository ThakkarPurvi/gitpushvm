from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
  colour = "pink"
  return f"<body style='background-color:{colour};'>\n<h1>Hello Purvi.</h1>\n\n<h2>I'm currently learning Docker compose.</h2>\n\n<h2>Hope to successfully finish this tutorial.</h2>\n\n<h3>Thank you.</h3>"


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
