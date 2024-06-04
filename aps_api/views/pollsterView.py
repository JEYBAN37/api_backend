from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from aps_api.managers.pollster import Pollster
from aps_api.serializers.pollsterSerializers import (PollsterSerializers,
                                                     PollsterSerializersAdd)
from rest_framework import status
from aps_api.properties.request import keys_member, mss, keys_pollster
from aps_api.utils.querys import get_request, post_request, update_request, delete_request
from aps_api.permissions import IsAnalyst, IsSurveyor, IsAdministrator, IsChannelizer


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, Pollster, PollsterSerializersAdd)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        print(request.data)
        return get_request(request, Pollster, PollsterSerializers, PollsterSerializers, keys_pollster)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, Pollster, PollsterSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(Pollster, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
