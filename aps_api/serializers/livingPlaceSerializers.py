from rest_framework import serializers
from aps_api.managers.livingpPlace import LivingPlace
from aps_api.properties.coverters import yn_mapping, type_living_place_map, wall_material_map, floor_material_map, \
    roof_material_map, irrigation_scenarios_map
from aps_api.serializers.sanitationSerializers import allSanitationSerializers


class LivingPlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = LivingPlace
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = LivingPlace
        fields = ['serial_id', 'info_general', 'type_living_place', 'animals', 'vectors_description', 'transmitting_vectors',
                  'bedrooms', 'access_to_home']


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = LivingPlace
        read_only_fields = ['serial_id', 'info_general']


class AllLivingSerializers(serializers.ModelSerializer):
    sanation = allSanitationSerializers()
    class Meta:
        model = LivingPlace
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['type_living_place'] = type_living_place_map.get(data['type_living_place'])
        data['wall_material'] = wall_material_map.get(data['wall_material'])
        data['floor_material'] = floor_material_map.get(data['floor_material'])
        data['roof_material'] = roof_material_map.get(data['roof_material'])
        data['over_population'] = yn_mapping.get(data['over_population'])
        data['transmitting_vectors'] = yn_mapping.get(data['transmitting_vectors'])
        data['economic_activity'] = yn_mapping.get(data['economic_activity'])
        return data