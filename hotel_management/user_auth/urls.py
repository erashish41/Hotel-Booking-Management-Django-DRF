from django.urls import path
from user_auth.views import UserRegisterView, UserLoginView, UserLogoutView, ManagerDashboardView, CustomerDashboardView

urlpatterns = [
    path('signup/',UserRegisterView.as_view(),name='signup'),
    path('signin/',UserLoginView.as_view(),name='signin'),
    path('signout/',UserLogoutView.as_view(),name='signout'),
    
    path('manager/',ManagerDashboardView.as_view(),name='manager'),
    path('customer/',CustomerDashboardView.as_view(),name='customer'),
]