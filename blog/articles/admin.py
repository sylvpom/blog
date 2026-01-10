from django.contrib import admin
from .models import Article,Categorie,Tags, Photo

class PhotoInline(admin.TabularInline):
  model = Photo
  extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  list_display = ("titre","auteur","categorie","date_publication")
  inlines = [PhotoInline]


# Register your models here.
#admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Tags)