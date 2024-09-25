from re import DEBUG
from flask import Flask

app = Flask(__name__)  #Flask object

@app.route("/")  #when a certain url is requested what should be returned.
def hello_world():
  return "Assalamoalikum its working"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
