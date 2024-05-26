from booking.models import Booking
from rest_framework import serializers
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):
    
    booking_date = serializers.DateField(required=True)
    # status = serializers.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')])

    class Meta:
        model = Booking
        fields = ('id', 'booking_date', 'user', 'status')
    
    def validate(self, attrs):
        booking_date = attrs.get('booking_date')

        if Booking.objects.filter(booking_date=booking_date).exists():
            raise serializers.ValidationError("A booking for this date already exists.")

        return attrs
    
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.booking_date = validated_data.get('booking_date', instance.booking_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance