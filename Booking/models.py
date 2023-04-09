from django.db import models

# Create your models here.

class Hotel(models.Model):
   email = models.EmailField(primary_key=True)
   name = models.CharField(max_length=100,null=True)
   address = models.CharField(max_length=200,null=True)
   phone_number = models.CharField(max_length=20,null=True)
   images =  models.FileField(upload_to="Hotels",default="")
   images1 =  models.FileField(upload_to="Hotels",default="")
   images2 =  models.FileField(upload_to="Hotels",default="")
   images3 =  models.FileField(upload_to="Hotels",default="")
   cost = models.IntegerField(null=True)
   password = models.CharField(max_length=10,null=True)
   
class Room(models.Model):
   Roomid = models.AutoField
   name = models.CharField(max_length=100,null=True)
   checkindate = models.DateField(null=False)
   checkoutdate = models.DateField(null=False)
   email= models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True)
   
# class User(models.Model):
#    Id = models.AutoField
#    name = models.CharField(max_length=100,null=True)
#    location = models.CharField(null=False,max_length=20)
#    email = models.CharField(null=False,max_length=20)
#    pwd = models.CharField(null=False,max_length=20,default="non")
   
class Reservation(models.Model):
   email = models.EmailField(primary_key=True)
   hotelemail=models.EmailField(null=True)
   name = models.CharField(max_length=100,null=True)
   address = models.CharField(max_length=200,null=True)
   phone_number = models.CharField(max_length=20,null=True)
   checkindate = models.DateField(null=False)
   checkoutdate = models.DateField(null=False)
   persons = models.IntegerField(null=False)
   note = models.CharField(max_length=100,null=True)
   

def __str__(self):
    return self.name 
