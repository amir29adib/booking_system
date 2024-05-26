from django.urls import path
from auth.views import SignupView, HomeView, LogoutView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='auth_signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', CustomTokenRefreshView.as_view(), name='auth_token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]