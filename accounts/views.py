from django.shortcuts import render,redirect
from .import forms
from .forms import RegisterForm,ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cars.models import Car
from django.contrib.auth.models import User
from orders.models import Order
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# Create your views here.

class UserResgisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created Successfully. Please Login.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Something is wrong, Please try again.')
        return super().form_invalid(form)    

class UserLogin(LoginView):
     template_name='register.html'
     def  get_success_url(self):
          return reverse_lazy('profile')
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
     def form_valid(self, form):
         messages.success(self.request,"Logged in successfully")
         return super().form_valid(form)
     def form_invalid(self, form):
          messages.success(self.request,"Logged in information incorrect")
          return super().form_invalid(form)

@login_required
def profile(request):
    data = Car.objects.filter(order__user=request.user).distinct()
    return render(request, 'profile.html', {'data': data})
# @login_required
# def edit_profile(request):
#         if request.method =='POST':                   #user post request kortese
#                 profile_form=forms.ChangeUserForm(request.POST,instance=request.user)        #user er post request er data akhana capture kora hosse
#                 if profile_form.is_valid():                          #post kora data gulan valid ki na amra check kortesi
#                     profile_form.save() 
#                     messages.success(request,"Profile updated successfully")                      #jodi valid hoy taile database a save korbe
#                     return redirect('profile')             #sob thik thakle taka add_author url a pathaye dibo
#         else:           #user normally website a gele blank data pabe 
#             profile_form=forms.ChangeUserForm(instance=request.user)
#             return render(request, 'update_profile.html',{'form':profile_form})

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')
    form_class = ChangeUserForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile update successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Something is wrong, Please try again.')
        return super().form_invalid(form)       
def pass_change(request):
    if request.method =='POST':
         pass_form=PasswordChangeForm(request.user,request.POST)
         if pass_form.is_valid():
            pass_form.save()
            messages.success(request,"Password changed successfully")
            update_session_auth_hash(request,pass_form.user)
            return redirect('profile')
    else:
         pass_form=PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':pass_form})
def user_logout(request):
     logout(request)
     messages.success(request,"Logged out successfully")
     return redirect('user_login')
