from django.shortcuts import render
from .models import Member
  
 
def home(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, "home.html", context)


def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request, "details.html", context)