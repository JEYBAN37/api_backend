from django.db import transaction
import random

numeros_generados = set()


numeros_disponibles = set(range(10000))


def increment_variable(model, campo):
    with transaction.atomic():
        setattr(model, campo, getattr(model, campo) + 1)
        model.save(update_fields=[campo])


def asignament_number_model(model, variable, filtrador):
    with transaction.atomic():
        members = model.objects.filter(**{variable: filtrador}).count()
        num_member = members + 1
        return num_member


def asigment_number_ramdom():
    while True:
        numero = random.randint(0, 9999)
        numero_str = "{:04d}".format(numero)
        if numero_str not in numeros_generados:
            numeros_generados.add(numero_str)
            return numero_str
