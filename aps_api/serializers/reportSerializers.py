from rest_framework import serializers
from aps_api.managers.report import Report


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        
class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['serial_id','type_register','type_entidad','id_entidad','date_init','date_final','number_family']

class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['serial_id']
