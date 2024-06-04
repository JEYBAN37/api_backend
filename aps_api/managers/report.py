from django.db import models

from aps_api.managers.family import Family
from aps_api.properties import enums
from django.core.validators import MinValueValidator, MaxValueValidator


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    type_register = models.CharField(max_length=1, default='1')  # 0
    type_entidad = models.IntegerField(choices=enums.OPTIONS_TRO, null=True, blank=True)  # 1
    id_entidad = models.CharField(max_length=12, null=True, blank=True)  # 2
    date_init = models.DateField(auto_now_add=True)  # 3
    date_final = models.DateField(auto_now_add=True)  # 4
    numbers_family = models.IntegerField(default=0)  # 5
    family = models.OneToOneField(Family, on_delete=models.CASCADE)
# OK


 #Tengo que hacer una consulta que me traiga el numeor de personas integrantes de la familia y la pegue en la variable las personas integrantes de la familia