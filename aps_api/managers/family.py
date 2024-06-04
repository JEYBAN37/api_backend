from django.db import models
from aps_api.managers.infoGeneral import InfoGeneral
from aps_api.properties import enums
from aps_api.utils.counter import increment_variable
from aps_api.utils.concat import concat_variable


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    info_general = models.ForeignKey(InfoGeneral, on_delete=models.CASCADE, db_index=True,related_name='family')
    family_type = models.IntegerField(choices=enums.OPTIONS_FT)  # 24
    total_members = models.PositiveIntegerField(default=0)  # 25
    imagen = models.ImageField(upload_to='famlygraphs/', blank=True, null=True)
    family_graphic = models.IntegerField(choices=enums.OPTIONS_FG)  # 26
    apgar = models.IntegerField(choices=enums.OPTIONS_APGAR)  # 27
    carer = models.IntegerField(choices=enums.OPTIONS_YN)  # 28
    zarit = models.IntegerField(choices=enums.OPTIONS_ZT, null=True)  # 29
    ecomapa = models.IntegerField(choices=enums.OPTIONS_ECO)  # 30
    observation = models.CharField(max_length=500, blank=True, null=True)
    number_family = models.CharField(max_length=60, blank=True, null=True)  # 83 Revisar Nomenclatura dicha por el Cliente

    # OK
    def save(self, *args, **kwargs):
        if not self.pk:
            increment_variable(self.info_general, 'num_families')
        if not self.number_family:
            field_value_13 = self.info_general.id_familia
            field_value_18 = self.info_general.basic_team
            field_value_20 = self.info_general.pollster.name_person.id
            union_field = f"{field_value_13}{field_value_18}{field_value_20}"
            self.number_family = union_field
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if not self.info_general.family.exclude(id=self.id).exists():
            self.info_general.delete()
        super().delete(*args, **kwargs)
