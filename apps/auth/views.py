from rest_framework import generics, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from auth.serializers import UserSerializer


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        user_id = request.user.id

        try:
            user_info = User.objects.get(id=user_id)
            serializer = UserSerializer(user_info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def permission_denied(self, request, message=None, code=None):
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="Please login to see your info and booking status!")
        return super().permission_denied(request, message, code)
    

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer