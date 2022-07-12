from flask import Flask, jsonify, render_template, redirect
from flask_cors import CORS 
from werkzeug.exceptions  import NotFound, BadRequest, InternalServerError


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # return render_template('index.html', short_url='qwe123asd')
    return {"url": "qwe123asd"}


@app.errorhandler(NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
