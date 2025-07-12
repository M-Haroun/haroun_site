from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    data = ContactForm(request.GET)
    if data.is_valid():
        data.save()
    context = {'contact_form':ContactForm}
    return render(request, 'pages/contact.html', context)