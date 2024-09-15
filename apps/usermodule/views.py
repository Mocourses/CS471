from django.shortcuts import render
#LAB_4
from django.http import HttpResponse

# Create your views here.
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, " bookmodule/index.html" , {"name": name})

def index2(request, val1 ): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))