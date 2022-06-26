import os
import re
import wolframalpha
import requests
from flask import Flask, redirect, render_template, session, url_for, request

#configure Wolfram API
client = wolframalpha.Client(os.environ['APP_ID'])

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    question = request.form.get("question")
    try:
      res = client.query(question)
      answer = next(res.results).text
      return render_template('answer.html', answer=answer)
    except:
      return render_template('question.html')
  else:
    return render_template('question.html')

@app.route('/answer',methods=['POST','GET'])
def answer():
  if request.method == "POST":
    pass
  else:
    return render_template('question.html')

@app.route('/contact',methods=['POST','GET'])
def contact():
  if request.method == "POST":
    pass
  else:
    return render_template('contact.html')

#Astronomy Picture of the Day
@app.route('/apod',methods=['POST','GET'])
def contact():
  if request.method == "POST":
    pass
  else:
    #configure NASA APOD API
    #https://api.nasa.gov/planetary/apod
    BASE_URL = 'https://api.nasa.gov/planetary/apod?api_key=qhmH0gzI2wgmXWS8TQqcdVNebG9DiTetM83JJm8h'
    response = requests.get(f"{BASE_URL}")
    detail = response.json()
    print(detail)
    return render_template('apod.html', detail=detail)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=81)