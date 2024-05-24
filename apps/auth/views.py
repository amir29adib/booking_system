from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from auth.serializers import UserSerializer
from django.contrib.auth.models import User


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer