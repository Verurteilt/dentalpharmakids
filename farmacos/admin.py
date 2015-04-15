from django.contrib import admin
from farmacos.models import Farmaco, SubFarmaco, FarmacoCuadro,FormulaSubFarmaco
admin.site.register(Farmaco)
admin.site.register(SubFarmaco)
admin.site.register(FarmacoCuadro)
admin.site.register(FormulaSubFarmaco)

