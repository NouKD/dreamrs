from django.db import models

# Create your models here.

class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom


class NewsLetter(models.Model):
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'

    def __str__(self):
        return self.email



class SocialAccount(models.Model):
    ICONS = [
        ("facebook", "fa-facebook-f"),
        ("instagram", "fa-instagram"),
        ("google-plus", "fa-google-plus-g"),
        ("linkedin", "fa-linkedin-in")
    ]
    
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom



class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/SiteInfo")
    adresse = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Site info'
        verbose_name_plural = 'Site infos'

    def __str__(self):
        return self.email



class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/Presentation")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom




class Temoignage(models.Model):
    photo = models.ImageField(upload_to="images/Temoignage")
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    message = models.TextField()
    job = models.CharField(max_length=255, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return self.nom