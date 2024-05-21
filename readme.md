# 24SUM_Django-Learn

-----

## W3 Notes

**Initial Setup**
> Replace `myworld` with `[name]`. `my_tennis_club` with `[app_name]`

`python -m venv myworld`
`source myworld/bin/activate`
`django-admin startproject my_tennis_club`


`python3.11 manage.py runserver`

`python3.11 manage.py startapp [name]`
> Apps == `web page` that has a specific purpose:
- homepage
- contact form
- members db

Specific app in here: list/register member in DB.

Views -> Takes HTTP requests & returns HTTP response such as a .html doc.

> Routing.
`urls.py` support moving in between pages. The `main` `urls.py` (on the directory with *startproject*) can accommodate app-specific

> Templates
Usually an html. To implement, return the html in `views.py`.Then tell Django members page exists vs settings py in `INSTALLED_APPS`.