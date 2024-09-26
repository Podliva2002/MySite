from django.core.mail import send_mail
from celery import shared_task
from .models import Contact
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_contact_email(
        contact_id: int
) -> None:
    try:
        contact: Contact = Contact.objects.get(id=contact_id)
        print("Sending contact", contact)

        subject_user = f'Заявка {contact.pk} создана'
        subject_admin = f'Новая заявка {contact.pk}'
        message_user = (
            f'Здравствуйте! Ваша заявка была успешно создана.\n\nСведения:\nИмя: {contact.name}\nEmail: {contact.email}'
            f'\nСообщение: {contact.message}')
        message_admin = (f'Новая заявка создана:\n\nСведения:\nИмя: {contact.name}\nEmail: {contact.email}'
                         f'\nСообщение: {contact.message}')
        from_email = "Pod.liv.a@yandex.ru"
        recipient_user = f"{contact.email}"
        recipient_admin = "i.agafonov@reglab.ru"

        send_mail(
            subject_user,
            message_user,
            "Pod.liv.a@yandex.ru",
            [recipient_user],
            fail_silently=False,
        )

        send_mail(
            subject_admin,
            message_admin,
            "Pod.liv.a@yandex.ru",
            [recipient_admin],
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f"Error sending email: {e}")
