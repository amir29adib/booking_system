from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User


class Booking(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()