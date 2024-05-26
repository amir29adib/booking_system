from booking.models import Booking
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

class BookingSerializer(serializers.ModelSerializer):
    
    booking_date = serializers.DateField(required=True)
    status = serializers.CharField(required=True, max_length=1)

    class Meta:
        model = Booking
        fields = ('id', 'booking_date', 'status')
    
    def validate(self, attrs):
        booking_date = attrs.get('booking_date')
        status = attrs.get('status')
        current_date = datetime.datetime.strptime(datetime.datetime.now(), "%Y-%m-%d")

        if Booking.objects.filter(booking_date=booking_date).exists():
            raise serializers.ValidationError("A booking for this date already exists!")

        if booking_date < current_date:
            raise serializers.ValidationError("Date is Expired!")

        if status not in (1,2,3):
            raise serializers.ValidationError("Status number is not valid!")


        return attrs
    
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.booking_date = validated_data.get('booking_date', instance.booking_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance