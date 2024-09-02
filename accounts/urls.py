from django.urls import path,include
from.import views
urlpatterns = [
path('register/',views.UserResgisterView.as_view(),name='register'),
path('login/',views.UserLogin.as_view(),name='user_login'),
path('logout/',views.user_logout,name='user_logout'),
path('profile/',views.profile,name='profile'),
path('profile/edit/<int:pk>',views.EditProfileView.as_view(),name='edit_profile'),
path('profile/edit/pass_change/',views.pass_change,name='pass_change'),

 
]