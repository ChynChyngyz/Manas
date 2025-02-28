from django.db import models


class Epos(models.Model):
    epos_name = models.CharField(max_length=100, unique=True)
    epos_photo = models.ImageField(upload_to="epos/", null=True, blank=True, verbose_name='Фото эпоса')
    epos_description = models.CharField(max_length=250)
    epos_info = models.TextField()

    def __str__(self):
        return f'Эпос: {self.epos_name}'

    class Meta:
        verbose_name = 'Эпос'
        verbose_name_plural = 'Эпосы'


class Manaschi(models.Model):
    manaschi_name = models.CharField(max_length=100)
    manaschi_photo = models.ImageField(upload_to="manaschi/", null=True, blank=True, verbose_name='Фото манасчи')
    manaschi_description = models.CharField(max_length=250)
    manaschi_info = models.TextField()
    def __str__(self):
        return f'Манасчи: {self.manaschi_name}'

    class Meta:
        verbose_name = 'Манасчи'
        verbose_name_plural = 'Манасчи'


class Researchers(models.Model):
    name = models.CharField(max_length=100)
    researchers_photo = models.ImageField(upload_to="researchers/", null=True, blank=True, verbose_name='Фото исследователей или этнографов')
    researchers_description = models.CharField(max_length=250)
    researchers_info = models.TextField()
    def __str__(self):
        return f'Исследователи/Этнографы: {self.name}'

    class Meta:
        verbose_name = 'Исследователь'
        verbose_name_plural = 'Исследователи'

