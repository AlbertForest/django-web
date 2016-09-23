#urls de contacte
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.contactes),
	url(r'^contacte/',views.contacte),
	]