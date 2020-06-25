from django.shortcuts import render

# Create your views here.

def register(request):
    
    data = {
        
    }
    
    return render(request, 'pages/register-20.html', data)

def login(request):
    
    data = {
        
    }
    
    return render(request, 'pages/login-20.html', data)  

def forgot(request):
    
    data = {
        
    }
    
    return render(request, 'pages/forgot-password-20.html', data)         