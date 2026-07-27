from django.shortcuts import render
from .models import Processor

def comparison(request):
    # Пока просто отдаём пустой список.
    # Поиск и добавление сделаем на следующем шаге.
    return render(request, 'processors/comparison.html', {
        'processors': []
    })
