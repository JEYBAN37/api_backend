from django.db import models
from aps_api.properties import enums
from .family import Family


class Welfare(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)
    tenure = models.IntegerField(choices=enums.OPTIONS_T)
    time_residence = models.CharField(max_length=250)
    permanence = models.IntegerField(choices=enums.OPTIONS_TR)
    lgtbi = models.IntegerField(choices=enums.OPTIONS_YN)
    life_style = models.IntegerField(choices=enums.OPTIONS_LS)
    alternative_health = models.IntegerField(choices=enums.OPTIONS_YN)
# OK
