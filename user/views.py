from django.shortcuts import render
from django.views.generic import *
#CreateView, TemplateView
from django.contrib.auth.forms import *
#UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from articles.models import *

# Create your views here.
class SignUpView(CreateView):
  #try to change this variable name to see what happens
  form_class = UserCreationForm #username, email, password, confirmpassword
  template_name = 'signup.html'
  success_url = reverse_lazy("user:profile")

  def form_valid(self, form):
    #create user in db
    response = super().form_valid(form)
    #Login
    user = form.instance
    login(self.request, user) #creer la session utilisateur
    return response


class ProfileView(TemplateView):
  template_name = "profile.html"

  def get_context_data(self, **kwargs):
    #recupere le contexte d'origin
    ctx = super().get_context_data(**kwargs)
    #recuperation de l'utilisateur lorsque la session est active
    user_obj = self.request.user

    #recuperer les articles de l'utilisateur
    articles_user = Article.objects.filter(auteur=user_obj)

    #ajouter les donnees dans le contexte
    ctx.update({
      "user": user_obj,
      "mes_articles": articles_user,
      "liked_articles": []
    })
    return ctx  

    
