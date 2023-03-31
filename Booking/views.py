from django.shortcuts import render
# Create your views here.
from datetime import datetime
from .models import Hotel,Room,User

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")


def Signuptest(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        location = request.POST.get("location")
        pwd = request.POST.get("pwd")
        temp = User(name=name,email=email,location=location,pwd=pwd)
        temp.save()
        data={
            'msg':"Signup successfully"
        }
    else :
        data={
            'msg' : "Again signup try again"
        }
    return render(request,"login.html",data)

def loginverify(request):
    if (request.method == "POST"):
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        if email != None :
            user=User.objects.get(email=email,pwd=pwd)
            data={
                'name'  : user.name
            }
            return render(request,"index.html",data)
    data={
        'msg' : "Wrong id or password"
    }
    return render(request,"login.html",data)


def hotellogin(request):
    return render(request,"login.html")

def loginadmin(request):
    if (request.method == "POST"):
        hotel=Hotel.objects.all()
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        
        if email != None :
            hotel=Hotel.objects.get(email=email)
            if(hotel.password == pwd):
                data={
                    'hotel' : hotel
                }
                return render(request,"about.html",data)
    data={
        'msg' : "Wrong id or password"
    }
    return render(request,"login.html",data)

def Checkavability(request):
    if (request.method == "POST"):
        Rooms = Room.objects.all()
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('ckeckout')
        print(checkin)
        rooms = Room.objects.filter(checkindate__lt=checkin)
        # rooms = rooms.objects.filter(checkoutdate__lt=checkout)
        # hotel=Hotel.objects.filter(name=rooms.name)
        data={
            'hotel':rooms
        }
    return render(request,"test.html",data)

def Check(request):
    return render(request,"availability.html")
    
def hotellist(request):
    if (request.method == "POST"):
        Rooms = Room.objects.all()
        checkin = request.POST.get("ckeckin")
        checkout = request.POST.get("ckeckout")
        print(checkin)
        print(checkout)
        rooms = Rooms.objects.raw('select * from Rooms where '+ checkin+'>= checkindate and '+checkout+'=< checkoutdate')
        hotel=Hotel.objects.filter(Hotelid=rooms.Hotelid)
    data={
        'hotel' : hotel
    }
    return render(request,"test.html",data)

def about(request):
    return render(request,"about.html")