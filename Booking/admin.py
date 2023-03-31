from django.contrib import admin
from Booking.models import Hotel,Room,User
# Register your models here.
 
class Adminhotel(admin.ModelAdmin):
    list_display =('name','address','phone_number','email','images')

class Adminroom(admin.ModelAdmin):
    list_display =('Roomid','name','checkindate','checkoutdate','email')

class Adminuser(admin.ModelAdmin):
    list_display =('Id','name','location','email','pwd')


admin.site.register(Hotel,Adminhotel)
admin.site.register(Room,Adminroom)
admin.site.register(User,Adminuser)
