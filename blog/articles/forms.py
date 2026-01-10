from django import forms
from .models import Commentaire

class CommentForm(forms.ModelForm):
  """username = forms.CharField(max_length=100, 
                             required=True, 
                             label = "Votre Nom")
  usercomment = forms.CharField(widget=forms.Textarea,
                                required = True)
  """
  class Meta:
    model = Commentaire
    fields = ["name", "contenu"]
    widgets = {
                "contenu": forms.Textarea(attrs={
                  "rows":4, 
                  "placeholder":"Enter your comment here"})
              }
  
  #Validating user information
  #User information are stored in a dictionary called  
  #cleaned data
    def clean_username(self):
      #Enlever les espaces
      # le dictionaire contient les donnees du formulaire
      username = self.cleaned_data.get("name")
      if username != None :
        return username.strip().lower()
      
    def clean_usercomment(self):
      #Enlever les espaces
      # le dictionaire contient les donnees du formulaire
      commentcontent = self.cleaned_data.get("usercomment")
      
      if "bete" in commentcontent :
        raise forms.ValidationError("Contenu inapproprie dans ce commentaire")  
      return commentcontent