# 24SUM_Django-Learn
Django follows the MVT design pattern (Model View Template).

- Model - The data you want to present, usually data from a database.
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

-----

## W3 Notes

**Initial Setup**
Replace [``myworld``](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fcvk%2FDownloads%2F%5BCODE%5D%20Local%20Projects%2F24SUM_Django-Learn%2Fmyworld%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/cvk/Downloads/[CODE] Local Projects/24SUM_Django-Learn/myworld") with `[name]`. [``my_tennis_club``](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fcvk%2FDownloads%2F%5BCODE%5D%20Local%20Projects%2F24SUM_Django-Learn%2Fmy_tennis_club%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/cvk/Downloads/[CODE] Local Projects/24SUM_Django-Learn/my_tennis_club") with `[app_name]`

`python -m venv myworld`
`source myworld/bin/activate`
`django-admin startproject my_tennis_club`


`python3.11 manage.py runserver`

`python3.11 manage.py startapp [name]`
Apps == `web page` that has a specific purpose:
- homepage
- contact form
- members db

Specific app in here: list/register member in DB.

Views -> Takes HTTP requests & returns HTTP response such as a .html doc.

Routing.
`urls.py` support moving in between pages. The `main` `urls.py` (on the directory with *startproject*) can accommodate app-specific

Templates
Usually an html. To implement, return the html in `views.py`.Then tell Django members page exists vs settings py in `INSTALLED_APPS`.