from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from aps_api.properties import enums
from .contact import Contact
from .names import Names
from .family import Family
from aps_api.utils.counter import increment_variable, asignament_number_model
from aps_api.utils.concat import concat_variable


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='in_charge')
    present_person = models.IntegerField(choices=enums.OPTIONS_YN, db_index=True)
    type_register = models.IntegerField(default=2)  # 0
    consent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True)  # 1
    name_person = models.OneToOneField(Names, on_delete=models.CASCADE, db_index=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, db_index=True)
    type_id = models.CharField(max_length=15, choices=enums.TYPE_ID)  # 6
    date_birth = models.DateField(db_index=True)  # 8
    sex = models.IntegerField(choices=enums.SEX)  # 9
    role = models.IntegerField(choices=enums.ROLE)  # 10
    weight = models.CharField(max_length=5, null=True, blank=True)  # 27
    size = models.CharField(max_length=5, null=True, blank=True)  # 28
    level_education = models.IntegerField(choices=enums.OPTIONS_LE)  # 12
    affiliation_regime = models.IntegerField(choices=enums.OPTIONS_AR)  # 13
    eps = models.CharField(choices=enums.EPS,max_length = 80)  # 14
    etnia = models.IntegerField(choices=enums.OPTIONS_E)  # 16
    indigena = models.IntegerField(choices=enums.COMUNIDADES, null=True, blank=True)  # 17
    last_update = models.DateField(auto_now=True)
    family_code = models.CharField(max_length=60, blank=True)  # 37
    # OK

    def save(self, *args, **kwargs):
        if not self.pk:
            increment_variable(self.family, 'total_members')
            self.consent = asignament_number_model(Member, 'family', self.family)
        if not self.family_code:
            family_code = (self.family.number_family
                           )
            self.family_code = concat_variable(family_code)
        super().save(*args, **kwargs)
