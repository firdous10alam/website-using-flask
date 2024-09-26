from flask import Flask, render_template

app = Flask(__name__)  # Flask object

@app.route("/")  # when a certain url is requested what should be returned.
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
