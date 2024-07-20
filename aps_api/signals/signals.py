from django.db.models.signals import post_save
from django.dispatch import receiver
from aps_api.managers.member import Member
from aps_api.managers.report import Report
from django.db import transaction


@receiver(post_save, sender=Member)
def generar_reporte(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            familia = instance.family
            reporte, _ = Report.objects.get_or_create(family=familia)
            reporte.numbers_family = familia.num_member
            reporte.type_entidad = 1
            reporte.id_entidad = '154'
            reporte.save()
