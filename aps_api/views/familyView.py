import datetime
from datetime import date
from django.db.models.functions import TruncDate
from aps_api.serializers.infoGeneralSerializers import FamilyGeneralSerializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from aps_api.managers.family import Family
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.permissions import IsSurveyor, IsAdministrator, IsChannelizer,IsAnalyst
from aps_api.serializers.familySerializers import FamilySerializers, CustomSerializers, CustomUpdateSerializers, FamilyGetSerializers, CustomFamilyMemberSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from aps_api.utils.querys import get_request, post_request, update_request, delete_request
from aps_api.properties.request import mss, keys_family
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from aps_api.serializers.allDataSerializers import FamilyAllSerializers


@api_view(['POST'])
def add_item(request):
    try:
        return post_request(request, Family, FamilySerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsSurveyor,IsAnalyst])
@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, Family, CustomSerializers, FamilyGetSerializers, keys_family)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@permission_classes([IsSurveyor])
@api_view(['GET'])
def view_items_pollster(request, pk):
    try:
        end_date = date.today()
        start_date = end_date - datetime.timedelta(days=7)
        result = (Family.objects.filter(info_general__pollster=pk)
                  .filter(info_general__creation_date__range=[start_date, end_date])
                  .order_by('-info_general__creation_date')
                  )
        serializer = CustomSerializers(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, Family, FamilySerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items_all(request):
    try:
        return get_request(request, Family, CustomSerializers, FamilySerializers, keys_family)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        return delete_request(Family, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FamilyListView(generics.ListAPIView):
    queryset = Family.objects.all()
    serializer_class = CustomSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'info_general__pollster': ['exact'],
        'info_general__creation_date': ['gte', 'lte']
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        end_date = date.today()
        start_date = end_date - datetime.timedelta(days=100)
        return queryset.filter(info_general__creation_date__range=[start_date, end_date]).order_by(
            '-info_general__creation_date')

@api_view(['GET'])
def count_family(request):
    try:
        total_families = Family.objects.count()
        data = [{'name': 'Total Familias', 'total': total_families}]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_family_by_id(request, pk):
    try:
        family = Family.objects.get(pk=pk)
        serializer = FamilyAllSerializers(family)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Family.DoesNotExist:
        return Response({"detail": "Family not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

