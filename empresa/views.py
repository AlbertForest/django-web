from django.shortcuts import render
from .models import empresa,centre

# Create your views here.

def dades_empresa(request):
	#consulta de les dades
	dataEmp = empresa.objects.order_by('id_empresa')
	#renderitzar la pagina
	return render(request,'empresa.html',{'dataEmp':dataEmp})
