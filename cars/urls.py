from django.urls import path
from . import views

app_name ='cars'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('base/', views.base, name = 'base'),
    path('cars/', views.all_cars, name = 'cars'),
    path('search/', views.search_car, name = 'search'),
    path('car_detail/<car_id>', views.car_detail, name = 'car_detail'),
]
