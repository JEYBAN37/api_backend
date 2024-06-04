from rest_framework import serializers
from aps_api.managers.channelEntity import ChannelEntity

class ChannelEntitySerializers(serializers.ModelSerializer):
    class Meta:
        model=ChannelEntity
        fields='__all__'

class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model=ChannelEntity
        fields=['serial_id','name','type','campus']
        
class CustomUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model=ChannelEntity
        fields=['serial_id']