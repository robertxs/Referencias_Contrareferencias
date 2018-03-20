from django.shortcuts import render, redirect
from django.views.generic import *
from paciente.models import *
from administrador.models import *
from .models import *
from .forms import *
from django.template.context_processors import csrf
from controllers import *

class CrearExamen(CreateView):
	template_name = 'bioanalista/crear_examen.html'
	form_class = ExamenForm
	
	def get(self, request):
		form = ExamenForm()
		
		return render(request, 'bioanalista/crear_examen.html', {'form' : form})
		
	def post(self, request):
		form = ExamenForm(request.POST)
		tipo_examen = request.POST.get('tipo_examen')
		paciente = request.POST.get('paciente')
		laboratorio = request.POST.get('laboratorio')
		tipoexamen = Tipoexamen.objects.filter(nombretipo = tipo_examen)
		
		# En caso de que se haya seleccionado un tipo de examen
		if(tipoexamen and not request.POST.get('filledform')):
			form.fields['paciente'].widget.attrs['disabled'] = True
			form.fields['tipo_examen'].widget.attrs['disabled'] = True
			form.fields['laboratorio'].widget.attrs['disabled'] = True
			mediciones = Medicion.objects.filter(tipoexamen = tipoexamen)
			context = {'form' : form,
						'mediciones' : mediciones,
						'paciente' : paciente,
						'laboratorio' : laboratorio,
						'tipo_examen' : tipo_examen
						}
			context.update(csrf(request))
			
			return render(request, 'bioanalista/crear_examen.html', context)
		
		# En caso de que ya se hayan seleccionado los valores para las mediciones
		elif(request.POST.get('filledform')):
			paciente = Paciente.objects.get(cedula = paciente)
			laboratorio = Laboratorio.objects.get(pk = laboratorio)
			user_pk = request.user.pk
			user = User.objects.get(pk = user_pk)
			usuario = Usuario.objects.get(user = user)
			bioanalista = Bioanalista.objects.get(usuario = usuario)
			tipoexamen = Tipoexamen.objects.get(nombretipo = tipo_examen)
			examen = Examen(paciente = paciente, bioanalista = bioanalista, laboratorio = laboratorio, tipoexamen = tipoexamen)
			examen.save()

			for elem in request.POST:
				if(elem not in ['paciente', 'filledform', 'laboratorio', 'tipo_examen', 'csrfmiddlewaretoken']):
					medicion = Medicion.objects.get(nombremedicion = elem)
					resultado = Resultadomedicion(examen = examen, medicion = medicion, resultado = request.POST.get(elem))
					resultado.save()
				
			return redirect('ver_examenes_bioanalista')
			return render(request, 'home.html', {})
		
		return render(request, 'bioanalista/crear_examen.html', {'form' : form})
		
		
class VerExamenes(CreateView):
	template_name = 'bioanalista/ver_examenes.html'

	def get(self, request):
		user_pk = request.user.pk
		user = User.objects.get(pk = user_pk)
		usuario = Usuario.objects.get(user = user)
		bioanalista = Bioanalista.objects.get(usuario = usuario)
		examenes = Examen.objects.filter(bioanalista = bioanalista)
		context = { 'examenes' : examenes }
		
		return render(request, 'bioanalista/ver_examenes.html', context)
		
	def post(self, request):
		pass
		
class DetallesExamen(TemplateView):
	template_name = 'bioanalista/detalles_examen.html'
	
	def get(self, request, examen_id):
		examen = Examen.objects.get(pk = examen_id)
		resultados = Resultadomedicion.objects.filter(examen = examen)
		#resultados = []
		#for r in aux:
		#	resultados = resultados + [r.medicion.nombremedicion]
			
		context = { 'examen' : examen,
					'resultados' : resultados
					 }
		
		return render(request, 'bioanalista/detalles_examen.html', context)

class VerSolicitudesExamen(TemplateView):
	
	def get(self, request):
		bioanalista = get_bioanalista(request.user.pk)
		laboratorio = BioanalistaEnLab.objects.get(bioanalista = bioanalista).laboratorio
		solicitudes = SolicitudExamen.objects.filter(laboratorio = laboratorio)
		
		context = {'solicitudes' : solicitudes}
		
		return render(request, 'bioanalista/ver_solicitudes_examen.html', context)
		
class AprobarSolicitudExamen(CreateView):
	
	def get(self, request, sol_id):
		solicitudExamen = SolicitudExamen.objects.get(pk = sol_id)
		mediciones = Medicion.objects.filter(tipoexamen = solicitudExamen.tipoexamen)
		form = ExamenForm(initial = {'paciente' : solicitudExamen.paciente,
									 'tipo_examen' : solicitudExamen.tipoexamen,
									 'laboratorio' : solicitudExamen.laboratorio
									})
		form.fields['paciente'].widget.attrs['disabled'] = True
		form.fields['tipo_examen'].widget.attrs['disabled'] = True
		form.fields['laboratorio'].widget.attrs['disabled'] = True
		context = {
			'solicitud' : solicitudExamen,
			'mediciones' : mediciones,
			'form' : form
			}
		
		return render(request, 'bioanalista/crear_examen.html', context)
		
	def post(self, request, sol_id):
		solicitudExamen = SolicitudExamen.objects.get(pk = sol_id)
		form = ExamenForm(request.POST)
		paciente = solicitudExamen.paciente
		laboratorio = solicitudExamen.laboratorio
		tipoexamen = solicitudExamen.tipoexamen
		
		user_pk = request.user.pk
		user = User.objects.get(pk = user_pk)
		usuario = Usuario.objects.get(user = user)
		bioanalista = Bioanalista.objects.get(usuario = usuario)
		
		examen = Examen(paciente = paciente, bioanalista = bioanalista, laboratorio = laboratorio, tipoexamen = tipoexamen)
		examen.save()

		for elem in request.POST:
			if(elem not in ['paciente', 'filledform', 'laboratorio', 'tipo_examen', 'csrfmiddlewaretoken']):
				medicion = Medicion.objects.get(nombremedicion = elem)
				resultado = Resultadomedicion(examen = examen, medicion = medicion, resultado = request.POST.get(elem))
				resultado.save()
				
		solicitudExamen.delete()
			
		return redirect('ver_solicitudes_examen')
	
		
