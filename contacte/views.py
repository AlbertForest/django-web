from django.shortcuts import render
from .models import contacte

# Create your views here.

def contacte(request):
	#consulta de les dades
	dataCont = contacte.objects.order_by('id_contacte')
	#renderitzar la pagina
	return render(request,'contacte.html',{'dataCont':dataCont})