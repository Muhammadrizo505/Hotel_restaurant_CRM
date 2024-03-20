from django.db import models
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13,blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Employee(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55, verbose_name='Your name')
    last_name = models.CharField(max_length=55, verbose_name='Your surname')
    phone_number = models.CharField(max_length=13, blank=True, null=True,verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Oyligiz')
    age = models.IntegerField(default=15, verbose_name='Yoshingiz')
    start_work_at = models.TimeField()
    end_work_at = models.TimeField()
    rating = models.FloatField(default=0)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name

class Hotel(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    bank_number = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    quantity_of_rooms = models.IntegerField(default=0)
    contact = models.CharField(max_length=13, blank=True, null=True,verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    location = models.ForeignKey(to='Address', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='Hotel_img/')



class Restouran(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=55)
    bank_number = models.PositiveIntegerField(null=True, blank=True)
    location = models.ForeignKey(to='Address', on_delete=models.PROTECT)
    description = models.TextField()
    contact = models.CharField(max_length=13, blank=True, null=True, verbose_name='Phone_number', unique=True,validators=[
            RegexValidator(
                regex='^[\+]9{2}8{1}[0-9]{9}$',
                message='Invalide phone number',
                code='Invalid number'
        )
    ])



class Address(models.Model):
    name = models.CharField(max_length=55, verbose_name='Adress')

    def __str__(self):
       return self.name



class Order(models.Model):
    name = models.CharField(max_length=55, verbose_name='Your name')
    food = models.ManyToManyField(to='Menu', verbose_name='Choose the food')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='Number of your room ')
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.first_name)
            super().save(*args, **kwargs)





class Rating(models.Model):
    rating = models.FloatField(default=0, verbose_name='Rate')


    def __str__(self):
        return self.rating


class Food_category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Menu(models.Model):
   name = models.CharField(max_length=55, verbose_name='Name of food')
   category = models.ForeignKey(to='Food_category', on_delete=models.PROTECT, verbose_name='Type of food')
   description = models.CharField(max_length=255, verbose_name='All about food')
   price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
   img = models.ImageField(upload_to='menu_img/', verbose_name='Photo', null=True, blank=True)

   def __str__(self):
      return self.name


class Order_food(models.Model):
    name = models.CharField(max_length=55, verbose_name='Your name')
    food = models.ManyToManyField(to='Menu', verbose_name='Name of food' )
    is_deliver = models.BooleanField(default=False, verbose_name='Is delivery')
    PAYMENT_TYPE = (
        ('Cash', 'Cash'),
        ('Card ', 'Card ')
    )
    payment_type = models.CharField(max_length=55, choices=PAYMENT_TYPE)
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.phone_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

















