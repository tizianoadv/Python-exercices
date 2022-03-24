from django import forms
from .models import TinyURL

class URLForm(forms.ModelForm):
    class Meta:
        model = TinyURL
        fields = ('username','url',)
