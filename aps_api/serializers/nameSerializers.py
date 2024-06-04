from rest_framework import serializers
from aps_api.managers.names import Names
from aps_api.serializers.contactSerializers import ContactMemberSerializers


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = '__all__'


class NameMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = ['name', 'second_name', 'last_name', 'id', 'second_last_name','id_document']


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = ['name']