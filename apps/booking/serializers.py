from booking.models import Booking
from rest_framework import serializers
from django.models.auth import User

class BookingSerializer(serializers.ModelSerializer):
    
    booking_date = serializers.DateTimeField(required=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Booking
        fields = ('id', 'booking_date', 'user')

    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("User must be selected.")
        return value
    
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.booking_date = validated_data.get('booking_date', instance.booking_date)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance