from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.managers.livingpPlace import LivingPlace
from aps_api.serializers.livingPlaceSerializers import LivingPlaceSerializers, CustomSerializers, CustomUpdateSerializers
from rest_framework import status
from aps_api.utils.querys import get_request, post_request, update_request, delete_request
from aps_api.properties.request import mss, keys_family


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, LivingPlace, LivingPlaceSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, LivingPlace, LivingPlaceSerializers, LivingPlaceSerializers, keys_family)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, LivingPlace, LivingPlaceSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(LivingPlace, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
