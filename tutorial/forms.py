
from .models import Snippet
from django import forms

class Mform(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title','code','linenos','language','style']
        
