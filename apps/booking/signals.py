# from django.core.mail import EmailMessage
# from django.conf import settings
# from asgiref.sync import sync_to_async
# import asyncio

# def booking_created(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         # Use sync_to_async to call the async function from a synchronous context
#         asyncio.run(sync_to_async(send_booking_email)(instance))

# async def send_booking_email(booking_instance):
#     user = booking_instance.user
    
#     subject = 'Booking Confirmation'
#     message = (
#         f'Hello {user.username},\n\n'
#         f'Your booking has been successfully created.\n\n'
#         f'Booking Date: {booking_instance.booking_date}\n'
#         f'Status: {booking_instance.status}'
#     )

#     email = EmailMessage(
#         subject=subject,
#         body=message,
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=[user.email],
#     )

#     # Use sync_to_async to send the email asynchronously
#     await sync_to_async(email.send, thread_sensitive=True)()
