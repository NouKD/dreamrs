from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/UserP')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'UserP'
        verbose_name_plural = 'UserPs'

    def __str__(self):
        return str(self.user)

class CategorieArticle(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/CategorieArticle")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie Article'
        verbose_name_plural = 'Categories Article'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to="images/Article")
    tag = models.ManyToManyField(Tag, related_name='tag_Article', blank=True )
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name='categorie_Article')
    auteur = models.ForeignKey(UserP, on_delete=models.CASCADE, related_name='auteur_Article', null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaire_article')
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    commentaire = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.nom