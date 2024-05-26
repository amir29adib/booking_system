from django.urls import path
from booking.views import BookingCreateView, BookingUpdateView, UserBookingListView, BookingDetailView, BookingDeleteView

urlpatterns = [
    path('', UserBookingListView.as_view(), name='booking_list'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),
]