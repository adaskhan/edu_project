from django.db import models


class PriceCard(models.Model):
    price = models.CharField(max_length=10, verbose_name='Цена')
    description = models.TextField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    old_price = models.CharField(max_length=10, verbose_name='Старая Цена')
    new_price = models.CharField(max_length=10, verbose_name='Новая Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
