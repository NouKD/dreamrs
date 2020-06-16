from django.shortcuts import render

# Create your views here.

def blog(request):
    
    data = {
        
    }
    
    return render(request, 'pages/blog.html', data)

def single_blog(request):
    
    data = {
        
    }
    
    return render(request, 'pages/single-blog.html', data)    