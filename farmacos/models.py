from django.db import models
from django.utils.encoding import force_unicode as _

# Create your models here.



class Farmaco(models.Model):
	nombre = models.CharField(max_length=100)
	clave = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return _(self.nombre)


class FarmacoCuadro(models.Model):
	farmaco = models.ForeignKey(Farmaco)
	imagen = models.ImageField(upload_to='farmacos')
	#descripcion = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)


class SubFarmaco(models.Model):
	nombre = models.CharField(max_length=100)
	farmaco = models.ForeignKey(Farmaco)
	efectos_adversos = models.TextField()
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return _(self.nombre)

class FormulaSubFarmaco(models.Model):
	nombre_formula = models.CharField(max_length=100)
	subfarmaco = models.ForeignKey(SubFarmaco)
	formula = models.TextField()
	formulario_html = models.TextField()

	def calcular_formula(self, edad):
		exec(self.formula)

