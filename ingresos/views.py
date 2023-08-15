from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    template_name="index.html"
    return render(request, template_name)