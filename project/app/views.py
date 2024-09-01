from django.shortcuts import render
from .models import Employee
# Create your views here.
def index(request):
  return render(request,"index.html")
  

def insertData(request):

  data=Employee.objects.all()
  context={"data":data}
  
  if request.method=="POST":
    name= request.POST.get('name')
    email= request.POST.get('Email')
    age= request.POST.get('age')
    gender= request.POST.get('gender')
    print(name,email,age,gender)
    query=Employee(name=name,email=email,age=age,gender=gender)
    query.save()

  return render(request,"index.html")

def about(request):
  return render(request,"about.html") 