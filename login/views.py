from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm

def LoginView(response):
        if response.method=="POST":
           form=RegisterForm(response.POST)
           if form.is_valid():
                form.save()
                messages.success(response, "Succesfully saved")
                return redirect("/login_user") 

        else:
         form=RegisterForm()

        return render(response,'login/login.html',{"form":form})
 

def login_user(request):
        # if request.method=='POST':
        # username = request.POST['username']
        # password = request.POST['password']

        return render(request,"login/loginuser.html")
# Create your views here.
