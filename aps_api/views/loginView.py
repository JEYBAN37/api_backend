from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from aps_api.serializers.loginSerializers import LoginSerializers
from rest_framework import status
from aps_api.properties.request import mss
from aps_api.utils.psscript import decrypt_password


class LoginView(APIView):
    def post(self, request):
        secret_key = '2031c44d3fccc96938b308a8a66dad4b'

        serializer = LoginSerializers(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            iv_hex = serializer.validated_data['iv']
            decrypted_password = decrypt_password(password, secret_key, iv_hex)
            user = authenticate(request=request._request, username=username, password=decrypted_password)

            # Verifica si el usuario no es None y si la propiedad 'true' existe y es verdadera
            if user is not None:
                login(request, user)
                pollster = user.account
                groups = user.groups.all()
                pollster_data = {'id': pollster.id, 'name': pollster.name_person.name}
                groups_data = [{'name': group.name, 'id': group.id} for group in groups]

                return Response({"pollster": {"pollster": pollster_data, "grupo": groups_data}},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
