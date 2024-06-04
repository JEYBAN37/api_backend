from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from aps_api.properties.request import mss


def filter_exists(model, filtro):
    with transaction.atomic():
        return model.objects.filter(id=filtro).exists()


def build_filters(request, filter_mapping):
    filters = {}
    for key, value in filter_mapping.items():
        param_value = request.query_params.get(key)
        if param_value is not None:
            filters[value] = param_value
    return filters


def get_request(request, model, serializer, serializer_especial, filter_mapping):
    filters = build_filters(request, filter_mapping)
    queryset = model.objects.filter(**filters) if filters else model.objects.all()

    serializer_class = serializer_especial if 'id' in filters else serializer
    serializer_instance = serializer_class(queryset, many=True)

    return Response(serializer_instance.data, status=status.HTTP_200_OK) if queryset.exists() else Response({mss[0]},
                                                                                                            status=status.HTTP_404_NOT_FOUND)


def post_request(request, model, serializer_class):
    try:
        if filter_exists(model, request.data.get('id')):
            return Response('Ya Existe', status=status.HTTP_409_CONFLICT)

        data = request.data
        pack_data = handle_serializer(serializer_class, data=data)
        return Response(pack_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_400_BAD_REQUEST)


def update_request(request, model, serializer_class, pk):
    try:
        item = model.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({mss[3]}, status=status.HTTP_404_NOT_FOUND)

    try:
        data = request.data
        pack_data = handle_serializer(serializer_class, instance=item, data=data, partial=True)
        return Response(pack_data, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_400_BAD_REQUEST)


def delete_request(model, pk):
    item = get_object_or_404(model, id=pk)
    item.delete()
    return Response({mss[4]}, status=status.HTTP_202_ACCEPTED)


def handle_serializer(serializer, instance=None, data=None, partial=False):
    if instance:
        pack = serializer(instance=instance, data=data, partial=partial)

    else:
        pack = serializer(data=data)

    pack.is_valid(raise_exception=True)
    print(data)
    pack.save()
    return pack.data


def get_request_pollster(request, model, serializer, serializer_especial, filter_mapping):
    filters = build_filters(request, filter_mapping)
    queryset = model.objects.filter(**filters) if filters else model.objects.all()

    serializer_class = serializer_especial if 'id' in filters else serializer
    serializer_instance = serializer_class(queryset, many=True)

    return Response(serializer_instance.data, status=status.HTTP_200_OK) if queryset.exists() else Response({mss[0]},
                                                                                                            status=status.HTTP_404_NOT_FOUND)


def delete_request_member(model, pk):
    item = get_object_or_404(model, member=pk)
    item.delete()
    return Response({mss[4]}, status=status.HTTP_202_ACCEPTED)
