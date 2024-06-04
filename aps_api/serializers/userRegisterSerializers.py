from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail
from aps_api.managers.pollster import Pollster



class UserUpdateSerialer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False, 'allow_blank': True},
        }

    def update(self, instance, validated_data):
        new_password = validated_data.get('password', None)
        # Verificar la contraseña antigua antes de actualizar la nueva, si se proporciona una nueva contraseña
        if new_password and not new_password.strip():
            raise ValidationError({'password': 'El campo de la nueva contraseña no puede estar en blanco.'})
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance

class UserRegisterSerializers(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    old_password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'old_password', 'groups','is_active']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False, 'allow_blank': True},
            'old_password': {'write_only': True, 'required': False, 'allow_blank': True}
        }

    def create(self, validated_data):
        grupos = validated_data.pop('groups')
        usuario = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active = False,
        )

        usuario.groups.set(grupos)
        return usuario

    def update(self, instance, validated_data):
        grupos = validated_data.pop('groups', None)
        old_password = validated_data.pop('old_password', None)
        new_password = validated_data.get('password', None)
        active = validated_data.get('is_active')


        # Verificar la contraseña antigua antes de actualizar la nueva, si se proporciona una nueva contraseña
        if new_password and not new_password.strip():
            raise ValidationError({'password': 'El campo de la nueva contraseña no puede estar en blanco.'})

        if new_password:
            if not old_password:
                raise ValidationError({'old_password': 'Se requiere la contraseña antigua para cambiar la contraseña.'})
            if not instance.check_password(old_password):
                raise ValidationError({'old_password': 'La contraseña antigua no es correcta.'})

        instance.username = validated_data.get('username', instance.username)

        # Actualiza la contraseña si se proporciona una nueva y la antigua es correcta
        if new_password:
            instance.set_password(new_password)

        instance.is_active = active
        instance.save()

        try:
            subject = 'Actualización de Estado de Usuario'
            message = f'Hola {instance.username}, tu estado de cuenta ha sido actualizado a {"activo" if active else "inactivo"}.'
            email_from = 'jeyban37@gmail.com'  # Reemplaza con tu correo electrónico configurado
            recipient_list = [instance.account.contact.email]
            print(recipient_list)# Asegúrate de tener el campo email en tu modelo Pollster
            send_mail(subject, message, email_from, recipient_list)
        except Pollster.DoesNotExist:
            pass  # Manejar caso donde no se encuentra un pollster asociado


        # Actualizar los grupos del usuario si se proporcionan
        if grupos is not None:
            instance.groups.set(grupos)

        return instance