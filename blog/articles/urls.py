from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
#HomeView, PostListView, AboutView, PostDetailView, CommentView, show_categories, ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    
    path("",HomeView.as_view(), name='home'),
    
    path("articles/",PostListView.as_view(), name='list-articles'),
    
    path("about/",AboutView.as_view(), name='about'),
    
    #route variable car le contenu change en fontion de l'article
    #on se sert d'une variable i.e pk qui identifie de maniere unique les articles sans oublier son type de donnee
    path("articles/<int:pk>/details",PostDetailView.as_view(), name='article-details'),
    
    path("articles/<int:pk>/comments",CommentView.as_view(), name='article-comments'),

    path("all_categories/",show_categories, name='all_categories'),

    #ici la variable utilise est pk,mais peut etre autre 
    #comme le titre ou autre donnee
    path("articles/<int:pk>/delete", supprimer_article, name ='supprimer_article')

] 