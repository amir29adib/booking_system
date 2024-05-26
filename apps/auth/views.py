from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from auth.serializers import UserSerializer
from booking.models import Booking
from booking.serializers import BookingSerializer


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        user_id = request.user.id

        try:
            user_info = User.objects.get(id=user_id)
            serializer_user = UserSerializer(user_info)
            
            booking_info = Booking.objects.filter(user=user_id)
            serializer_booking = BookingSerializer(booking_info)

            response_data = {
                'data' : {
                    'user' : serializer_user.data,
                    'booking' : serializer_booking.data,
                },
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def permission_denied(self, request, message=None, code=None):
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="Please login to see your info and booking status!")
        return super().permission_denied(request, message, code)
    

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"message": "You're logged out!"})