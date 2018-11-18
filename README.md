# Imprint CMS (Content Management System)

Seniors Honors Project by Raymond Gines.

Emulates the significant features of a modern day CMS such as Wordpress and Magento with adding posts and pages and creating an attractive web page up to modern standards of responsive design.

## Built With

* [Python]- Main programming language used
* [Flask]- Flask creates web
* [HTML] - Used to generate Flask templates
* [CSS] - Styles given templates
* [Javascript] - Used to change settings of website such as font size and family
* [Bootstrap](https://getbootstrap.com/) - Used for grid framework and responsive design

### Prerequisites

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

To reset and initialize the database:
```
flask init-db
```

## Deployment

Deployed to Heroku @ https://imprintcms.herokuapp.com/
