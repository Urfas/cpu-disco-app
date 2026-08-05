from django.db import models

class Processor(models.Model):
    # === Основная информация ===
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
    category = models.CharField("Категория", max_length=50, choices=[
        ('Desktop', 'Десктопный'),
        ('Mobile', 'Мобильный'),
        ('Server', 'Серверный'),
        ('Other', 'Другой'),
    ], blank=True)
    image = models.URLField("Ссылка на изображение", blank=True, null=True)

    # === Ядра и потоки ===
    cores = models.PositiveIntegerField("Всего ядер", null=True, blank=True)
    performance_cores = models.PositiveIntegerField("Performance-ядра", null=True, blank=True)
    efficiency_cores = models.PositiveIntegerField("Efficiency-ядра", null=True, blank=True)
    threads = models.PositiveIntegerField("Потоки", null=True, blank=True)

    # === Частоты ===
    base_clock = models.FloatField("Базовая частота (GHz)", null=True, blank=True)
    boost_clock = models.FloatField("Boost частота (GHz)", null=True, blank=True)

    # === Кэш ===
    l1_cache = models.CharField("Кэш L1", max_length=100, blank=True)
    l2_cache = models.CharField("Кэш L2", max_length=100, blank=True)
    l3_cache = models.CharField("Кэш L3", max_length=100, blank=True)

    # === Архитектура и техпроцесс ===
    architecture = models.CharField("Архитектура (ядро)", max_length=100, blank=True)
    lithography = models.CharField("Техпроцесс", max_length=50, blank=True)
    transistors = models.PositiveIntegerField("Транзисторов (млн)", null=True, blank=True)

    # === Питание и температура ===
    tdp = models.PositiveIntegerField("TDP (Вт)", null=True, blank=True)
    max_temp = models.PositiveIntegerField("Макс. температура (°C)", null=True, blank=True)

    # === Сокет и шина ===
    socket = models.CharField("Сокет", max_length=50, blank=True)
    bus = models.CharField("Шина", max_length=100, blank=True)

    # === Графика ===
    integrated_graphics = models.BooleanField("Встроенная графика", default=False)
    igpu_name = models.CharField("Название iGPU", max_length=150, blank=True)

    # === Память и PCIe ===
    memory_support = models.CharField("Поддержка памяти (RAM)", max_length=200, blank=True)
    pcie = models.CharField("PCIe", max_length=100, blank=True)

    # === Прочее ===
    integrated_modules = models.TextField("Встроенные модули", blank=True)
    instructions = models.TextField("Инструкции и технологии", blank=True)
    other_features = models.TextField("Другие особенности", blank=True)
    release_year = models.PositiveIntegerField("Год выхода", null=True, blank=True)

    # === БЕНЧМАРКИ ===
    overall_score = models.PositiveIntegerField("Общий рейтинг", null=True, blank=True)
    overall_score_approx = models.BooleanField("Общий рейтинг приблизительный", default=False)

    cinebench_r23_single = models.PositiveIntegerField("Cinebench R23 Single", null=True, blank=True)
    cinebench_r23_single_approx = models.BooleanField("Cinebench R23 Single приблизительный", default=False)
    cinebench_r23_multi = models.PositiveIntegerField("Cinebench R23 Multi", null=True, blank=True)
    cinebench_r23_multi_approx = models.BooleanField("Cinebench R23 Multi приблизительный", default=False)

    cinebench_2024_single = models.PositiveIntegerField("Cinebench 2024 Single", null=True, blank=True)
    cinebench_2024_single_approx = models.BooleanField("Cinebench 2024 Single приблизительный", default=False)
    cinebench_2024_multi = models.PositiveIntegerField("Cinebench 2024 Multi", null=True, blank=True)
    cinebench_2024_multi_approx = models.BooleanField("Cinebench 2024 Multi приблизительный", default=False)

    geekbench6_single = models.PositiveIntegerField("Geekbench 6 Single", null=True, blank=True)
    geekbench6_single_approx = models.BooleanField("Geekbench 6 Single приблизительный", default=False)
    geekbench6_multi = models.PositiveIntegerField("Geekbench 6 Multi", null=True, blank=True)
    geekbench6_multi_approx = models.BooleanField("Geekbench 6 Multi приблизительный", default=False)

    passmark = models.PositiveIntegerField("PassMark", null=True, blank=True)
    passmark_approx = models.BooleanField("PassMark приблизительный", default=False)

    # === Служебные ===
    notes = models.TextField("Заметки", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"
        ordering = ['-release_year', 'name']

    def __str__(self):
        return self.name
