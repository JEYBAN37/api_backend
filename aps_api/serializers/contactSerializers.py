from rest_framework import serializers
from aps_api.managers.contact import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['telephone', 'email']
        
class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['serial_id']
