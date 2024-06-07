from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from aps_api.properties import enums
from aps_api.managers.pollster import Pollster
from aps_api.utils.concat import concat_variable,concat_variable_special
from aps_api.utils.counter import asigment_number_ramdom
from aps_api.utils.validationFields import numbers_validator


class InfoGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    type_register = models.IntegerField(default=2)  # 0
    number_register = models.IntegerField(default=1)  # 1
    consent = models.IntegerField(default=1)  # 2
    departament = models.CharField(max_length=2, choices=enums.DEPARTAMENTS)  # 3
    zonal_unit = models.CharField(max_length=7, default='UZPE999')  # 4 Tenemos que revisar nomenclatura de UZOE
    municipality = models.CharField(max_length=5, choices=enums.MUNICIPALITY)  # 5
    territory = models.CharField(max_length=3, default='T99')  # 6
    microterritory = models.CharField(max_length=4, default='T99')  # 7
    name_branding = models.IntegerField(choices = enums.NH,db_index=True)  # 8
    address = models.CharField(max_length=200, null=True, blank=True)  # 9
    longitud = models.DecimalField(max_digits=11, decimal_places=8)  # 10 frontend
    latitud = models.DecimalField(max_digits=10, decimal_places=8)  # 11 frontend
    home_location = models.CharField(max_length=200, null=True, blank=True)  # 12
    id_familia = models.CharField(max_length=32, blank=True)  # 13  18 + F + XXXX frontend
    estratum = models.IntegerField(choices=enums.OPTIONS_STR)  # 14
    households = models.CharField(max_length=1, default="1", validators=[numbers_validator], blank=True)  # 15
    num_families = models.IntegerField(default=0, validators=[numbers_validator], blank=True)  # 16
    people = models.IntegerField(default=1, validators=[numbers_validator], blank=True)  # 17
    basic_team = models.CharField(max_length=27, blank=True)  # 18
    id_primary_provider = models.CharField(max_length=10, choices=enums.OPTIONS_ESE)  # 19
    pollster = models.ForeignKey(Pollster, on_delete=models.CASCADE)  # 20-21
    id_ficha = models.CharField(max_length=27, blank=True)  # 22
    creation_date = models.DateField(auto_now_add=True, db_index=True)  # 23

    # OK

    def save(self, *args, **kwargs):
        if not self.basic_team:
            basic_team = (self.departament,
                          self.zonal_unit,
                          self.municipality,
                          self.territory,
                          self.microterritory,
                          'EBS',
                          )
        if not self.id_ficha:
            id_ficha = (self.id_familia,
                        'CF',
                        )
            self.basic_team = concat_variable(basic_team)
            self.id_ficha = concat_variable(id_ficha)
        if not self.id_familia:

            id_familia = (self.basic_team,
                          'F',
                          asigment_number_ramdom()
                          )
            self.id_familia = concat_variable_special(id_familia)
        super().save(*args, **kwargs)
