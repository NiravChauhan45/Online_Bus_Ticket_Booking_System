from django.urls import path,include
from home import views
from . views import *
urlpatterns = [
    path('home',views.home,name="home"),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('elements',views.elements,name="elements"),
    path('offers',views.offers,name="offers"),
    path('single_listing',views.offers,name="single_listing"),
    
    

    # authentications part
    path('singup',views.handleSignUp,name="handleSignUp"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('ChangePass',views.ChangePass,name="ChangePass"),


    path('findbus',views.findbus,name="findbus"),
    # path('payment',views.payment,name="payment"),
    path('pay_succ',views.pay_succ,name="pay_succ"),
    # path('paymenr',views.paymenr,name="paymenr"),
    path('payment01',views.payment01,name="payment01"),
    


    

    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('success', views.success, name="success"),   
]



