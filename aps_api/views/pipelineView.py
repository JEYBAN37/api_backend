from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.managers.pipelines import Pipelines
from aps_api.serializers.pipelinesSerializers import PipelinesSerializers, CustomSerializers, CustomUpdateSerializers
from rest_framework import status
from aps_api.properties.request import mss, keys_pipeline
from aps_api.utils.querys import post_request, get_request, update_request, delete_request

@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, Pipelines, PipelinesSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, Pipelines, CustomSerializers, PipelinesSerializers, keys_pipeline)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, Pipelines, CustomUpdateSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(Pipelines, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)