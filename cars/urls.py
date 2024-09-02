from django.urls import path,include
from.import views
from .views import DetailsCar

urlpatterns = [
path('details/<int:id>/',views.DetailsCar.as_view(),name='details'),
path('buy/<int:id>/', views.buy_car, name='buy_car'), 
]
