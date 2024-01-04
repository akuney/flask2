from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
	print("Printing out for observability purposes.")
    return jsonify({"Message": "Is this branch going to auto-build?"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
