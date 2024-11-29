from django.db.models.signals import post_save
from django.dispatch import receiver

from site_app.models import Contact
from site_app.tasks import send_contact_email


@receiver(post_save, sender=Contact)
def send_contact_notification(instance: Contact, created: bool, **kwargs):
    if not created:
        print("Just updated contact:", instance)
    result = send_contact_email.delay(contact_id=instance.pk)
    print(f"Task sent: {result}")

