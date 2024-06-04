import json
import os

from django.test import Client, TestCase
from aps_api.managers.sanitation import Sanitation
from aps_api.managers.livingpPlace import LivingPlace
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.managers.pollster import Pollster
from aps_api.managers.names import Names
from aps_api.managers.contact import Contact
from django.contrib.auth.models import User

class RegistroSanitation(TestCase):
    def tearDown(self):
        InfoGeneral.objects.all().delete()
        Pollster.objects.all().delete()
        Names.objects.all().delete()
        Contact.objects.all().delete()
        LivingPlace.objects.all().delete()
        Sanitation.objects.all().delete()

    def setUp(self):
        self.client = Client()
        self.url = '/api/sanation/add/'
        file_path = os.path.join(os.path.dirname(__file__), './responses/data_sanitation.json')
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
        
        self.info_general =InfoGeneral.objects.create(
            id=3,
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
            id_ficha="CF"
        )
        
        self.living_place = LivingPlace.objects.create(
            id=1,
            info_general=self.info_general,
            type_living_place=1,
            description="ejemplo",
            wall_material=1,
            other_wall_material="ejemplo",
            floor_material=1,
            other_floor_material="ejemplo",
            roof_material=1,
            other_roof_material="ejemplo",
            bedrooms=3,
            over_population=1,
            irrigation_scenarios=[1],
            access_to_home=[1],
            food_source=[1],
            other_food_source="ejemplo",
            transmitting_vectors=1,
            vectors_description="ejemplo",
            places_around=[1],
            other_places_around="ejemplo",
            economic_activity=1,
            animals=[1],
            other_animals="ejemplo"
        )
        self.assert_data['living_place_id'] = self.living_place.id
        
    def test_registro(self):
        response = self.client.post(self.url, self.assert_data)
        if response.status_code != 201:
            print("Error response content:", response.content)  # Diagnóstico: Imprimir contenido de la respuesta
        self.assertEqual(response.status_code, 201)
    