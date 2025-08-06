from django.urls import path
from user_auth.views import UserRegisterView

urlpatterns = [
    path('signup/',UserRegisterView.as_view(),name='signup')
]