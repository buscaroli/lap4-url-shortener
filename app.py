import uuid
from flask import Flask, jsonify, render_template, redirect, request, url_for
from flask_cors import CORS 
from werkzeug.exceptions  import NotFound, BadRequest, InternalServerError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)

# # Database
# select a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialise the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

base_url = 'http://localhost:5000/'

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
        
        original_url = request.form["url-input"]
        shortened_url = base_url + str(uuid.uuid4())[:8]
        print('*'*10)
        print(original_url)
        print(shortened_url)

        new_url = Address(url=original_url, short_url=shortened_url)
        db.session.add(new_url)
        db.session.commit()
        # generate url
        # save to database
        # refer back to homepage
        return render_template('home.html', result=shortened_url)
    else:
        return render_template('home.html')
        # return {"url": "qwe123asd"}

# @app.route('/<surl>')
# def refer(surl):
#     url = db.session.query(surl)
#     return redirect(url_for(surl))

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
