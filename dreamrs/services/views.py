from django.shortcuts import render
from .models import Contact, NewsLetter, Presentation, SiteInfo, SocialAccount, Temoignage
from blog.models import Article, CategorieArticle, Commentaire, Tag, UserP
from website.models import Apartment, CatProjet, Projet, Services

# Create your views here.

def apartment(request):

    appartement = Apartment.objects.all().order_by('-date_update')[:4]
    presentation = Presentation.objects.filter(status=True)[:1]

    data = {
        'appartements' : appartement,
        'presentation' : presentation,
    }
    
    return render(request, 'pages/Apartment.html', data)
    

def project(request):
    
    projet = Projet.objects.filter(status=True)[:3]
    projet_n = Projet.objects.filter(status=True).order_by('-date_update')[:2]

    data = {
        'projet' : projet,
        'projet_n' : projet_n,
    }
    
    return render(request, 'pages/project.html', data)

def services(request):
    
    service = Services.objects.filter(status=True)[:4]
    presentation = Presentation.objects.filter(status=True).last
    temoignage = Temoignage.objects.filter(status=True)[:3]

    data = {
        'service' : service,
        'presentation' : presentation,
        'temoignage' : temoignage,
    }
    
    return render(request, 'pages/services.html', data)        