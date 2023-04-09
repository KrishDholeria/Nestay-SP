from django.contrib import admin
from Booking.models import Hotel,Room,Reservation
# Register your models here.
 
class Adminhotel(admin.ModelAdmin):
    list_display =('name','address','phone_number','email','images','images1','images2','images3','cost')

class Adminroom(admin.ModelAdmin):
    list_display =('Roomid','name','checkindate','checkoutdate','email')

# class Adminuser(admin.ModelAdmin):
#     list_display =('Id','name','location','email','pwd')

class Adminreservation(admin.ModelAdmin):
    list_display =('name','address','phone_number','email','hotelemail','checkindate','checkoutdate','persons','note')
    

admin.site.register(Hotel,Adminhotel)
admin.site.register(Room,Adminroom)
# admin.site.register(User,Adminuser)
admin.site.register(Reservation,Adminreservation)
