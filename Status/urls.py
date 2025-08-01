from django.urls import path
from .views import *


app_name = 'status'
urlpatterns = [
    path('shoptatus/', view_status, name='status')
]