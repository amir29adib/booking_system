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

    def perform_create(self, serializer):
        status = serializer.validated_data.get('status')
        booking_date = serializer.validated_data.get('booking_date')
        user_id = self.request.user.id

        serializer.save(user_id=user_id, booking_date=booking_date, status=status)


@extend_schema(tags=['Booking'])
class BookingUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ['patch']

    def perform_update(self, serializer):
        status = serializer.validated_data.get('status')
        booking_date = serializer.validated_data.get('booking_date')
        
        serializer.save(booking_date=booking_date, status=status)


@extend_schema(tags=['Booking'])
class BookingDeleteView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Booking'])
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)

    http_method_names = ['get']


@extend_schema(tags=['Booking'])
class UserBookingListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user.id)
