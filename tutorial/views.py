
from .models import Snippet
from django.shortcuts import render
from .forms import Mform
from .serializers import SnippetSerializer

def show(request):
    modelform = SnippetSerializer
    return render(request, 'index.html', {'key':modelform})
    
    
    
    
