from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #redirect
            return redirect('staffpages:home')

        else:
            #redirect
            messages.success(request,'There was an error login in, Try again latter!')
            return redirect('cars:index')
    
    else:
        #
        return render(request,'accounts/login_user.html')

def logout_user(request):
    logout(request)
    return redirect('cars:index')