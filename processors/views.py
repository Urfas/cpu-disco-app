from django.shortcuts import render, get_object_or_404
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
            'category': cpu.category,
        })

    return JsonResponse({'results': results})


def processor_detail(request, pk):
    cpu = get_object_or_404(Processor, pk=pk)

    def pair(value, approx):
        return {
            'value': value,
            'approx': bool(approx),
        }

    data = {
        'id': cpu.id,
        'name': cpu.name,
        'slug': cpu.slug,
        'manufacturer': cpu.manufacturer,
        'series': cpu.series,
        'category': cpu.category,
        'cores': cpu.cores,
        'threads': cpu.threads,
        'base_clock': cpu.base_clock,
        'boost_clock': cpu.boost_clock,
        'l1_cache': cpu.l1_cache,
        'l2_cache': cpu.l2_cache,
        'l3_cache': cpu.l3_cache,
        'architecture': cpu.architecture,
        'lithography': cpu.lithography,
        'tdp': cpu.tdp,
        'max_temp': cpu.max_temp,
        'socket': cpu.socket,
        'integrated_graphics': cpu.integrated_graphics,
        'igpu_name': cpu.igpu_name,
        'memory_support': cpu.memory_support,
        'pcie': cpu.pcie,
        'release_year': cpu.release_year,
        'benchmarks': {
            'overall_score': pair(cpu.overall_score, cpu.overall_score_approx),
            'passmark': pair(cpu.passmark, cpu.passmark_approx),
            'geekbench4_single': pair(cpu.geekbench4_single, cpu.geekbench4_single_approx),
            'geekbench4_multi': pair(cpu.geekbench4_multi, cpu.geekbench4_multi_approx),
            'cinebench_r15_single': pair(cpu.cinebench_r15_single, cpu.cinebench_r15_single_approx),
            'cinebench_r15_multi': pair(cpu.cinebench_r15_multi, cpu.cinebench_r15_multi_approx),
            'cinebench_r11_single': pair(cpu.cinebench_r11_single, cpu.cinebench_r11_single_approx),
            'cinebench_r11_multi': pair(cpu.cinebench_r11_multi, cpu.cinebench_r11_multi_approx),
            'threedmark06_cpu': pair(cpu.threedmark06_cpu, cpu.threedmark06_cpu_approx),
            'winrar': pair(cpu.winrar, cpu.winrar_approx),
            'x264_pass1': pair(cpu.x264_pass1, cpu.x264_pass1_approx),
            'x264_pass2': pair(cpu.x264_pass2, cpu.x264_pass2_approx),
        },
    }
    return JsonResponse(data)
