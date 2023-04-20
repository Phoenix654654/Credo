from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyObtainPairView, RegisterView

urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterView.as_view(), name='register')
]