from rest_framework import serializers
from aps_api.managers.livingpPlace import LivingPlace
from aps_api.serializers.sanitationSerializers import SanitationSerializers


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
    sanation = SanitationSerializers()
    class Meta:
        model = LivingPlace
        fields = '__all__'