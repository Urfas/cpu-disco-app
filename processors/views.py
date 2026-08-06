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
            'tdp': cpu.tdp,
            'socket': cpu.socket,
            'lithography': cpu.lithography,
            'max_temp': cpu.max_temp,
            'category': cpu.category,
            'integrated_graphics': cpu.integrated_graphics,
            'igpu_name': cpu.igpu_name,
            'base_clock': cpu.base_clock,
            'boost_clock': cpu.boost_clock,
            'memory_support': cpu.memory_support,
            'overall_score': cpu.overall_score,
            'cinebench_r23_single': cpu.cinebench_r23_single,
            'cinebench_r23_multi': cpu.cinebench_r23_multi,
            'cinebench_2024_single': cpu.cinebench_2024_single,
            'cinebench_2024_multi': cpu.cinebench_2024_multi,
            'geekbench6_single': cpu.geekbench6_single,
            'geekbench6_multi': cpu.geekbench6_multi,
            'passmark': cpu.passmark,
            'image': cpu.image,
        })
    
    return JsonResponse({'results': results})
