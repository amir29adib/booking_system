from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from booking.models import Booking
from booking.serializers import BookingSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Booking'])
class BookingCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, request, serializer):
        user_id = request.user.id

        serializer.save(user=user_id)

@extend_schema(tags=['Booking'])
class BookingUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_update(self, serializer):
        serializer.save()

@extend_schema(tags=['Booking'])
class UserBookingListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    
    def get_queryset(self, request):
        return Booking.objects.filter(user=request.user.id)
