from django.shortcuts import render
from django.http import JsonResponse
from .models import Processor

def comparison(request):
    return render(request, 'processors/comparison.html')

def search_processors(request):
    query = request.GET.get('q', '').strip()
    
    if len(query) < 2:
        return JsonResponse({'results': []})
    
    processors = Processor.objects.filter(name__icontains=query)[:15]
    
    results = []
    for cpu in processors:
        results.append({
            'id': cpu.id,
            'name': cpu.name,
            'manufacturer': cpu.manufacturer,
            'cores': cpu.cores,
            'threads': cpu.threads,
            'release_year': cpu.release_year,
        })
    
    return JsonResponse({'results': results})
