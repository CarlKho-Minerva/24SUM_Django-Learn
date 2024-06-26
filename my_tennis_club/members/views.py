from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

# The members view does the following:

# - Creates a mymembers object with all the values of the Member model.
# - Loads the all_members.html template.
# - Creates an object containing the mymembers object.
# - Sends the object to the template.
# - Outputs the HTML that is rendered by the template.

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# The details view does the following:

# Gets the id as an argument.
# Uses the id to locate the correct record in the Member table.
# loads the details.html template.
# Creates an object containing the member.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# The main view does the following:

# loads the main.html template.
# Outputs the HTML that is rendered by the template.


def testing(request):
  mydata = Member.objects.all()
  # mydata = Member.objects.values_list('firstname', flat=True)
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def testingcss(request):
  template = loader.get_template('template_css.html')
  return HttpResponse(template.render())