from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request,'login_user.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def state(request):
    return render(request,'state.html')
def district(request):
    return render(request,'District.html')

def company(request):
    return render(request,'Publication_house.html')

def headline(request):
    return render(request,'headline.html')
def magzine(request):
    return render(request,'magzine.html')
def magzine_catagory(request):
    return render(request,"magzine_catagory.html")
def sunday_magzine(request):
    return render(request,"sunday_magzine.html")

def publish_newspaper(request):
    return render(request,"publish_newspaper.html")