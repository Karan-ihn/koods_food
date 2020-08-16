from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('products/<int:myid>',views.products, name='products'),
    path('checkout/',views.checkout,name='checkout')
]