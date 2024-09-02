from django.core.mail import send_mail
from celery import shared_task
from .models import Contact


@shared_task
def send_contact_email(
        contact_id: int
    ) -> None:
    contact: Contact = Contact.objects.get(id=contact_id)
    print ("Sending contact")

    subject_user = f'Заявка {contact.pk} создана'
    subject_admin = f'Новая заявка {contact.pk}'
    message_user = (f'Здравствуйте! Ваша заявка была успешно создана.\n\nСведения:\nИмя: {contact.name}\nEmail: {contact.email}'
                    f'\nСообщение: {contact.message}')
    message_admin = (f'Новая заявка создана:\n\nСведения:\nИмя: {contact.name}\nEmail: {contact.email}'
                    f'\nСообщение: {contact.message}')
    from_email = "sbcgl@gmail.com"
    recipient_user = f"{contact.email}"
    recipient_admin = "admin@sbcgl.com"

    send_mail(
        subject_user,
        message_user,
        from_email,
        [recipient_user],
        fail_silently=False,
    )

    send_mail(
        subject_admin,
        message_admin,
        from_email,
        [recipient_admin],
        fail_silently=False,
    )
