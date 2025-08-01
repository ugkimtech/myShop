from django.urls import path
from .views import *


app_name = 'users'
urlpatterns = [
    path('', login, name='login'),
    path('createUser/', create_user, name='createUser'),
    path('getUsers/', get_users, name='getUsers'),
    path('home/', dashboard, name='home'),
    path('addItem/', add_item, name='addItem'),
    path('addStock/', add_stock, name='addStock'),
    path('addSale/', add_sale, name='addSale'),
    path('expenditure/', expenditure, name='expenditure'),
    path('shopStatus/', view_status, name='shopStatus'),
    path('st/', init_status, name='st'),
]