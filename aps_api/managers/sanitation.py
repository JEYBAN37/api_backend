from django.db import models
from aps_api.managers.livingpPlace import LivingPlace
from aps_api.properties import enums
from aps_api.utils.validationFields import letters_validator
from django.contrib.postgres.fields import ArrayField


class Sanitation(models.Model):
    id = models.AutoField(primary_key=True)
    living_place_id = models.OneToOneField(LivingPlace, on_delete=models.CASCADE)
    water_supply = ArrayField(models.IntegerField(choices=enums.OPTIONS_SS, null=True, blank=True,))  # 75
    other_water_supply = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 76
    disposal_system = ArrayField(models.IntegerField(choices=enums.OPTIONS_DS))  # 77
    other_disposal_system = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 78
    residual_water = ArrayField(models.IntegerField(choices=enums.OPTIONS_W))  # 79
    other_residual_water = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 80
    solid_waste = ArrayField(models.IntegerField(choices=enums.OPTIONS_SW))  # 81
    other_Solid_waste = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 82
    hygiene = models.IntegerField(enums.OPTIONS_YN)
    food_hygiene = models.IntegerField(enums.OPTIONS_YN)
    kitchen_toilet = models.IntegerField(enums.OPTIONS_YN)
    handwashing = models.IntegerField(enums.OPTIONS_YN)
    hygiene_element = models.IntegerField(enums.OPTIONS_YN)
    brushed = models.IntegerField(enums.OPTIONS_B)
# OK
