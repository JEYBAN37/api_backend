from aps_api.managers.pollster import Pollster
from aps_api.properties.coverters import jobs
from aps_api.serializers.contactSerializers import ContactMemberSerializers
from aps_api.serializers.nameSerializers import NameSerializers, NameMemberSerializers
from aps_api.serializers.userRegisterSerializers import UserRegisterSerializers
from aps_api.utils.serializersGeneric import SerializerEnlace
from rest_framework import serializers


class PollsterSerializers(serializers.ModelSerializer):
    user = UserRegisterSerializers()
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()

    class Meta:
        model = Pollster
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.job = validated_data.get('job', instance.job)
        instance.user = self.fields['user'].update(instance.user, validated_data.get('user', {}))
        instance.name_person = self.fields['name_person'].update(instance.name_person,
                                                                 validated_data.get('name_person', {}))
        instance.contact = self.fields['contact'].update(instance.contact, validated_data.get('contact', {}))

        instance.save()
        return instance



class CustomSerializers(SerializerEnlace):
    user = UserRegisterSerializers()
    class Meta:
        model = Pollster
        fields = ['name_person', 'id', 'contact','user','job']


class CustomUpdateSerializers(SerializerEnlace):
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()
    class Meta:
        model = Pollster
        fields = ['name_person','contact','job']


class NombreSerializer(SerializerEnlace):
    name_person = NameSerializers()
    class Meta:
        model = Pollster
        fields = ['name_person','user','job']


class PollsterSerializersAdd(SerializerEnlace):
    class Meta:
        model = Pollster
        fields = '__all__'
