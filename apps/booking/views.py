from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from booking.models import Booking
from booking.serializers import BookingSerializer


class BookingCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, request, serializer):
        user_id = request.user.id

        serializer.save(user=user_id)

class UserBookingListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    
    def get_queryset(self, request):
        return Booking.objects.filter(user=request.user.id)
