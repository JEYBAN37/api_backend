from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.managers.familyContext import FamilyContext
from aps_api.serializers.familyContextSerializers import FamilyContextSerializers, CustomSerializers, CustomUpdateSerializers
from rest_framework import status
from aps_api.utils.querys import get_request, post_request, update_request, delete_request
from aps_api.properties.request import mss, keys_family_context


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, FamilyContext, FamilyContextSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, FamilyContext, FamilyContextSerializers, FamilyContextSerializers, keys_family_context)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, FamilyContext, FamilyContextSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(FamilyContext, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def count_vulnerability(request):
    try:
        # Contar los registros con vulnerability = 1
        count_vulnerability_1 = FamilyContext.objects.filter(vulneravility=1).count()
        # Contar los registros con vulnerability = 2
        count_vulnerability_2 = FamilyContext.objects.filter(vulneravility=2).count()

        # Crear la respuesta con los contadores
        data = [
            {'name': 'Opcion Si', 'total Si': count_vulnerability_1},
            {'name': 'Opcion No', 'total No': count_vulnerability_2},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def count_antecedent_salud(request):
    try:
        count_opcion_si = FamilyContext.objects.filter(antecedent_salud=1).count()
        count_opcion_no = FamilyContext.objects.filter(antecedent_salud=2).count()

        # Crear la respuesta con los contadores
        data = [
            {'name': 'Opcion Si', 'total Si': count_opcion_si},
            {'name': 'Opcion No', 'total No': count_opcion_no},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def count_victim(request):
    try:
        count_opcion_si = FamilyContext.objects.filter(victim=1).count()
        count_opcion_no = FamilyContext.objects.filter(victim=2).count()

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
    
@api_view(['GET'])
def count_disability(request):
    try:
        count_opcion_si = FamilyContext.objects.filter(disable=1).count()
        count_opcion_no = FamilyContext.objects.filter(disable=2).count()

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
    
@api_view(['GET'])
def count_disease_prevention(request):
    try:

        count_opcion_si = FamilyContext.objects.filter(family_welfare=1).count()
        count_opcion_no = FamilyContext.objects.filter(family_welfare=2).count()

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

@api_view(['GET'])
def count_healthy_habits(request):
    try:

        count_opcion_si = FamilyContext.objects.filter(healthy_habits=1).count()
        count_opcion_no = FamilyContext.objects.filter(healthy_habits=2).count()

        # Crear la respuesta
        data = [
            {'name': 'Opcion Si', 'total': count_opcion_si},
            {'name': 'Opcion No', 'total': count_opcion_no},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_familyContext_by_id(request, pk):
    try:
        family = FamilyContext.objects.get(pk=pk)
        serializer = CustomSerializers(family)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except FamilyContext.DoesNotExist:
        return Response({"detail": "Family not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
