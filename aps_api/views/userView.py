from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from aps_api.managers.pollster import Pollster


from aps_api.serializers.pollsterSerializers import PollsterSerializers
from aps_api.serializers.userRegisterSerializers import UserRegisterSerializers, UserUpdateSerializer
from rest_framework import status
from aps_api.properties.request import mss
from django.middleware.csrf import get_token

from aps_api.signals.method_generator import KeysRamdom
from aps_api.utils.psscript import decrypt_password
from aps_api.utils.querys import post_request, update_request, get_request
import random


@api_view(['POST'])
def register(request):
    try:
        secret_key = '2031c44d3fccc96938b308a8a66dad4b'
        password = request.data['password']
        iv_hex = request.data['iv']
        decrypted_password = decrypt_password(password, secret_key, iv_hex)
        request.data['password'] = decrypted_password
        return post_request(request, User, UserRegisterSerializers)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def out(request):
    try:
        logout(request)
        return Response({mss[7]}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def token_generate(request):
    token = get_token(request)
    return Response({'csrf_token': token}, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_items(request, pk):
    try:
        return update_request(request, User, UserRegisterSerializers, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def view_items(request):
    try:
        return get_request(request, User, UserRegisterSerializers, UserRegisterSerializers, {'id'})
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def recovery_item(request):
    try:
        item = request.data
        request = Pollster.objects.get(name_person__id_document=item['id_document'])
        if request:
            if item['code'] in KeysRamdom:
                serializer_instance = PollsterSerializers(request)
                return Response(serializer_instance.data, status=status.HTTP_200_OK)
            elif item['code'] == "":
                aleatory = random.randint(0, 3)
                subject = 'Actualización de Estado de Usuario'
                message = f'Hola, tu código de recuperación de cuenta <strong>{KeysRamdom[aleatory]}</strong>.'
                email_from = 'jeyban37@gmail.com'
                recipient_list = [item['email']]
                print(recipient_list)
                send_mail(subject, " ", email_from, recipient_list, html_message=message)
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def reset_password(request, pk):
    try:
        secret_key = '2031c44d3fccc96938b308a8a66dad4b'
        password = request.data['password']
        iv_hex = request.data['iv']
        decrypted_password = decrypt_password(password, secret_key, iv_hex)
        request.data['password'] = decrypted_password
        return update_request(request, User, UserUpdateSerializer, pk)
    except Exception as e:
        return Response({mss[1]: str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
