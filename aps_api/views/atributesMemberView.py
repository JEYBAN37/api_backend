from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.managers.atributesMember import AtributesMember
from aps_api.managers.member import Member
from aps_api.serializers.atributesMemberSerializers import AtributesMemberSerializers, CustomSerializers, CustomUpdateSerializers
from rest_framework import status
from aps_api.utils.querys import get_request, post_request, update_request, delete_request, delete_request_member
from aps_api.properties.request import mss, keys_member_atributes


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, AtributesMember, AtributesMemberSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, AtributesMember, CustomSerializers, AtributesMemberSerializers, keys_member_atributes)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, AtributesMember, AtributesMemberSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request_member(AtributesMember, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def count_sport(request):
    try:
     
        count_opcion_si = AtributesMember.objects.filter(sport=1).count()
        count_opcion_no = AtributesMember.objects.filter(sport=2).count()

        # Crear la respuesta con los contadores
        data = [
            {'name': 'Opcion Si', 'total': count_opcion_si},
            {'name': 'Opcion No', 'total': count_opcion_no},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

