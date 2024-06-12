from rest_framework import serializers
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.serializers.livingPlaceSerializers import AllLivingSerializers

from aps_api.serializers.pollsterSerializers import CustomUpdateSerializers
from aps_api.properties.coverters import estratum_mapping, departaments_mapping, municipality_mapping, dict_options_ese



class InfoGeneralSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = ['id', 'departament', 'municipality', 'address',
                  'creation_date', 'id_primary_provider', 'people','longitud','latitud','estratum']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'municipality' in data:
            data['municipality'] = municipality_mapping.get(data['municipality'], data['municipality'])
            data['departament'] = departaments_mapping.get(data['departament'])
            data['id_primary_provider'] = dict_options_ese.get(data['id_primary_provider'])

        return data


class CustomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = ['departament', 'municipality', 'name_branding', 'address', 'num_families',
                  'people','home_location', 'estratum', 'id_primary_provider', 'pollster']


class EstadisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = ['num_families', 'creation_date']


class FamilyGeneralSerializers(serializers.ModelSerializer):
    pollster = CustomUpdateSerializers()
    class Meta:
        model = InfoGeneral
        fields = ['departament', 'municipality', 'name_branding', 'address', 'num_families',
                  'people', 'pollster', 'home_location', 'estratum','creation_date','latitud','longitud', 'id_primary_provider']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if 'estratum' in data:
            data['estratum'] = estratum_mapping.get(data['estratum'], data['estratum'])

        if 'departament' in data:
            data['departament'] = departaments_mapping.get(data['departament'])

        if 'municipality' in data:
            data['municipality'] = municipality_mapping.get(data['municipality'], data['municipality'])

        return data

class AllInfoGeneralSerializers(serializers.ModelSerializer):
    living_place = AllLivingSerializers()
    class Meta:
        model = InfoGeneral
        fields = '__all__'