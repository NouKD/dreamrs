from django.db import models

# Create your models here.

class Services(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Services")
    description =  models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom

class CatProjet(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'CatProjet'
        verbose_name_plural = 'CatProjets'

    def __str__(self):
        return self.nom


class Projet(models.Model):

    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Services")
    description =  models.TextField()
    cat_projet = models.ForeignKey(CatProjet, on_delete=models.CASCADE, related_name='Catprojet', null=True) 

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.nom




class Apartment(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Apartment')
    superficie = models.FloatField(null=True)
    douche = models.IntegerField(null=True)
    n_win = models.IntegerField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'

    def __str__(self):
        return self.titre