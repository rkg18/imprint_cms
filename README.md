# Imprint CMS (Content Management System)

Seniors Honors Project by Raymond Gines (Due in April 2019)

Emulates the significant features of a modern day CMS such as Wordpress and Magento with adding posts and pages and creating an attractive web page up to modern standards of responsive design.

## Built With

* Python
* Flask - Web framework for Python
* HTML - Used to generate Flask templates that holds the content for pages and posts
* CSS - Styles given templates
* Javascript - Used to change settings of website such as font size and family
* [Bootstrap](https://getbootstrap.com/) - Used for grid framework and responsive design

## Requirements

* Python 3.x.x or higher
* Pip Package Manager + Python Libraries
```
pip install requirements.txt
```

### How to Run

To run on Windows 10 open 'Windows Powershell' and navigate to imprint_cms directory:

```
$env:FLASK_APP="imprint"
```
```
$env:FLASK_ENV="development"
```
```
flask run
```

To run on MacOS

```
export FLASK_APP=imprint
```
```
export FLASK_ENV=development
```
```
flask run
```

To reset and initialize the database:
```
flask init-db
```

Go to Browser and go to -> http://localhost:5000/

## Deployment

Deployed to Heroku @ https://imprintcms.herokuapp.com/
