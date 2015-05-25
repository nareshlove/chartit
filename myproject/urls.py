from django.conf.urls import patterns, include, url
from django.contrib import admin
from myproject.core.views import *

urlpatterns = patterns(
    'myproject.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^linechart/$', LineChartView.as_view(), name='linechart'),
    url(r'^piechart/$', 'piechart', name='piechart'),
    url(r'^multiplechart/$', 'multiplechart', name='multiplechart'),
    url(r'^combinationchart/$', 'combinationchart', name='combinationchart'),
    url(r'^download/$', 'download', name='download'),
    url(r'^about/$', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
