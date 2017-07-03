# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'auteur', 'date')
   list_filter    = ('auteur','categorie',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('titre', 'contenu')

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
