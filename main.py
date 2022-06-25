import os
import re
import wolframalpha

from flask import Flask, redirect, render_template, session, url_for, request

#configure Wolfram Knowledge Database
client = wolframalpha.Client(os.environ['APP_ID'])

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    pass
  else:
    return render_template('question.html')

#wolfram configure continued:
def output(input):
  print("Answer to "+str(input)+"\n")
  try:
    res = client.query(input)
    print(next(res.results).text)
    print("\n")
    return
  except:
    return output("Provide a different question: ")
    
#Ask questions to the Wolfram Knowledgebase. 
#output("2+2")
#output("Volume of a Cylinder")
#output(input("Ask a question: "))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=81)