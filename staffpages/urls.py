from django.urls import path
from . import views

app_name ='staffpages'

urlpatterns = [
    path('cars/', views.all_cars, name = 'cars'),
    path('add/', views.add_cars, name = 'add_cars'),
    path('update/<car_id>', views.update_cars, name = 'update'),
    path('delete_car/<car_id>', views.delete_car, name='delete_car'),
    path('home/', views.home, name='home'),
    path('messages/', views.messages, name = 'messages'),
    path('view_message/<message_id>', views.view_message, name = 'view_message'),
    path('delete_message/<message_id>', views.delete_message, name='delete_message'),
    path('search/', views.search, name = 'search_admin'),
    path('detail/<car_id>', views.detail_admin, name = 'detail_admin'),
]
