# Imprint CMS (Content Management System)

Seniors Honors Project by Raymond Gines (Due in April 2019)

The Imprint CMS (Content Management System) aims to emulate the key features of popular existing CMS applications such as Wordpress, Drupal, Magento, etc. This will be a lightweight alternative that can be used to kick start a digital presence by producing landing pages, product pages, and blog posts with ease. Individuals will be able to register and create their own account that will be secured in a database that they can use to login and manage their pages and posts. In addition, they will have the option of changing multiple settings such as the theme and color scheme of their website.

The overall goal is to be able to setup a website with the main features that can dynamically create pages on the fly and edit them as I wish. I want to be able to experience all levels of development from the front-end,back-end, and server-side to create a “significant” web application.

## Built With

* Python
* Flask - Web framework for Python
* HTML - Used to generate Flask templates that holds the content for pages and posts
* CSS - Styles given templates
* Javascript - Used to change settings of website such as font themes and row movement
* [Bootstrap](https://getbootstrap.com/) - Used for grid framework and responsive design

## Requirements

* Python 3.x.x or higher
* Pip Package Manager + Python Libraries
```
pip install -f requirements.txt
```

## How to Run

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
