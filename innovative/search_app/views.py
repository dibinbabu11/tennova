from django.shortcuts import render
from  Recipes .models import Recipie 
from django .db.models import Q
from django.http import HttpResponse
# Create your views here.
def searchresult(request):
    if request.method=='POST':
        searched = request.POST['searched']
        recipies=Recipie.objects.filter(name__contains=searched)

        return render(request,'search.html',{'searched':searched,'recipies':recipies})
    else:
        return render(request,'search.html',)


