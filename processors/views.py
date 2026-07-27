from django.shortcuts import render
from .models import Processor

def comparison(request):
    processors = Processor.objects.all()[:20]  # пока берём первые 20
    return render(request, 'processors/comparison.html', {
        'processors': processors
    })
