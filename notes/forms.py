from django import forms
from .models import Note, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('label', 'body', 'tags')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)



