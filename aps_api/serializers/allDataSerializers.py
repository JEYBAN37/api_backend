from rest_framework import serializers
from aps_api.managers.family import Family
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