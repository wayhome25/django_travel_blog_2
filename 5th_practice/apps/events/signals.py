from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.events.models import Pizzazip


@receiver(post_save, sender=Pizzazip)
def pizzazip_post_save(sender, instance: Pizzazip, **kwargs):
    # location = kwargs['instance'].location
    location = instance.location
    location.num_pizzazip += 1
    location.save()

