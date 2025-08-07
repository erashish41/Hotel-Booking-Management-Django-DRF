from django.shortcuts import render
from user_auth.models import User
from user_auth.forms import CustomUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'user_auth/sign_up.html'
    success_url = reverse_lazy('signin')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Something went wrong, Please check your form again")
        return super().form_invalid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'user_auth/sign_in.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'manager':
            return reverse_lazy('manager')
        elif user.user_type == 'customer':
            return reverse_lazy('customer')
        return reverse_lazy('login')
    
    
class UserLogoutView(LogoutView):
     next_page = reverse_lazy('signin')   
     
class ManagerDashboardView(TemplateView):
    template_name = 'user_auth/manager.html'


class CustomerDashboardView(TemplateView):
    template_name = 'user_auth/customer.html'