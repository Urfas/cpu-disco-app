from django.db import models

class Processor(models.Model):
    # Основная информация
    name = models.CharField("Название", max_length=200, unique=True)
    manufacturer = models.CharField("Производитель", max_length=50, choices=[
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        ('Apple', 'Apple'),
        ('Qualcomm', 'Qualcomm'),
        ('MediaTek', 'MediaTek'),
        ('Samsung', 'Samsung'),
        ('Other', 'Другой'),
    ])
    series = models.CharField("Серия", max_length=100, blank=True)
    image = models.URLField("Ссылка на изображение", blank=True, null=True)

    # Характеристики
    cores = models.PositiveIntegerField("Всего ядер", null=True, blank=True)
    performance_cores = models.PositiveIntegerField("Performance-ядра", null=True, blank=True)
    efficiency_cores = models.PositiveIntegerField("Efficiency-ядра", null=True, blank=True)
    threads = models.PositiveIntegerField("Потоки", null=True, blank=True)
    
    base_clock = models.FloatField("Базовая частота (GHz)", null=True, blank=True)
    boost_clock = models.FloatField("Boost частота (GHz)", null=True, blank=True)
    
    tdp = models.PositiveIntegerField("TDP (Вт)", null=True, blank=True)
    socket = models.CharField("Сокет", max_length=50, blank=True)
    release_year = models.PositiveIntegerField("Год выхода", null=True, blank=True)
    lithography = models.CharField("Техпроцесс", max_length=50, blank=True)
    integrated_graphics = models.BooleanField("Встроенная графика", default=False)
    igpu_name = models.CharField("Название iGPU", max_length=100, blank=True)

    # === БЕНЧМАРКИ ===

    # Общий рейтинг
    overall_score = models.PositiveIntegerField("Общий рейтинг", null=True, blank=True)
    overall_score_approx = models.BooleanField("Общий рейтинг приблизительный", default=False)

    # Cinebench R23
    cinebench_r23_single = models.PositiveIntegerField("Cinebench R23 Single", null=True, blank=True)
    cinebench_r23_single_approx = models.BooleanField("Cinebench R23 Single приблизительный", default=False)
    
    cinebench_r23_multi = models.PositiveIntegerField("Cinebench R23 Multi", null=True, blank=True)
    cinebench_r23_multi_approx = models.BooleanField("Cinebench R23 Multi приблизительный", default=False)

    # Cinebench 2024
    cinebench_2024_single = models.PositiveIntegerField("Cinebench 2024 Single", null=True, blank=True)
    cinebench_2024_single_approx = models.BooleanField("Cinebench 2024 Single приблизительный", default=False)

    cinebench_2024_multi = models.PositiveIntegerField("Cinebench 2024 Multi", null=True, blank=True)
    cinebench_2024_multi_approx = models.BooleanField("Cinebench 2024 Multi приблизительный", default=False)

    # Geekbench 6
    geekbench6_single = models.PositiveIntegerField("Geekbench 6 Single", null=True, blank=True)
    geekbench6_single_approx = models.BooleanField("Geekbench 6 Single приблизительный", default=False)

    geekbench6_multi = models.PositiveIntegerField("Geekbench 6 Multi", null=True, blank=True)
    geekbench6_multi_approx = models.BooleanField("Geekbench 6 Multi приблизительный", default=False)

    # PassMark
    passmark = models.PositiveIntegerField("PassMark", null=True, blank=True)
    passmark_approx = models.BooleanField("PassMark приблизительный", default=False)

    # Дополнительно
    notes = models.TextField("Заметки", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"
        ordering = ['-release_year', 'name']

    def __str__(self):
        return self.name
