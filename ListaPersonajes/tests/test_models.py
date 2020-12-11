from django.test import TestCase
from ListaPersonajes.models import Personaje
from django.core.files.uploadedfile import SimpleUploadedFile



class PersonajeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        image1 = SimpleUploadedFile(name='test_imagen1.jpg', content=b'', content_type='image/jpeg')
        image2 = SimpleUploadedFile(name='test_imagen2.jpg', content=b'', content_type='image/jpeg')
        image3 = SimpleUploadedFile(name='test_imagen3.jpg', content=b'', content_type='image/jpeg')
        Personaje.objects.create(Nombre='Naruto', Apellido='Uzumaki', imagen1=image1, imagen2=image2,imagen3=image3)

    def test_Nombre_label(self):
        personaje=Personaje.objects.get(id=1)
        field_label = personaje._meta.get_field('Nombre').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_Apellido_label(self):
        personaje=Personaje.objects.get(id=1)
        field_label = personaje._meta.get_field('Apellido').verbose_name
        self.assertEquals(field_label,'Apellido')

    def test_Nombre_max_length(self):
        personaje=Personaje.objects.get(id=1)
        max_length = personaje._meta.get_field('Nombre').max_length
        self.assertEquals(max_length,100)

    def test_Apellido_max_length(self):
        personaje=Personaje.objects.get(id=1)
        max_length = personaje._meta.get_field('Apellido').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        personaje=Personaje.objects.get(id=1)
        expected_object_name = '%s, %s' % (personaje.Nombre, personaje.Apellido)
        self.assertEquals(expected_object_name,str(personaje))

    
