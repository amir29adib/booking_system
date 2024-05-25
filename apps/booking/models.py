from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User


class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

    class Meta:
        db_table = 'booking'
        