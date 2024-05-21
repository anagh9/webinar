from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
]
