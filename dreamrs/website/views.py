from django.shortcuts import render

# Create your views here.

def index(request):
    
    data = {
        
    }
    
    return render(request, 'pages/index.html', data)

def about(request):
    
    data = {
        
    }
    
    return render(request, 'pages/about.html', data)

def contact(request):
    
    data = {
        
    }
    
    return render(request, 'pages/contact.html', data)        