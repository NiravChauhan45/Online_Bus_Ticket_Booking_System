from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Contact
from django.contrib.auth.decorators import login_required
from .models import User, Bus, Book, Payment,book_des,pack,clients,aboutt
from datetime import datetime
from django.contrib import messages
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
import razorpay


def index(request):
    book_desData = book_des.objects.all()
    packData = pack.objects.all()
    clientsData = clients.objects.all()
   
   
    data ={
        'book_desData': book_desData,
        'packData': packData,
        'clientsData': clientsData,
        'title':'Yatra',
    }

    # for submit our issues
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        print(name, email, subject, message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        if contact:
            messages.success(
                request, "Congratulations For - successfully submitted the message."
            )
            return redirect("index")
    return render(request, "index.html",data)


def home(request):
    return render(request, "home.html")


def findbus(request):
    return render(request, "bus/findbus.html")


def about(request):
    abouttData=aboutt.objects.all()
    data={'abouttData':abouttData}
    return render(request, "about.html",data)


def blog(request):
    return render(request, "blog.html")


@login_required(login_url="login")
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        print(name, email, subject, message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        if contact:
            messages.success(
                request, "Congratulations - Your issue successfully submitted"
            )
            return redirect("contact")
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def footer(request):
    return render(request, "footer.html")


def header(request):
    return render(request, "header.html")


def book(request):
    return render(request, "book.html")


def offers(request):
    return render(request, "offers.html")


def single_listing(request):
    return render(request, "single_listing.html")


# Authenticate Models(Login and Registers)
def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # check for errorneous input
        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers"
            )
            return redirect("home")

        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect("home")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect("home")

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpass = request.POST["loginpass"]

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("home")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


def ChangePass(request):
    if request.method == "POST":
        username = request.POST["username"]
        p1 = request.POST["p1"]
        p2 = request.POST["p2"]

        if p1 != p2:
            context = {
                "message": "Password does not match, Please try again!!",
                "class": "danger",
            }
            return render(request, "ChangePass.html", context)

        if User.objects.filter(username=username).exists():
            u = User.objects.get(username=username)
        else:
            context = {
                "message": "Invalid username, Please try again!!",
                "class": "danger",
            }
            return render(request, "ChangePass.html", context)
        # u = User.objects.get(username=username)
        u.set_password(p1)
        u.save()
        messages.success(request, "Your password successfully changed")
        return redirect("home")
    return render(request, "ChangePass.html")


@login_required(login_url="login")
def findbus(request):
    context = {}
    if request.method == "POST":
        source_r = request.POST.get("source")
        dest_r = request.POST.get("destination")
        date_r = request.POST.get("date")
        date_r = datetime.strptime(date_r, "%Y-%m-%d").date()
        year = date_r.strftime("%Y")
        month = date_r.strftime("%m")
        day = date_r.strftime("%d")
        bus_list = Bus.objects.filter(
            source=source_r,
            dest=dest_r,
            date__year=year,
            date__month=month,
            date__day=day,
        )
        if bus_list:
            return render(request, "myapp/list.html", locals())
        else:
            context["data"] = request.POST
            context["error"] = "No available Bus Schedule for entered Route and Date"
            return render(request, "findbus.html", context)
    else:
        return render(request, "findbus.html")


@login_required(login_url="login")
def bookings(request):
    context = {}
    if request.method == "POST":
        id_r = request.POST.get("bus_id")
        seats_r = int(request.POST.get("no_seats"))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(
                    name=username_r,
                    email=email_r,
                    userid=userid_r,
                    bus_name=name_r,
                    source=source_r,
                    busid=id_r,
                    dest=dest_r,
                    price=price_r,
                    nos=seats_r,
                    date=date_r,
                    time=time_r,
                    status="BOOKED",
                )
                print("------------book id-----------", book.id)
                # book.save()
                return render(request, "myapp/bookings.html", locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, "findbus.html", context)

    else:
        return render(request, "findbus.html")


@login_required(login_url="login")
def cancellings(request):
    context = {}
    if request.method == "POST":
        id_r = request.POST.get("bus_id")
        # seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            # nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status="CANCELLED")
            Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request, "Booked Bus has been cancelled successfully.")
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, "error.html", context)
    else:
        return render(request, "findbus.html")


@login_required(login_url="login")
def seebookings(request, new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, "myapp/booklist.html", locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, "findbus.html", context)


def success(request):
    context = {}
    context["user"] = request.user
    return render(request, "success.html", context)


# def payment(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         amount = int(request.POST.get("amount")) * 100
#         client = razorpay.Client(
#             auth=("rzp_test_3JslblohjnJjXS", "Q8R1bVrnNAt5ieyXp2zy2kSa")
#         )
#         payment = client.order.create(
#             {"amount": amount, "currency": "INR", "payment_capture": "1"}
#         )
#         print(payment)
#         coffee = Payment(name=name, amount=amount, email=email, payment_id=payment["id"])
#         coffee.save()
#         return render(request, "myapp/payment.html", {"payment": payment})
#     return render(request, "myapp/payment.html")

@csrf_exempt
def pay_succ(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        user = Payment.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request, "pay_succ.html")

def payment01(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(
            auth=("rzp_test_eTRHvcz3rU4TBg", "aAtTlQpVk9waIgQGpI6FxDdm")
        )
        payment = client.order.create(
            {"amount": amount, "currency": "INR", "payment_capture": "1"}
        )
        print(payment)
        coffee = Payment(name=name, amount=amount, email=email, payment_id=payment["id"])
        coffee.save()
        return render(request, "payment01.html", {"payment": payment})
    return render(request, "payment01.html")

