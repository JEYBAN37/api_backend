from django.contrib.postgres.fields import ArrayField
from django.db import models
from aps_api.managers.infoGeneral import InfoGeneral
from django.core.validators import MinValueValidator, MaxValueValidator
from aps_api.properties import enums
from aps_api.utils.validationFields import letters_validator, numbers_validator


class LivingPlace(models.Model):
    id = models.AutoField(primary_key=True)
    info_general = models.OneToOneField(InfoGeneral, on_delete=models.CASCADE,related_name='living_place')
    type_living_place = models.IntegerField(enums.OPTIONS_HT)  # 54
    description = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 55
    wall_material = models.IntegerField(enums.OPTIONS_SM)  # 56
    other_wall_material = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 57
    floor_material = models.IntegerField(enums.OPTIONS_FM)  # 58
    other_floor_material = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 59
    roof_material = models.IntegerField(enums.OPTIONS_RM)  # 60
    other_roof_material = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 61
    bedrooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50), numbers_validator])  # 62
    over_population = models.IntegerField(enums.OPTIONS_YN)  # 63
    irrigation_scenarios = ArrayField(models.IntegerField(choices=enums.OPTIONS_SI, null=True, blank=True))  # 64
    access_to_home = ArrayField(models.IntegerField(choices=enums.OPTIONS_AC, null=True, blank=True))  # 65
    food_source = ArrayField(models.IntegerField(choices=enums.OPTIONS_FS, null=True, blank=True))  # 66
    other_food_source = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 67
    transmitting_vectors = models.IntegerField(choices=enums.OPTIONS_YN)  # 68
    vectors_description = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 69
    places_around = ArrayField(models.IntegerField(choices=enums.OPTIONS_OE, null=True, blank=True))  # 70
    other_places_around = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 71
    economic_activity = models.IntegerField(enums.OPTIONS_YN)  # 72
    animals = ArrayField(models.IntegerField(choices=enums.OPTIONS_A, null=True, blank=True))  # 73
    other_animals = models.CharField(max_length=30, null=True, blank=True)  # 74
# OK
