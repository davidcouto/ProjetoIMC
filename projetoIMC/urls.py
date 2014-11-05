from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('avaliacoes.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'login'),
    url(r'^avaliacao/$', 'avaliacao'),
    url(r'^salvar/$', 'salvar'),

)
