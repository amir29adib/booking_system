from django.urls import path
from booking.views import BookingCreateView, BookingUpdateView, UserBookingListView

urlpatterns = [
    path('', UserBookingListView.as_view(), name='booking_list'),
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
]