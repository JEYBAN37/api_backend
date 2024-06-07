from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .member import Member
from aps_api.properties import enums
from aps_api.utils.validationFields import numbers_validator
from django.contrib.postgres.fields import ArrayField

from ..properties.enums import OPTIONS_GP, OPTIONS_DISABILITY, OPTIONS_HEALTH_SERVICES, OPTIONS_DTPE_INTERVENTIONS, \
    OPTIONS_BP, OPTIONS_ACCESSIBILITY, OPTIONS_HEALTH_PROVIDERS


class AtributesMember(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE,related_name='member_atributes')
    group_demographic = ArrayField(models.IntegerField(choices=OPTIONS_GP))  # 15
    disability = ArrayField(models.IntegerField(choices=OPTIONS_DISABILITY))  # 18
    chronic_condition = models.IntegerField(choices=enums.OPTIONS_YN)  # 19
    care_scheme = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 20
    pending_interventions = ArrayField(models.IntegerField(choices=OPTIONS_HEALTH_SERVICES), null=True, blank=True)  # 21
    health_promotion = ArrayField(models.IntegerField(choices=OPTIONS_DTPE_INTERVENTIONS), null=True, blank=True)  # 22
    sport = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 23
    breastfeeding = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 24
    breastfeeding_months = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(24), numbers_validator], null=True, blank=True)  # 25
    under_five_years = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 26
    weight_for_height = models.IntegerField(choices=enums.OPTIONS_ZW, null=True, blank=True)  # 29
    brachial_perimeter = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)], null=True,
                                             blank=True)  # 30
    physical_signs_of_malnutrition = ArrayField(models.IntegerField(choices=OPTIONS_BP), null=True, blank=True)  # 31
    presented_disease = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 32
    disease_description = models.CharField(max_length=200, null=True, blank=True)  # 33
    acute_disease_treatment = models.IntegerField(choices=enums.OPTIONS_YN, null=True, blank=True)  # 34
    reason_for_no_attention = ArrayField(models.IntegerField(choices=OPTIONS_ACCESSIBILITY), null=True, blank=True)  # 35
    medical_care = ArrayField(models.IntegerField(choices=OPTIONS_HEALTH_PROVIDERS))  # 36
    canalization = ArrayField(models.IntegerField(choices=enums.CANALIZATIONS))
    # OK
