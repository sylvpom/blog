from django.test import TestCase
from articles.models import Article, Categorie, Tags, Commentaire
from django.contrib.auth.models import User


class ArticleModeleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", "test@mail.com", "pass")
        self.categorie = Categorie.objects.create(nom="Test")
        self.tag = Tags.objects.create(nom = "testtag")


    def test_creation_article(self):
        # Fact - Act - Assert
        #ACTION
        my_article = Article.objects.create(
            titre= "Mon Article",
            contenu="Texte",
            categorie = self.categorie,
            auteur = self.user
        )
        my_article.tags.add(self.tag)
        #ASSERTIONS (VERIFICATIONS)
        self.assertEqual(my_article.titre,"Mon Article")
        self.assertEqual(my_article.tags.count(), 1)
        self.assertNotEqual(my_article.contenu, "Hello")


    """Test de la relation One-to-Many avec Categorie"""
    def test_relation_categorie(self):
      article1 = Article.objects.create(
        titre="Article 1", 
        contenu="content 1", 
        categorie=self.categorie, 
        auteur=self.user)
      article2 = Article.objects.create(
        titre="Article 2", 
        contenu="content 2", 
        categorie=self.categorie, 
        auteur=self.use)
      self.assertEqual(self.categorie.article_set.count(), 2)
      self.assertIn(article1, self.categorie.article_set.all())    
    
    """ Testing that an article cannot exist without a category"""
    def test_article_without_category_validation_error(self):
      article = Article.objects.create(
        titre="Article sans catégorie",
        contenu="Contenu test",
        auteur=self.user)
      #self.as

class CommentaireTest(TestCase):
    def test_create_comment_and_article_relation(self):
        #Fact
        user = User.objects.create_user("testuser", "test@mail.com", "pass")
        cat = Categorie.objects.create(nom="Test")
        tag = Tags.objects.create(nom = "testtag")
        art = Article.objects.create(titre="test", contenu="...", categorie=cat, auteur=user)
        #Act
        comment = Commentaire.objects.create(
            contenu="test",
            name ="UserTest",
            article = art
        )
        #Assert
        #self.assertEqual(comment.article_id, art.id)
        self.assertEqual(comment.article.titre, art.titre)
        self.assertNotEqual(comment.name, art.auteur.username)
        #self.assertEqual(comment.contenu, "test1")




"""
from django.test import TestCase
from articles.models import *
from django.contrib.auth.models import User

class ArticleModeleTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user("testuser", "test@gmail.com", "pass")
    self.categorie = Categorie.objects.create(nom="Test")
    self.tag = Tags.objects.create(nom = "testtag")


  def test_creation_article(self):
    #Fact - Act - Assert
    #Act (action call a method or an http request)
    my_article = Article.objects.create(
      titre = "Mon Article",
      contenu ="Texte",
      categorie = self.categorie,
      auteur = self.user
    )
    my_article.tags.add(self.tag)
    #Assert
    self.assertEqual(my_article.titre,"Mon Article")
    self.assertEqual(my_article.tags.count(),1)
    self.assertNotEqual(my_article.contenu,"Hello")


class CommentaireTest(TestCase):
  def test_create_comment_add_article_relation(self):
    #Fact
    user = User.objects.create_user("testuser", "test@gmail.com", "pass")
    cat = Categorie.objects.create(nom = "Test")
    tag = Tags.objects.create(nom = "testtag")
    art = Article.objects.create(
      titre = "Mon Article",
      contenu ="Test contenu",
      categorie = cat,
      auteur = user
    )
    #Act
    comment = Commentaire.objects.create(
      contenu ="test commentaire",
      name = "UserTest",
      article = art,
    )
    #Assert
    self.assertEqual(comment.article_id, art.id)
    self.assertEqual(comment.article.titre, art.titre)
    self.assertNotEqual(comment.name, art.auteur.username)
    self.assertEqual(comment.contenu,"test1")
"""


