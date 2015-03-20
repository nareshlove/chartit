# -*- coding: utf-8 -*-
from django.db import models
from chartit import DataPool, Chart


class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        ordering = ['month']
        verbose_name = 'month'
        verbose_name_plural = 'months'

    def __unicode__(self):
        return str(self.month)
