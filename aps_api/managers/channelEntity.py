from django.db import models
from .contact import Contact
from .pollster import Pollster


class ChannelEntity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    campus = models.CharField(max_length=15)  # 17
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    pollster = models.OneToOneField(Pollster, on_delete=models.CASCADE)
# OK
