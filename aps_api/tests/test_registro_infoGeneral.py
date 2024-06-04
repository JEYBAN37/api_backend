import json
import os

from django.test import Client, TestCase
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.managers.pollster import Pollster
from aps_api.managers.names import Names
from aps_api.managers.contact import Contact
from django.contrib.auth.models import User

class RegistroInfoGeneralTestCase(TestCase):
    def tearDown(self):
        InfoGeneral.objects.all().delete()
        Pollster.objects.all().delete()
        Names.objects.all().delete()
        Contact.objects.all().delete()

    def setUp(self):
        self.client = Client()
        self.url = '/api/info_general/add/'
        file_path = os.path.join(os.path.dirname(__file__), './responses/data_infoGeneral.json')
        self.assert_data = json.loads(open(file_path, encoding='utf-8').read())
        
        # Crear instancias de los modelos relacionados
        self.name_person=Names.objects.create(name='carlos',second_name='carlos',last_name='perez',second_last_name='perez', id_document='1098645342')
        self.contact=Contact.objects.create(email='test@example.com', telephone='1234567890')
        self.user = User.objects.create_user(username='testuser', password='123')
        # Crear un objeto Pollster para usar en la prueba
        self.pollster = Pollster.objects.create(
            name_person=self.name_person,
            contact=self.contact,
            job='110',
            user=self.user
        )
        
        self.assert_data['pollster'] = self.pollster.id

    def test_registro(self):
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 201)
    
    def test_campo_obligatorio_estratum(self):
        self.tearDown()
        
        InfoGeneral.objects.create(
            id=4,
            type_register=2,
            number_register=1,
            consent=1,
            zonal_unit="UZPE999",
            departament="52",
            municipality="52001",
            territory="T99",
            microterritory="T99",
            name_branding="poblado",
            address="manzana 2 casa 4",
            creation_date="2024-05-17",
            id_primary_provider="5200100107",
            people=1,
            longitud="-77.27498500",
            latitud="1.20340780",
            home_location="parque poblado",
            id_familia="52UZPE99952001T99T99EBSF7534",
            estratum=2,
            households="1",
            num_families=1,
            basic_team="52UZPE99952001T99T99EBS",
            pollster=self.pollster,
            id_ficha="CF")
        
      
        self.assert_data['estratum'] = ""
        
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)
    
    def test_registro_people_invalido(self):
        self.tearDown()

        InfoGeneral.objects.create(
            id=4,
            type_register=2,
            number_register=1,
            consent=1,
            zonal_unit="UZPE999",
            departament="52",
            municipality="52001",
            territory="T99",
            microterritory="T99",
            name_branding="poblado",
            address="manzana 2 casa 4",
            creation_date="2024-05-17",
            id_primary_provider="5200100107",
            people=1,
            longitud="-77.27498500",
            latitud="1.20340780",
            home_location="parque poblado",
            id_familia="52UZPE99952001T99T99EBSF7534",
            estratum=2,
            households="1",
            num_families=1,
            basic_team="52UZPE99952001T99T99EBS",
            pollster=self.pollster,
            id_ficha="CF")
        

        self.assert_data['people'] = "prueba"
        
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)