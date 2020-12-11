from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.

class Informaciones(models.Model):
	"""Model representing an author."""
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='images')

	class Meta:
		ordering = ['Apellido', 'Nombre']


	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.Nombre} {self.Apellido}'	
