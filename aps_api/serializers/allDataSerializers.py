from rest_framework import serializers
from aps_api.managers.family import Family
from aps_api.properties.coverters import family_type_mapping, family_garph_mapping, family_garph_apgar, yn_mapping, \
    family_garph_zarit, family_garph_ecomapa
from aps_api.serializers.memberSerializers import MemberFamilySerializers
from aps_api.serializers.familyContextSerializers import FamilyContextAnaliticSerializers
from aps_api.serializers.infoGeneralSerializers import  AllInfoGeneralSerializers
from aps_api.serializers.welfareSerializers import WelfareSerializers


class FamilyAllSerializers(serializers.ModelSerializer):
    in_charge = MemberFamilySerializers(many=True)
    family_context = FamilyContextAnaliticSerializers()
    info_general=AllInfoGeneralSerializers()
    welfare = WelfareSerializers()
    class Meta:
        model = Family
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['family_type'] = family_type_mapping.get(data['family_type'])
        data['family_graphic'] = family_garph_mapping.get(data['family_graphic'])
        data['apgar'] = family_garph_apgar.get(data['apgar'])
        data['carer'] = yn_mapping.get(data['carer'])
        data['zarit'] = family_garph_zarit.get(data['zarit'])
        data['ecomapa'] = family_garph_ecomapa.get(data['ecomapa'])
        return data
