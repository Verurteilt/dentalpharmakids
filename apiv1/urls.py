from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
#especialidades, 

urlpatterns = patterns('',
    url(r'^login/', login_view),
    url(r'^signup/', signup_view),
    url(r'^obtener_cuadros_generales_subfarmacos/', obtener_cuadros_generales_subfarmacos),
    url(r'^tiene_formulas/', tiene_formulas),
    url(r'^obtener_efectos_adversos/', obtener_efectos_adversos),
    url(r'^obtener_lista_formulas/', obtener_lista_formulas),
    url(r'^formula_html/', formula_html),
    url(r'^calcular_formula/', calcular_formula),
    #url(r'^especialidades/', especialidades),
)



