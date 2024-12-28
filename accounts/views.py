from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.views.decorators.csrf import csrf_exempt
# Handle Auth
@csrf_exempt
def login_view (request):
    if request.method == 'GET':
        print("authing")
        form = AuthenticationForm()
        return render (request , 'accounts/login.html' , {"form" : form})

    else :
        form = AuthenticationForm(request , data=request.POST)
        print(dir (AuthenticationForm))
        if form.is_valid():
            user=  form.get_user()
            login(request,user)
            return redirect('/')
        return render(request,  'accounts/login.html', {'form' : form})
    
        

def logout_view(request):
    if request.method == 'POST' or request.method == "GET":
        logout(request)

    return redirect('/')

def register(request):
    form = UserCreationForm( request.POST or None)
    if form.is_valid():
        form.save()

    return render(request , 'accounts/register.html' , {"form" : form})
