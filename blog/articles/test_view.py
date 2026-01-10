from django.test import TestCase
from articles.models import Article, Categorie, Tags, Commentaire
from django.contrib.auth.models import User
from django.urls import reverse

class CommentCreateViewTest(TestCase):
  def test_post_comment(self):
    #FACTS
    user = User.objects.create_user("testuser", "test@mail.com", "pass")
    cat = Categorie.objects.create(nom="Test")
    tag = Tags.objects.create(nom = "testtag")
    art = Article.objects.create(titre="test", contenu="...", categorie=cat, auteur=user)
    #ACTION
    url = reverse ("article-comments", kwargs={"pk": art.pk})
    #HTTP REQUEST
    response = self.client.post(url, data={"name":"Harry", "contenu":"Test comment"}, follow=True)
    #ASSERTION
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Test")
    self.assertEqual(art.commentaire_set.count(),1)