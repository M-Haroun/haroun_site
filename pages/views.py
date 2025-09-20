from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from projects.models import Project,ProjectImage
import random

# Create your views here.
def index(request):
    all_images = list(ProjectImage.objects.exclude(images=''))  # get all images that are not empty
    slides_images = random.sample(all_images, (min(len(all_images),5)))    
    context = {
        'slides_images': slides_images,
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    data = ContactForm(request.GET)
    if data.is_valid():
        data.save()
    context = {'contact_form':ContactForm}
    return render(request, 'pages/contact.html', context)