from rest_framework import serializers
from aps_api.managers.family import Family
from aps_api.managers.member import Member
from aps_api.serializers.infoGeneralSerializers import CustomSerializers, FamilyGeneralSerializers, InfoGeneralSerializers
from aps_api.serializers.memberSerializers import ResponsableSerializer
from aps_api.serializers.pollsterSerializers import CustomUpdateSerializers
from aps_api.properties.coverters import family_type_mapping


class FamilySerializers(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = '__all__'



class FamilyGetSerializers(serializers.ModelSerializer):
    info_general = CustomSerializers()

    class Meta:
        model = Family
        fields = ['id', 'info_general', 'family_type', 'total_members', 'observation']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['family_type'] = family_type_mapping.get(representation['family_type'])
        return representation

class CustomSerializers(serializers.ModelSerializer):
    info_general = CustomSerializers()
    in_charge = serializers.SerializerMethodField()

    class Meta:
        model = Family
        fields = ['id', 'info_general', 'family_type', 'total_members', 'in_charge']
    def get_in_charge(self, obj):
        # Filtrar los miembros responsables con present_person igual a 1 para la familia actual
        members_responsible = obj.in_charge.filter(present_person=1)
        # Serializar los miembros responsables
        member_serializer = ResponsableSerializer(members_responsible, many=True)
        return member_serializer.data

    def to_representation(self, instance):
        # Obtener la representación de la familia utilizando el método de la clase base
        representation = super().to_representation(instance)
        # Agregar los miembros responsables a la representación de la familia
        representation['in_charge'] = self.get_in_charge(instance)
        representation['family_type'] = family_type_mapping.get(representation['family_type'])
        return representation

    def to_representationDos(self, instance):
        data = super().to_representation(instance)
        if 'family_type' in data:
            data['family_type'] = family_type_mapping.get(data['family_type'], data['family_type'])
        return data




class CustomUpdateSerializers(serializers.ModelSerializer):
    info_general = FamilyGeneralSerializers()
    class Meta:
        model = Family
        fields = ['family_type', 'family_graphic', 'apgar', 'carer', 'zarit', 'ecomapa','info_general','total_members']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['family_type'] = family_type_mapping.get(data['family_type'])
        return data

class CustomFamilyMemberSerializers(serializers.ModelSerializer):
    info_general = FamilyGeneralSerializers()
    class Meta:
        model = Family
        fields = ['family_type', 'family_graphic', 'apgar', 'carer', 'zarit', 'ecomapa','total_members']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['family_type'] = family_type_mapping.get(data['family_type'])
        return data


