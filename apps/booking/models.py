from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User


class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending')


    class Meta:
        db_table = 'booking'
        