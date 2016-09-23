from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here

# Dades noticies
class post(models.Model):
	id_post = models.AutoField(primary_key=True)
	titol_post = models.CharField("Titol de la noticia",max_length=100)
	text_post = models.TextField("Contingut de la noticia")
	autor_post = models.ForeignKey("auth.User")
	creacio_post = models.DateTimeField(default=timezone.now)
	#cod_categoria = models.ForeignKey(categoria)

    #logo_empresa = models.ImageField(upload_to='uploads' ,verbose_name='Empresa_imatge')

	def __unicode__(self):
 		return u'%s' % (self.titol_post)

	class Meta:
		ordering = ['titol_post']

class categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	nom_categoria = models.CharField("Titol de la categoria",max_length=100)
	#pare_categoria = models.ForeignKey("Contingut de la noticia")

    #logo_empresa = models.ImageField(upload_to='uploads' ,verbose_name='Empresa_imatge')

	def __unicode__(self):
 		return u'%s' % (self.titol_post)

	class Meta:
		ordering = ['nom_categoria']