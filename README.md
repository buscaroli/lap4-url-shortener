# lap4-url-shortener

This is a url shortener that allow a user to add a link and get a shortened version of it that can be pasted in the address bar of their browser.
The client is rendered server side using a templating engine (Jinja2).

## Deployment

The Url Shortener is currently deployed on [Heroku](https://alimat.herokuapp.com/).

## Installation & usage

- Clone or download code:
  - cd into the folder
  - in terminal run:
    1. pipenv shell
    2. pip install pipenv
    3. pipenv install
  - To run development mode:
    - pipenv run dev
    - open http://localhost:5000 to view it in your browser
    - remember to refresh the page upon code changes

## Technologies

- Python
- Flask
- Flask-sqlalchemy
- pytest and pytest-cov

## Challenges

- it was challenging to pass the data from the server to the templates only in specific cases

## Bugs

- Not deployed

## TODO

- Testing

## Contacts

[Alice Kreslin](https://github.com/alicekres)
[Matteo Buscaroli](https://github.com/buscaroli)
