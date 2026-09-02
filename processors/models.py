from django.db import models


class Processor(models.Model):
    # === Основная информация ===
    name = models.CharField("Название", max_length=200, unique=True)
    slug = models.SlugField("Slug", max_length=220, unique=True, blank=True, null=True)
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
        ('Embedded', 'Встраиваемый'),
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
    socket = models.CharField("Сокет", max_length=80, blank=True)
    bus = models.CharField("Шина", max_length=100, blank=True)

    # === Графика ===
    # В JSON приходит строка: "нет" / "Intel UHD Graphics 730" и т.п.
    integrated_graphics = models.BooleanField("Есть iGPU", default=False)
    igpu_name = models.CharField("Название iGPU", max_length=150, blank=True)

    # === Память и PCIe ===
    memory_support = models.CharField("Поддержка памяти (RAM)", max_length=250, blank=True)
    pcie = models.CharField("PCIe", max_length=120, blank=True)

    # === Прочее ===
    integrated_modules = models.TextField("Встроенные модули", blank=True)
    instructions = models.TextField("Инструкции и технологии", blank=True)
    other_features = models.TextField("Другие особенности", blank=True)
    release_year = models.PositiveIntegerField("Год выхода", null=True, blank=True)

    # === БЕНЧМАРКИ (то, что реально спарсили) ===
    overall_score = models.PositiveIntegerField("Общий рейтинг", null=True, blank=True)
    overall_score_approx = models.BooleanField("Общий рейтинг приблизительный", default=False)

    passmark = models.PositiveIntegerField("PassMark", null=True, blank=True)
    passmark_approx = models.BooleanField("PassMark приблизительный", default=False)

    geekbench4_single = models.FloatField("Geekbench 4 Single", null=True, blank=True)
    geekbench4_single_approx = models.BooleanField("Geekbench 4 Single приблизительный", default=False)
    geekbench4_multi = models.FloatField("Geekbench 4 Multi", null=True, blank=True)
    geekbench4_multi_approx = models.BooleanField("Geekbench 4 Multi приблизительный", default=False)

    cinebench_r15_single = models.FloatField("Cinebench R15 Single", null=True, blank=True)
    cinebench_r15_single_approx = models.BooleanField("Cinebench R15 Single приблизительный", default=False)
    cinebench_r15_multi = models.FloatField("Cinebench R15 Multi", null=True, blank=True)
    cinebench_r15_multi_approx = models.BooleanField("Cinebench R15 Multi приблизительный", default=False)

    cinebench_r11_single = models.FloatField("Cinebench R11.5 Single", null=True, blank=True)
    cinebench_r11_single_approx = models.BooleanField("Cinebench R11.5 Single приблизительный", default=False)
    cinebench_r11_multi = models.FloatField("Cinebench R11.5 Multi", null=True, blank=True)
    cinebench_r11_multi_approx = models.BooleanField("Cinebench R11.5 Multi приблизительный", default=False)

    threedmark06_cpu = models.FloatField("3DMark06 CPU", null=True, blank=True)
    threedmark06_cpu_approx = models.BooleanField("3DMark06 CPU приблизительный", default=False)

    winrar = models.FloatField("WinRAR", null=True, blank=True)
    winrar_approx = models.BooleanField("WinRAR приблизительный", default=False)

    x264_pass1 = models.FloatField("x264 Pass 1", null=True, blank=True)
    x264_pass1_approx = models.BooleanField("x264 Pass 1 приблизительный", default=False)
    x264_pass2 = models.FloatField("x264 Pass 2", null=True, blank=True)
    x264_pass2_approx = models.BooleanField("x264 Pass 2 приблизительный", default=False)

    # === На будущее (пока пустые, можно заполнить позже) ===
    cinebench_r23_single = models.PositiveIntegerField("Cinebench R23 Single", null=True, blank=True)
    cinebench_r23_single_approx = models.BooleanField(default=False)
    cinebench_r23_multi = models.PositiveIntegerField("Cinebench R23 Multi", null=True, blank=True)
    cinebench_r23_multi_approx = models.BooleanField(default=False)

    cinebench_2024_single = models.PositiveIntegerField("Cinebench 2024 Single", null=True, blank=True)
    cinebench_2024_single_approx = models.BooleanField(default=False)
    cinebench_2024_multi = models.PositiveIntegerField("Cinebench 2024 Multi", null=True, blank=True)
    cinebench_2024_multi_approx = models.BooleanField(default=False)

    geekbench6_single = models.PositiveIntegerField("Geekbench 6 Single", null=True, blank=True)
    geekbench6_single_approx = models.BooleanField(default=False)
    geekbench6_multi = models.PositiveIntegerField("Geekbench 6 Multi", null=True, blank=True)
    geekbench6_multi_approx = models.BooleanField(default=False)

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
