from rest_framework import serializers
from aps_api.managers.welfare import Welfare


class WelfareSerializers(serializers.ModelSerializer):
    class Meta:
        model = Welfare
        fields = '__all__'


class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Welfare
        fields = '__all__'


class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Welfare
        fields = ['serial_id']
