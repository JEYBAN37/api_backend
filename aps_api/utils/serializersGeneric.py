from rest_framework import serializers
from aps_api.managers.contact import Contact
from aps_api.managers.names import Names
from aps_api.serializers.nameSerializers import NameMemberSerializers
from aps_api.serializers.contactSerializers import ContactMemberSerializers


class SerializerEnlace(serializers.ModelSerializer):
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()

    def create(self, validated_data):
        name_data = validated_data.pop('name_person')
        name_instance = Names.objects.create(**name_data)
        contact_data = validated_data.pop('contact')
        contact_instance = Contact.objects.create(**contact_data)

        member_instance = self.Meta.model.objects.create(name_person=name_instance, contact=contact_instance,
                                                         **validated_data)
        return member_instance

    def update(self, instance, validated_data):

        # Actualiza los campos anidados (si es necesario)
        name_data = validated_data.pop('name_person', None)
        contact_data = validated_data.pop('contact', None)

        if name_data or contact_data:
            # Actualiza el campo name_person
            name_serializer = self.fields['name_person']
            contact_serializer = self.fields['contact']
            name_serializer.update(instance.name_person, name_data)
            contact_serializer.update(instance.contact, contact_data)
        return instance

