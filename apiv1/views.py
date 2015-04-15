# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.core import serializers
from users.models import User
from farmacos.models import *
import inspect

def return_json_response(error, message):
	data = {}
	data['code'] = "ERROR" if error else "SUCCESS"
	data['data'] = message
	return HttpResponse(json.dumps(data), content_type="application/json")

#def especialidades(request):
#	return return_json_response(False, serializers.serialize('json', Especialidad.objects.filter(activa=True)))

@csrf_exempt
def login_view(request):
	cedula  = request.POST.get('cedula',"")
	password  = request.POST.get('password', "")
	user = authenticate(username=cedula, password=password)
	error = False
	message = ""
	if user is not None:
		if user.is_active:
			login(request,user)
			user.password = ""
			message =  serializers.serialize('json', [ user, ])
		else:
			error = True
			message = u"Tu cuenta no esta activa, porfavor manda un correo a viriap87@hotmail.com."
	else:
		error = True
		message = u"Valida la información del formulario, de igual manera asegurate de estar registrado."
	return return_json_response(error, message)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email)
        return True
    except ValidationError:
        return False

def create_user(nombre,email,is_active,cedula,password):
	try:
		usuario = User()
		usuario.nombre = nombre
		usuario.email = email
		usuario.is_active = is_active
		usuario.cedula = cedula
		usuario.set_password(password)
		usuario.save()
		return usuario
	except Exception as e:
		print e
		return None

def existe_usuario_email(email):
	try:
		return User.objects.get(email=email)
	except:return None

def existe_usuario_cedula(cedula):
	try:
		return User.objects.get(cedula=cedula)
	except:return None


@csrf_exempt
def signup_view(request):
	email  = request.POST.get('email',"")
	nombre  = request.POST.get('nombre',"")
	password_2  = request.POST.get('password_2',"")
	password  = request.POST.get('password', "")
	cedula  = request.POST.get('cedula', "")
	error = False
	message = ""
	if (not (email and nombre and password and password_2 and cedula)) or not ( validateEmail(email) ):
		error = True
		message = u"Valida la información del formulario."
	else:
		if password_2 != password:
			error = True
			message = u"Las contraseñas deben coincidir."
		else:
			if ( not existe_usuario_cedula(cedula) ) and ( not existe_usuario_email(email) ):
				if not create_user(nombre, email, False, cedula, password_2):
					error = True
					message = u"Hubo algún problema con el servidor, intentalo de nuevo, si el problema persiste manda un correo a viriap87@hotmail.com"
				else:
					message =  u"Tu cuenta se validará para ver que tu Cédula sea correcta."
			else:
				error = True
				message = u"Ya existe un usuario con este email o cédula, si tienes aĺgún problema haciendo login manda un correo a viriap87@hotmail.com"
	return return_json_response(error, message)


def ya_pago(user):
	return user.pagado


def obtener_cuadros_generales_subfarmacos(request):
	try:
		farmaco = Farmaco.objects.get(clave=request.GET['farmaco_clave'])
		farmacos_cuadros = FarmacoCuadro.objects.filter(farmaco=farmaco, habilitado=True)
		imagenes_farmacos_cuadros = ["http://localhost:8000"+m.imagen.url for m in farmacos_cuadros]
		subfarmacos = SubFarmaco.objects.filter(habilitado=True, farmaco=farmaco)
		subfarmacos_lista = [o.nombre + "|"+ str(o.id) for o in subfarmacos]
		return return_json_response(False, [imagenes_farmacos_cuadros, subfarmacos_lista])
	except Exception as e:
		print e
		return return_json_response(True, {})

def tiene_formulas(request):
	subfarmaco = SubFarmaco.objects.get(id=request.GET['subfarmaco_id'])
	formulas = FormulaSubFarmaco.objects.filter(subfarmaco=subfarmaco)
	formulas_ = False
	if formulas:
		formulas_ = True
	return return_json_response(False, formulas_)

def obtener_efectos_adversos(request):
	subfarmaco = SubFarmaco.objects.get(id=request.GET['subfarmaco_id'])
	return return_json_response(False, subfarmaco.efectos_adversos)

def obtener_lista_formulas(request):
	subfarmaco = SubFarmaco.objects.get(id=request.GET['subfarmaco_id'])
	formulas = FormulaSubFarmaco.objects.filter(subfarmaco=subfarmaco)
	lista_formulas = [o.nombre_formula + "|" + str(o.id) for o in formulas]
	return return_json_response(False, lista_formulas)

def formula_html(request):
	formula_farmaco= FormulaSubFarmaco.objects.get(id=request.GET['formula_farmaco_id'])
	return return_json_response(False, formula_farmaco.formulario_html)


def calcular_formula(request):
	formula_farmaco = FormulaSubFarmaco.objects.get(id=request.GET['formula_farmaco_id'])
	try: 
		edad = int(request.GET.get('edad',0))
	except:
		edad = 0
	formula_farmaco.calcular_formula(edad)
	attributes = inspect.getmembers(formula_farmaco, lambda a:not(inspect.isroutine(a)))
	necesarios = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__') or a[0].startswith('_') or a[0] in ("DoesNotExist", "MultipleObjectsReturned", "subfarmaco", "formula", "nombre_formula", "pk", "subfarmaco_id", "id"))]
	return return_json_response(False,dict(necesarios))