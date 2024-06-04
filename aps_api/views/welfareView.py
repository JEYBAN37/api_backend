from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.managers.welfare import Welfare
from aps_api.serializers.welfareSerializers import WelfareSerializers, CustomSerializers, CustomUpdateSerializers
from rest_framework import status
from aps_api.properties.request import mss, keys_welfare
from aps_api.utils.querys import post_request, get_request, update_request, delete_request


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, Welfare, WelfareSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, Welfare, CustomSerializers, WelfareSerializers, keys_welfare)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, Welfare, CustomUpdateSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(Welfare, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
