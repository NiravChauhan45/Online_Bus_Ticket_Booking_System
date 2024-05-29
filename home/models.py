from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = HTMLField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + '-'+ self.email


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    
    class Meta:
        verbose_name_plural = "List of Busses"

    def __str__(self):
        return self.bus_name



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    class Meta:
        verbose_name_plural = "List of Books"
    def __str__(self):
        return self.email

class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
   # paid = models.BooleanField(default=False)
   
class book_des(models.Model):
    book_title = models.CharField(max_length=100)
    book_des=models.TextField()

class pack(models.Model):
    pack_title= models.CharField(max_length=120)
    pack_rating= models.CharField(max_length=120)
    pack_des= models.TextField()

class clients(models.Model):
    client_image= models.ImageField()
    client_name = models.CharField(max_length=100)
    client_date = models.DateField()
    client_title = models.CharField(max_length=100)
    client_des = models.TextField()

class aboutt(models.Model):
    aboutt_title = models.CharField(max_length=100)
    aboutt_des=models.TextField()