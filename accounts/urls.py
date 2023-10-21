from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('login_user/',views.login_user, name = 'valid_member'),
    path('logout_user/',views.logout_user, name = 'logout'),
]
