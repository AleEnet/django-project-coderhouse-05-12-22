from django.shortcuts import render
from .models import Familiare

def home (request):
    familiar = Familiare.objects.all()
    return render(request,"home.html", {"familiar" : familiar})
# Create your views here.
