"""Nastay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from Nastay import views
import Booking
from Booking import views
import Nastay
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Nastay.views.home),
    path('about',Nastay.views.about),
    path('after',Nastay.views.home),
    path('Book',Booking.views.reservation),
    path('confirmbooking',Booking.views.confirmbooking),
    path('withoutlogin',Nastay.views.withoutlogin),
    path('login' ,Booking.views.login) ,  
    path('logout' ,Booking.views.logout) ,  
    path('signup' ,Booking.views.signup) ,  
    # path('Signuptest' ,Booking.views.Signuptest) ,  
    path('profile',Booking.views.about),
    # path('hotellogin',Booking.views.hotellogin),
    # path('loginadmin',Booking.views.loginadmin),
    path('Check',Booking.views.Check),
    path('Checkavability',Booking.views.Checkavability),
    # path('loginverify',Booking.views.loginverify),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


