from django.db import models
from .channelEntity import ChannelEntity
from .member import Member
from aps_api.properties import enums


class Pipelines(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(ChannelEntity, on_delete=models.CASCADE)
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    channel = models.CharField(max_length=150)
    state = models.IntegerField(choices=enums.OPTIONS_SW)
#  OK
