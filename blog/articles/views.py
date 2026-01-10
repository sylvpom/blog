from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView, CreateView
from .models import Article, Commentaire, Categorie
from .forms import CommentForm
import datetime 
from django.db.models import Q

from rest_framework import viewsets
from .serializers import ArticleSerializer
from django.contrib.auth.decorators import permission_required


# Create your views here.
class HomeView(TemplateView):
  template_name ='Home.html'


class PostListView(ListView):
  model = Article
  template_name ='List-articles.html'
  context_object_name = 'articles' # variable to store our articles list
  paginate_by = 5 # presents 5 articles per page


class AboutView(TemplateView):
  template_name = 'About.html'

class PostDetailView(DetailView):#Detail view pour afficher les details
  #Recuperation de l'article dans un model
  model = Article
  """
  Ensuite on l'affiche 
  dans un template en se servant d'un context
  """
  context_object_name = 'article_details'
  form_class = CommentForm
  template_name = 'detail.html'
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx["form"] = CommentForm() 
    return ctx
  """

  """

class CommentView(CreateView):
  form_class = CommentForm
  #we pass the form object to work with 
  context_object_name = "form"
  model = Commentaire
  #fields = ["name", "contenu"]#ici les champs a renseigner sont ceux du model commentaire
  #which form to work with in our comment
  
  def form_valid(self, form):
    form.instance.article_id = self.kwargs['pk']
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('article-details', kwargs={'pk': self.kwargs['pk']})
  

#vues basees sur des fonctions
def show_categories(request):
  #recuperation de toutes les categories et 
  #stockage dans la variable Categories
  Categories = Categorie.objects.all()
  #categories_list est la cle du dictionaire pour parcourir les categories
  return render (request,"categories.html", {"categories_list":Categories}) 


"""
fonction de vues pour les articles et leur auteurs
"""
def list_articles_author(request):
  articles_author_infos = Article.objects.select_related('auteur').all()
  
  date_hier = datetime.datetime = datetime.datetime.today() - datetime.timedelta(days = 1)
  articles_today = Article.objects.filter(date_publication__gt= date_hier)
  
  articles_admin_avanthier = Article.objects.filter(Q(auteur__username="admin")
                                                    &Q(date_publication__lte = date_hier))\
                                                    .order_by('-titre')
  total_articles_admin = len(Article.objects.filter(auteur__username='admin'))
  return render(request, 'articles_auteurs.html',{"infos":articles_author_infos})


@permission_required('articles.peut_supprimer_article', raise_exception=True)
def supprimer_article(request, article_id):
  #article = Article.objects.filter(pk=article_id).first()
  #if article_id doesn't exist, then article will be none
  
  #article = Article.objects.get(pk=article_id)

  article = get_object_or_404(Article, pk=article_id)
  article.delete()
  return redirect("list-articles")



#  DJANGO REST
#
#
class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer





