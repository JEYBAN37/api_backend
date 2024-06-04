from django.db import models
from aps_api.properties import enums
from .family import Family
from aps_api.utils.validationFields import letters_validator
from django.contrib.postgres.fields import ArrayField


class FamilyContext(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)
    younger = models.IntegerField(choices=enums.OPTIONS_YN)  # 31
    pregnant = models.IntegerField(choices=enums.OPTIONS_YN)  # 22
    senior = models.IntegerField(choices=enums.OPTIONS_YN)  # 33
    victim = models.IntegerField(choices=enums.OPTIONS_YN)  # 34
    disable = models.IntegerField(choices=enums.OPTIONS_YN)  # 35
    patient = models.IntegerField(choices=enums.OPTIONS_YN)  # 36
    infected_person = models.IntegerField(choices=enums.OPTIONS_PI, null=True, blank=True)  # 37
    event_noted = models.IntegerField(choices=enums.OPTIONS_YN)  # 38
    vulneravility = models.IntegerField(choices=enums.OPTIONS_YN)  # 39
    risk_psychosocial = models.IntegerField(choices=enums.OPTIONS_YN)  # 40
    antecedent_salud = models.IntegerField(choices=enums.OPTIONS_YN)  # 41
    antecedent = models.CharField(max_length=30, null=True, blank=True, validators=[letters_validator])  # 42
    source_food = ArrayField(models.IntegerField(choices=enums.OPTIONS_SF))  # 43
    descripcion_source = models.CharField(max_length=100, null=True, blank=True, validators=[letters_validator])  # 44
    healthy_habits = models.IntegerField(choices=enums.OPTIONS_YN)  # 45
    socioemotional = models.IntegerField(choices=enums.OPTIONS_YN)  # 46
    environment_care = models.IntegerField(choices=enums.OPTIONS_YN)  # 47
    healthy_relationships = models.IntegerField(choices=enums.OPTIONS_YN)  # 48
    health_support = models.IntegerField(choices=enums.OPTIONS_YN)  # 49
    senior_protection = models.IntegerField(choices=enums.OPTIONS_YN)  # 50
    family_welfare = models.IntegerField(choices=enums.OPTIONS_YN)  # 51
    scl_conservation = models.IntegerField(choices=enums.OPTIONS_YN)  # 52
    recognition_rights = models.IntegerField(choices=enums.OPTIONS_YN)  # 53
# OK
