import datetime

from django.db.models import Sum
from django.db.models.functions import TruncDate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aps_api.serializers.infoGeneralSerializers import (InfoGeneralSerializers, CustomSerializers,
                                                        CustomUpdateSerializers, EstadisticSerializer,
                                                        CustomUpdateSerializer)
from aps_api.managers.infoGeneral import InfoGeneral
from rest_framework import status
from aps_api.properties.request import keys_info_general, mss
from aps_api.utils.querys import get_request, post_request, update_request, delete_request
from datetime import date


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, InfoGeneral, InfoGeneralSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, InfoGeneral, CustomSerializers, InfoGeneralSerializers, keys_info_general)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, InfoGeneral, CustomUpdateSerializer, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(InfoGeneral, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def counter_families(request, pk):
    try:
        end_date = date.today()
        start_date = end_date - datetime.timedelta(days=7)
        results = (
            InfoGeneral.objects
            .filter(pollster=pk)
            .filter(creation_date__range=[start_date, end_date])
            .annotate(day=TruncDate('creation_date'))
            .values('day')
            .annotate(total_families=Sum('num_families'))
            .order_by('day')
        )
        # Lista para almacenar los resultados con fecha
        data = []
        # Itera sobre los resultados y agrega la fecha junto con el total de familias
        for result in results:
            data.append({
                'date': result['day'],
                'total_families': result['total_families'],
            })

        # Retorna los resultados con fecha en la respuesta
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def count_stratum(request):
    try:
        count_stratum_1 = InfoGeneral.objects.filter(estratum=1).count()
        count_stratum_2 = InfoGeneral.objects.filter(estratum=2).count()
        count_stratum_3 = InfoGeneral.objects.filter(estratum=3).count()
        count_stratum_4 = InfoGeneral.objects.filter(estratum=4).count()
        count_stratum_5 = InfoGeneral.objects.filter(estratum=5).count()
        count_stratum_6 = InfoGeneral.objects.filter(estratum=6).count()

        data = [
            {'name': 'Bajo bajo', 'total Bajo bajo': count_stratum_1},
            {'name': 'Bajo', 'total Bajo': count_stratum_2},
            {'name': 'Medio-bajo', 'total Medio bajo': count_stratum_3},
            {'name': 'Medio', 'total Medio': count_stratum_4},
            {'name': 'Medio alto', 'total Medio alto': count_stratum_5},
            {'name': 'Alto', 'total Alto': count_stratum_6},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
