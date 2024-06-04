from django.db import models
from aps_api.managers.pollster import Pollster


class NewFields(models.Model):
    id = models.AutoField(primary_key=True)
    textJustify = models.CharField(max_length=500,blank=True,null=True)
    pollster = models.ForeignKey(Pollster, on_delete=models.CASCADE)
    longitud = models.DecimalField(max_digits=11, decimal_places=8,blank=True, null=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=8,blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True, db_index=True)
