from django.shortcuts import redirect, render
# Create your views here.
from datetime import datetime
from .models import Hotel,Room,Reservation
from django.contrib.auth.models import auth, User

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            data={
                'msg' : "Invalid input"
            }
            return render(request,"login.html", data)
    else:
        return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = User.objects.create_user(username=username, password=pwd, email=email, first_name=name)
        user.save()
        return redirect('/')
    else:
        return render(request,"signup.html")


def Checkavability(request):
    if (request.method == "POST"):
        Rooms = Room.objects.all()
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        place = request.POST.get('place')
        name=request.POST.get('name')
        print(checkin)
        print(checkout)
        rooms = Room.objects.filter(checkindate__lt=checkin,checkoutdate__gt=checkout)
        hotel=[]
        # if name==None:
        #     msg="First Login"
        #     data={
        #         'msg' : msg
        #     }
        #     return redirect("/login",data)
        if rooms != None:
            
            for room in rooms:
                hotel.append(Hotel.objects.filter(email=room.email.email,address__icontains=place))
                print(hotel)
            data={
                'hotel': hotel
            }
            return render(request,"hotellist.html",data)
        data={
            'hotel' : hotel
        }
    msg =  "Room not avilable"
    data={
        'msg' :msg
    }
    return render(request,"index.html",data)

def Check(request):
    return render(request,"availability.html")
    
def reservation(request):
    if (request.method == "POST"):
        email = request.POST.get("hotelemail")
        hotel=Hotel.objects.get(email=email)
        data={
            'hotel' : hotel
        }
    return render(request,"reservation.html",data)


def confirmbooking(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        hotelemail = request.POST.get("hotelemail")
        print(hotelemail)
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        checkin_date = request.POST.get("checkin_date")
        checkout_date = request.POST.get("checkout_date")
        adults = request.POST.get("adults")
        adult = int (adults)
        children = request.POST.get("children")
        childrens = int (children)
        message = request.POST.get("message")
        person= adult+childrens
        hotel=Hotel.objects.get(email=hotelemail)
        totalcost= int(hotel.cost) * int(adults)
        temp = Reservation(name=name,email=email,hotelemail=hotelemail,address=address,phone_number=phone,checkindate=checkin_date,checkoutdate=checkout_date,persons=person,note=message)
        temp.save()
        data={
            'name': name,
            'hotelname': hotel.name,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'cost' : hotel.cost ,
            'total' : totalcost,
            'totalperson' : person
        }
    return render(request,"bill.html",data)

def about(request):
    return render(request,"about.html")

def logout(request):
    auth.logout(request)
    return redirect("/")