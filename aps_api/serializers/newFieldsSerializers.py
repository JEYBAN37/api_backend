from rest_framework import serializers
from aps_api.managers.newFields import NewFields


class NewFieldsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewFields
        fields = '__all__'
