import uuid
from flask import Flask, jsonify, flash, render_template, redirect, request, url_for
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

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# base_url = 'http://127.0.0.1:5000/'

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
        shortened_url = '' + str(uuid.uuid4())[:8]
        print('*'*10)
        print(original_url)
        print(shortened_url)


        if not original_url:
            flash('The URL is required!')
            return redirect(url_for('home'))

        new_url = Address(url=original_url, short_url=shortened_url)
        db.session.add(new_url)
        db.session.commit()
        # generate url
        # save to database
        # refer back to homepage
        app_path = request.host_url
        short_url_with_path = f"{app_path}{shortened_url}"
        print('* '*10)
        print(short_url_with_path)
        return render_template('home.html', original=original_url, result=short_url_with_path)
    else:
        return render_template('home.html')
        # return {"url": "qwe123asd"}

@app.route('/<surl>')
def refer(surl):
    # query the database to check if the short_url is there
    # if so redirect the user to it
    print('==  ==  ==  ==  ==  == ')
    print(surl)
    try:
        address_entry = db.session.query(Address).filter_by(short_url=surl).one()
        # print('*^'*6)
        # print(address_entry)
        url = address_entry.url
        # print('* '*10)
        # print(url)
        return redirect('http://' + url)
        # print('#'*10)
        
    except:
        print('^'*5)
        print('back to homepage')
        return render_template('home.html')
#
#   # if not redirect to the homepage
    # return render_template('home.html')

# error handling 
# as we are using dynamic strings some of them might need to go

@app.errorhandler(NotFound)
def handle_404(err):
    return  render_template('errors/404.html'), 404

@app.errorhandler(BadRequest)
def handle_400(err):
    return render_template('errors/405.html'), 400

@app.errorhandler(InternalServerError)
def handle_500(err):
    return render_template('errors/500.html'), 500

# remove debugging mode once ready for deployment 

if __name__ == "__main__":
    app.run(debug=True)
