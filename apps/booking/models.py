from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User


class Booking(BaseModel):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Confirmed'),
        (3, 'Canceled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')


    class Meta:
        db_table = 'booking'
        