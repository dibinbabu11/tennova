from django.shortcuts import render,redirect
from . models import Recipie
from . forms import recipie_form
from django .core . paginator import Paginator,EmptyPage,InvalidPage
from django .contrib.auth.models import User


# Create your views here.

def index(request):
    recipie=Recipie.objects.all()
    paginator=Paginator(recipie,8)
    try:
        page= int(request.GET.get('page','1'))
    except:
        page=1
    try:
        recipies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        recipies=paginator.page(paginator.num_pages)
  
    return render(request,'index.html',{'recipies':recipies})

def detail(request,recipie_id):
    recipies=Recipie.objects.get(id=recipie_id)

    return render(request,'detail.html',{'recipies':recipies})
def add_recipie(request):

    if request.method=="POST":
        name=request.POST.get('name')
        difficulty=request.POST.get('difficulty')
        prep_time=request.POST.get('prep_time')
        Image=request.FILES['Image']
        recipies=Recipie(name=name,difficulty=difficulty,prep_time=prep_time,Image=Image)
        recipies.save()
        return redirect('/')

    
    return render(request,'add.html')

def update(request,id):
    recipies=Recipie.objects.get(id=id) 
    form=recipie_form(request.POST or None,request.FILES,instance=recipies)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'recipies':recipies})
def delete(request,id):
    if request.method=="POST":
        recipies=Recipie.objects.get(id=id)
        recipies.delete()
        return redirect('/')
    return render (request,'delete.html')
# def review(request):
#     id=request.GET.get('id')
#     recipie=Recipie.objects.get(id=int(id)) 
#     user=request.session['name']
#     if request.method == 'POST':
#         star_rating=request.POST.get('rating')
#         recipie_review=request.POST.get('recipie_review')
#         recipie_review=review(user)
    # return render(request,'review.html')