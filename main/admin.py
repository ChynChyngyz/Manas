from django.contrib import admin
from .models import Epos, Manaschi, Researchers

# Класс для настройки отображения модели Epos в админке
class EposAdmin(admin.ModelAdmin):
    list_display = ('epos_name', 'epos_description', 'epos_info', 'epos_photo')  # Какие поля отображаются в списке
    search_fields = ('epos_name',)  # По каким полям можно искать
    list_filter = ('epos_name',)  # Фильтрация по полям
    ordering = ('epos_name',)  # Как сортировать элементы

# Класс для настройки отображения модели Manaschi в админке
class ManaschiAdmin(admin.ModelAdmin):
    list_display = ('manaschi_name', 'manaschi_description', 'manaschi_info', 'manaschi_photo')
    search_fields = ('manaschi_name',)
    list_filter = ('manaschi_name',)
    ordering = ('manaschi_name',)

# Класс для настройки отображения модели Researchers в админке
class ResearchersAdmin(admin.ModelAdmin):
    list_display = ('name', 'researchers_description', 'researchers_info', 'researchers_photo')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

# Регистрация моделей с их админскими настройками
admin.site.register(Epos, EposAdmin)
admin.site.register(Manaschi, ManaschiAdmin)
admin.site.register(Researchers, ResearchersAdmin)
