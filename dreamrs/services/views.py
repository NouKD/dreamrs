from django.shortcuts import render

# Create your views here.

def Apartment(request):
    
    data = {
        
    }
    
    return render(request, 'pages/Apartment.html', data)

def elements(request):
    
    data = {
        
    }
    
    return render(request, 'pages/elements.html', data)

def project(request):
    
    data = {
        
    }
    
    return render(request, 'pages/project.html', data)

def services(request):
    
    data = {
        
    }
    
    return render(request, 'pages/services.html', data)        