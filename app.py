from flask import Flask, request, make_response, render_template
from flask.json import jsonify

app = Flask(__name__)

products = [
    {
        "name": "Apple iPhone 12"
    },
    {
        "name": "Apple iPhone XR"
    },
    {
        "name": "Samsung Galaxy S8"
    },
    {
        "name": "Samsung TV"
    },
    {
        "name": "Application Software"
    },
    {
        "name": "Banana (Yellow)"
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    search_text = request.args.get("query").lower()
    filtered_list = list(filter(lambda x: search_text in x["name"].lower(), products))

    print(filtered_list) 

    return jsonify(filtered_list)

if __name__ == "__main__":
    app.run(debug=True)