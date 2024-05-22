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

Models
Make a table with a class in `models.py`.

**After, manage.py:**
-> makemigrations [foldername]
-> migrate
*view SQL executions*
`py manage.py sqlmigrate members 0001` (refer to migrations for query number)

----
[Inserting data with Python shell](https://www.w3schools.com/django/django_insert_data.php)

After all that, you create a template and add to `views.py`.

----
{% block name %} can be used to replace .html files with one `master.html`. Think of `sync content` with notion. End with {% endblock %}. Make sure to {% extend master.html %} to the html files you were thinking of replacing.

----
Django admin has built-in CRUD. Make sure DEBUG=TRUE then head to `/admin`

____
### Syntax

**Vars**
You can create a variable in `views.py` via context. Or a variable in template with the `{%with var="content" %}` tag.

Normally, most of the external data you want to use in a template, comes from a model. To get data from the Member model, we will have to import it in the views.py file, and extract data from it in the view:

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
```

Now we can use the data in the template
```html
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>
```

On more programming logic with templates: [Template Tags](https://www.w3schools.com/django/django_template_tags.php)

> In Django templates, you typically use {{ }} to output variables or expressions. When you need to perform logic or control flow, you use {% %}.

You can also just add external html files via include.

Given
`<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>`, you can add withs to use laid out vars:
`{% include "mymenu.html" with me="TOBIAS" sponsor="W3SCHOOLS" %}`
____

When we fetch data from the model, it comes as a QuerySet object, with a similar format as the cars example above: a list with dictionaries.

[How to deal with displaying data.](https://www.w3schools.com/django/showdjango.php?filename=demo_templates_for3)

____

### QuerySet

**Limit to a single column (flat):**
`mydata = Member.objects.values_list('firstname', flat=True)`

**Return Specific Rows**
You can filter the search to only return specific rows/records, by using the `filter()` method.

**Field Lookups [Reference](https://www.w3schools.com/django/django_queryset_filter.php))**
Django has its own way of specifying SQL statements and WHERE clauses.

To make specific where clauses in Django, use "Field lookups".

____
**Collecting Static Files**

Mostly for styling man. Since we did some changes in the static mystyles.css file, we have to run the collectstatic command to make the changes take effect:

____
### AWS for DB / Deployment (Hosting)

**DB**
1. Database
2. Create new POSTGRES
3. Take a walk and update `settings.py`

**Elastic Beanstalk**
[Specific setup instructions](https://www.w3schools.com/django/django_deploy_config.php). Make sure to update WSGI path accordingly. zipping next step.