from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from Action.action import Action

# Register your models here.

class ServicesAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info', {'fields': ['nom', 'description', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class ApartmentAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info', {'fields': ['nom', 'description', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class CatProjetAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info ', {'fields': ['nom',]}),
                 ('Standard', {'fields': ['status']})
                 ]

class ProjetAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update','status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Projet', {'fields': ['nom', 'description', 'image', 'cat_projet']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Services, ServicesAdmin)
_register(models.CatProjet, CatProjetAdmin)
_register(models.Projet, ProjetAdmin)
_register(models.Apartment, ApartmentAdmin)