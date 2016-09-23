from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Dades empresa
class empresa(models.Model):
	id_empresa = models.AutoField(primary_key=True)
	nom_empresa = models.CharField(max_length=40)
	mail_empresa = models.EmailField(max_length=80)
	tlf_empresa = models.CharField(max_length=9)
	adr_empresa = models.CharField(max_length=80)
	cp_empresa = models.CharField(max_length=5)
    #logo_empresa = models.ImageField(upload_to='uploads' ,verbose_name='Empresa_imatge')

	def __unicode__(self):
 		return u'%s' % (self.nom_empresa)

	class Meta:
		ordering = ['nom_empresa']

class centre(models.Model):
	id_centre = models.AutoField(primary_key=True)
	nom_centre = models.CharField(max_length=40)
	cit_centre = models.CharField(max_length=20)
	cp_centre = models.CharField(max_length=80)
	tlf_centre = models.CharField(max_length=9)
	mail_centre = models.EmailField(max_length=80)
	cod_empresa = models.ForeignKey(empresa)


	def __unicode__(self):
 		return u'%s' % (self.nom_centre)


	class Meta:
		ordering = ['nom_centre']

