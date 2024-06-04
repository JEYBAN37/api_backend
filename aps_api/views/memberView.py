from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from aps_api.managers.atributesMember import AtributesMember
from aps_api.managers.member import Member
from aps_api.managers.names import Names
from aps_api.managers.family import Family
from aps_api.serializers.memberSerializers import (MemberSerializers, CustomSerializers, CustomUpdateSerializers,
                                                   SaveMemberSerializers,MemberFamiliySerializer)
from rest_framework import status
from aps_api.properties.request import keys_member, mss
from aps_api.utils.querys import get_request, post_request, update_request, delete_request


@api_view(['POST'])
def add_item(request):
    try:
        id_document = request.data['name_person']['id_document']
        if Names.objects.filter(id_document=id_document, member__isnull=False).exists():
            return Response({mss[8]}, status=status.HTTP_409_CONFLICT)
        return post_request(request, Member, MemberSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, Member, CustomSerializers, MemberSerializers, keys_member)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, Member, CustomUpdateSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        attribute_instance = get_object_or_404(AtributesMember, member=pk)
        attribute_instance.delete()
        return delete_request(Member, pk)
    except AtributesMember.DoesNotExist:
        return Response({'error': 'Atributos del miembro no encontrados.'}, status=status.HTTP_404_NOT_FOUND)
    except Member.DoesNotExist:
        return Response({'error': 'Miembro no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def count_sex(request):
    try:
        count_M = Member.objects.filter(sex=1).count()
        count_F = Member.objects.filter(sex=2).count()
        count_I = Member.objects.filter(sex=3).count()

        data = [
            {'name': 'Hombre', 'total': count_M},
            {'name': 'Mujer', 'total': count_F},
            {'name': 'Indeterminado', 'total': count_I},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def count_affiliation_regime(request):
    try:
        count_sub = Member.objects.filter(affiliation_regime=1).count()
        count_con = Member.objects.filter(affiliation_regime=2).count()
        count_esp = Member.objects.filter(affiliation_regime=3).count()
        count_exc = Member.objects.filter(affiliation_regime=4).count()
        count_noa = Member.objects.filter(affiliation_regime=5).count()

        data = [
            {'name': 'Subsidiado', 'total': count_sub},
            {'name': 'Contributivo', 'total': count_con},
            {'name': 'Especial', 'total': count_esp},
            {'name': 'Excepcion', 'total': count_exc},
            {'name': 'No Afiliado', 'total': count_noa},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def count_etnia(request):
    try:
        count_1 = Member.objects.filter(etnia=1).count()
        count_2 = Member.objects.filter(etnia=2).count()
        count_3 = Member.objects.filter(etnia=3).count()
        count_4 = Member.objects.filter(etnia=4).count()
        count_5 = Member.objects.filter(etnia=5).count()
        count_6 = Member.objects.filter(etnia=6).count()
        count_7 = Member.objects.filter(etnia=7).count()

        data = [
            {'name': 'Indígena', 'Indígena': count_1},
            {'name': 'ROM Gitano', 'ROM Gitano': count_2},
            {'name': 'Raizal', 'Raizal': count_3},
            {'name': 'Palenquero de San Basilio', 'Palenquero de San Basilio': count_4},
            {'name': 'Negro, Mulato, Afro', 'Negro, Mulato, Afro': count_5},
            {'name': 'Ninguna de las anteriores', 'Ninguna de las anteriores': count_6},
            {'name': 'Otro', 'Otro': count_7},
        ]

        # Retornar la respuesta con estado HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        # Retornar un error con estado HTTP 500 Internal Server Error
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_member_family_by_id(request, pk):
    try:
        family = Family.objects.get(pk=pk)
        members = Member.objects.filter(family=family)
        serializer = MemberFamiliySerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Family.DoesNotExist:
        return Response({"detail": "Family not found."}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
