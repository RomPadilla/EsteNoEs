from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.

class Personaje(models.Model):
	"""Model representing an author."""
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	imagen1 = models.ImageField(upload_to='images')
	imagen2 = models.ImageField(upload_to='images')
	imagen3 = models.ImageField(upload_to='images')

	class Meta:
		ordering = ['Apellido', 'Nombre']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return '%s, %s' % (self.Nombre, self.Apellido)
