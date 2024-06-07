from rest_framework import serializers
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.serializers.familySerializers import FamilyAnaliticSerializers


class InfoAnaliticSerializer(serializers.ModelSerializer):
    family = FamilyAnaliticSerializers(many=True)
    class Meta:
        model = InfoGeneral
        fields = ['id','estratum','creation_date','people','family','name_branding','address','num_families',
                  'longitud','latitud']