from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking


@receiver(post_save, sender=Booking)
def booking_created(sender, instance, created, **kwargs):
    if created:
        send_booking_email(instance)


def send_booking_email(booking_instance):
    user = booking_instance.user
    
    subject = 'Booking Confirmation'
    message = (
        f'Hello {user.username},\n\n'
        f'Your booking has been successfully created.\n\n'
        f'Booking Date: {booking_instance.booking_date}\n'
        f'Status: {booking_instance.status}'
    )

    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email.send()