from rest_framework import serializers
from aps_api.managers.pipelines import Pipelines


class PipelinesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pipelines
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pipelines
        fields = ['serial_id', 'channel', 'state']


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pipelines
        fields = ['serial_id']
