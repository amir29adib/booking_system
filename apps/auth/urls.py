from django.urls import path
from auth.views import SignupView, HomeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='auth_signup'),
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='auth_token_refresh'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]