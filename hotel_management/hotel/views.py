from django.shortcuts import render, get_object_or_404, redirect
from hotel.models import Hotel, Room, Review, Destination, Facility
from user_auth.models import User
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from hotel.forms import HotelCreateForm, RoomCreateForm, ReviewCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

# Hotel CRUD
class HotelListView(LoginRequiredMixin,ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    paginate_by = 10

    
    def get_queryset(self):
        hotel = Hotel.objects.all().distinct()
        # hotel = Hotel.objects.order_by('name')
        return hotel
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.user_type == 'manager':
            context['form'] = HotelCreateForm()
        return context

class HotelCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Hotel
    form_class = HotelCreateForm
    template_name = 'hotels/hotel_list.html'
    success_url = reverse_lazy('hotel_list')
    success_message = 'Hotel added Successfully'
    
    def form_valid(self, form):
        if self.request.user.user_type == 'manager':
            return super().form_valid(form)
        else:
            messages.error(self.request,"Only managers can create hotels.")
        return self.form_invalid(form)

    
class HotelDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView, UpdateView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    form_class = HotelCreateForm
    context_object_name = 'hotel'
    success_message = 'Hotel information updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  
        context['rooms'] = self.object.rooms.all()
        context['reviews'] = self.object.reviews.select_related('user') 

        context['review_form'] = ReviewCreateForm()

        return context

    
class HotelDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Hotel
    success_url = reverse_lazy('hotel_list')
    success_message = "Hotel successfully deleted"

# Room CRUD

class RoomListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Room
    context_object_name = 'rooms'
    
    def get_queryset(self):
        room = Room.objects.all().distinct()
        # room = Hotel.objects.order_by('name')
        return room
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.user_type == 'manager':
            context['form'] = RoomCreateForm()
        return context

class RoomCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Room
    form_class = RoomCreateForm
    template_name = 'hotels/hotel_detail.html'
    success_url = reverse_lazy('room_list')
    success_message = 'Room added Successfully'
    context_object_name = 'rooms'
    
    def form_valid(self, form):
        if self.request.user.user_type == 'manager':
            return super().form_valid(form)
        else:
            messages.error(self.request,"Only managers can create rooms.")
        return self.form_invalid(form)

    
class RoomDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView, UpdateView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    form_class = RoomCreateForm
    context_object_name = 'room'
    success_message = 'Hotel information updated successfully!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RoomCreateForm()
        return context
    
    
class RoomDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Room
    success_url = reverse_lazy('hotel_list')
    success_message = "Room successfully deleted"
    
# Review CRUD
    
class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'hotels/hotel_detail.html'
    success_message = 'Review added successfully'
    context_object_name = 'reviews'

    def form_valid(self, form):
        hotel_id = self.request.POST.get('hotel_id')
        hotel = get_object_or_404(Hotel, id=hotel_id)

        review = form.save(commit=False)
        review.user = self.request.user
        review.hotel = hotel
        review.save()

        return redirect('hotel_detail', pk=hotel.id)

    
class ReviewDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView, UpdateView):
    model = Hotel
    template_name = 'hotels/hotel_detail.html'
    form_class = ReviewCreateForm
    context_object_name = 'review'
    success_message = 'Hotel information updated successfully!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewCreateForm()
        return context
    
    
class ReviewDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Review
    success_url = reverse_lazy('hotel_list')
    success_message = "Review successfully deleted"
    
    