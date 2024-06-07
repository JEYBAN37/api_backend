from rest_framework import serializers

from aps_api.managers.member import Member
from aps_api.managers.names import Names
from aps_api.properties.coverters import type_id_mapping, type_id_mapping_reverse, eps_member, role_mapping, sex_mapping
from aps_api.serializers.atributesMemberSerializers import AtributesAnaliticSerializers
from aps_api.serializers.contactSerializers import ContactMemberSerializers
from aps_api.serializers.nameSerializers import NameMemberSerializers
from aps_api.utils.serializersGeneric import SerializerEnlace


class MemberSerializers(SerializerEnlace):
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()

    class Meta:
        model = Member
        fields = '__all__'

    def to_internal_value(self, data):
        data['type_id'] = type_id_mapping_reverse.get(data['type_id'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['type_id'] = type_id_mapping.get(data['type_id'])
        return data


class CustomSerializers(SerializerEnlace):
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()

    class Meta:
        model = Member
        fields = ['id', 'family', 'name_person', 'contact', 'type_id', 'date_birth',
                  'sex', 'affiliation_regime', 'eps', 'etnia', 'role']

    def to_internal_value(self, data):
        data.type_id = type_id_mapping_reverse.get(data['type_id'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['eps'] = eps_member.get(data['eps'])
        data['role'] = role_mapping.get(data['role'])
        data['sex'] = sex_mapping.get(data['sex'])
        return data


class CustomUpdateSerializers(SerializerEnlace):
    name_person = NameMemberSerializers()
    contact = ContactMemberSerializers()

    def to_internal_value(self, data):
        data['type_id'] = type_id_mapping_reverse.get(data['type_id'])
        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        name_person_data = validated_data.pop('name_person', None)
        contact_data = validated_data.pop('contact', None)

        if name_person_data:
            for attr, value in name_person_data.items():
                setattr(instance.name_person, attr, value)
            instance.name_person.save()

        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contact, attr, value)
            instance.contact.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = Member
        fields = '__all__'


class ResponsableSerializer(SerializerEnlace):
    class Meta:
        model = Member
        fields = ['id', 'present_person', 'name_person', 'contact', 'role']


class SaveMemberSerializers(serializers.ModelSerializer):
    contact = ContactMemberSerializers()
    name_person = NameMemberSerializers()

    class Meta:
        model = Member
        fields = '__all__'

class MemberFamiliySerializer(SerializerEnlace):
    contact = ContactMemberSerializers()
    name_person = NameMemberSerializers()
    class Meta:
        model = Member
        fields = ['id', 'name_person', 'contact', 'role', 'date_birth']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['role'] = role_mapping.get(data['role'])
        return data


class MemberFamilySerializers(serializers.ModelSerializer):
    contact = ContactMemberSerializers()
    name_person = NameMemberSerializers()
    member_atributes = AtributesAnaliticSerializers()
    class Meta:
        model = Member
        fields = ['name_person','contact','sex','etnia','affiliation_regime','role','member_atributes','present_person']
