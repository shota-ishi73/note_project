from django import forms
from .models import Note
from user.models import User

class NoteCreateForm(forms.ModelForm):

  class Meta:
    model = Note
    fields = ['title','text','category','create_at','update_at','user_id']