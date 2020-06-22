from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from Action.action import Action
# Register your models here.

class CommentaireInline(admin.StackedInline):
    model = models.Commentaire


class CategorieArticleInline(admin.TabularInline):
    model = models.Article
    
class UserPAdmin(Action):
    list_display = ('user', 'date_add', 'date_update','status', 'photo_view')
    list_filter = ('status', )
    search_fields = ('user', )
    date_hierarchy = 'date_add'
    list_display_links = ['user']
    ordering = ['user']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['user', 'photo',]}),
                 ('Standare', {'fields': ['status']})
                 ]

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.photo.url))



class CategorieArticleAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update','status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['nom', 'description', 'image']}),
                 ('Standare', {'fields': ['status']})
                 ]
    inlines = [CategorieArticleInline]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class TagAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Tag', {'fields': ['nom',]}),
                 ('Standare', {'fields': ['status']})
                 ]


class ArticleAdmin(Action):
    list_display = ('titre', 'date_add', 'date_update','status', 'images_view')
    list_filter = ('status', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['titre', 'auteur', 'contenu', 'description', 'image', 'tag', 'categorie']}),
                 ('Standare', {'fields': ['status']})
                 ]
    inlines = [CommentaireInline]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class CommentaireAdmin(Action):
    list_display = ('nom', 'prenom', 'article', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('article', )
    date_hierarchy = 'date_add'
    list_display_links = ['article']
    ordering = ['article']
    list_per_page = 10
    fieldsets = [('Info Commentaire', {'fields': ['article', 'nom', 'commentaire']}),
                 ('Standare', {'fields': ['status']})
                 ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.UserP, UserPAdmin)
