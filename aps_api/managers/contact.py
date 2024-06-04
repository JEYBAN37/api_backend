from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
# OK
