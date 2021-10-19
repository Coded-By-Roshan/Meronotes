from django import forms
from django.forms import fields
from . models import Note

class CreateNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'file']