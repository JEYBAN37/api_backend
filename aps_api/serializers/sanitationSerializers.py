from rest_framework import serializers
from aps_api.managers.sanitation import Sanitation


class SanitationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sanitation
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sanitation
        fields = ['serial_id', 'living_place_id', 'water_supply', 'disposal_system', 'residual_water', 'Solid_waste',
                  'hygiene', 'kitchen_toilet']


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sanitation
        read_only_fields = ['serial_id', 'living_place_id']
