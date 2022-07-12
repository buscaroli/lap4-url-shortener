import uuid
from flask import Flask, jsonify, render_template, redirect, request
from flask_cors import CORS 
from werkzeug.exceptions  import NotFound, BadRequest, InternalServerError
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

# # Database
# select a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialise the database
db = SQLAlchemy(app)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(500), nullable=False)
    
    def __str__(self):
        return f"<Address {self.id}>"


# routes

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        base_url = 'http://localhost:5000/'
        #original_url = request.form["url"]
        short_url = base_url + str(uuid.uuid4())[:8]
        print('*'*10)
        print(short_url)
        # generate url
        # save to database
        # refer back to homepage
    else:
        # return render_template('index.html', short_url='qwe123asd')
        return {"url": "qwe123asd"}


# error handling

@app.errorhandler(NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

# remove debugging mode once ready for deployment 

if __name__ == "__main__":
    app.run(debug=True)
