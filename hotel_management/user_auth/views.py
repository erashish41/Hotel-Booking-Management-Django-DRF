from django.shortcuts import render
from user_auth.models import User
from user_auth.forms import CustomUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'user_auth/sign_up.html'
    # success_url = reverse_lazy('hotel_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Something went wrong, Please check your form again")
        return super().form_invalid(form)