from rest_framework import serializers
from aps_api.managers.atributesMember import AtributesMember
from aps_api.properties.coverters import canalizacion


class AtributesMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = AtributesMember
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = AtributesMember
        fields = '__all__'


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = AtributesMember
        read_only_fields = ['id', 'member']


class AtributesAnaliticSerializers(serializers.ModelSerializer):
    class Meta:
        model = AtributesMember
        fields = ['sport','disability','chronic_condition','canalization']
