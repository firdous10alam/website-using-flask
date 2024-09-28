from flask import Flask, render_template, jsonify

app = Flask(__name__)  # Flask object

RECIPE = [{
    'id': 1,
    'name': 'Pizza',
    'ingredients': ['cheese', 'tomato', 'dough'],
    'Time': 30
}, {
    'id': 2,
    'name': 'Burger',
    'ingredients': ['cheese', 'tomato', 'bun'],
}, {
    'id': 3,
    'name': 'Chowmean',
    'ingredients': ['chow', 'tomato', 'vinegar'],
    'Time': 30
}, {
    'id': 4,
    'name': 'Pasta',
    'ingredients': ['pasta', 'tomato', 'pasta_masala'],
    'Time': 30
}]


@app.route("/")  # when a certain url is requested what should be returned.
def hello_world():
   return render_template('home.html',
                          recipies=RECIPE,
                          company_name='MasterChef')



@app.route("/list")
def list_item():
    return jsonify(RECIPE)


if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
