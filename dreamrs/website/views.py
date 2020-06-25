from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from .models import Apartment, CatProjet, Projet, Services 
from blog.models import Article, CategorieArticle, Commentaire, Tag, UserP
from services.models import Contact, NewsLetter, Presentation, SiteInfo, SocialAccount, Temoignage
#from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    presentation = Presentation.objects.filter(status=True).last
    article = Article.objects.filter(status=True)[:3]
    project = CatProjet.objects.filter(status=True)[:4]
    site_info = SiteInfo.objects.filter(status=True).last
    appartement = Apartment.objects.filter(status=True)[:3]
    services = Services.objects.filter(status=True)[:4]
   
    data = {
        'presentation' : presentation,
        'article' : article,
        'project'  : project,
        'site_info'  : site_info,
        'appartement' : appartement,
        'services' : services,
    }
    return render(request, 'pages/index.html', data)

def about(request):

    presentation = Presentation.objects.filter(status=True).last
    appartement = Apartment.objects.filter(status=True)[:4]
    temoignage = Temoignage.objects.filter(status=True)[:3]
    
    data = {
       'presentation' : presentation,
       'appartement' : appartement,
       'temoignage' : temoignage, 
    }
    
    return render(request, 'pages/about.html', data)

def contact(request):
    
    site_info = SiteInfo.objects.filter(status=True).last
    contacter_nous = Contact.objects.filter(status=True).last
    message = ""
    if request.method == 'POST':
        nom = request.POST.get('username')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        try:
            isemail = validate_email(email)
            if isemail and not email.isspace() and nom and message:
                print("1")
                contact = models.Contact(
                    nom = nom,
                    email = email,
                    sujet = sujet,
                    message = message
                )
                contact.save()
                print("3")
                message = "vous avez été enregistré"
        except :
            message = "email incorrect"
            print("2")

    data = {
        'site_info' : site_info,
        'contacter_nous' : contacter_nous,
        'message' : message,
    }
    
    return render(request, 'pages/contact.html', data)

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(email=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))                