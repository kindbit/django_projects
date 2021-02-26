from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from phone_field import PhoneField

class Specie(models.Model):
    specie_choices =(
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
    )

    specie = models.CharField(max_length=10, choices=specie_choices, null=True)

    def __str__(self):
        return self.specie

class Gender(models.Model):
    gender_choices= (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = models.CharField(max_length=50, choices=gender_choices, null=True)

    def __str__(self):
        return self.gender

class Size(models.Model):
    size_choices = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Big','Big'),
    )

    size = models.CharField(max_length=50, choices=size_choices, null=True)

    def __str__(self):
        return self.size

class Vaccinated(models.Model):
    yes_no_choices = (
        ('Yes','Yes'),
        ('No','No'),
    )

    vaccinated = models.CharField(max_length=50, choices=yes_no_choices, null=True)

    def __str__(self):
        return self.vaccinated

class Sterilized(models.Model):
    yes_no_choices = (
        ('Yes','Yes'),
        ('No','No'),
    )

    sterilized = models.CharField(max_length=50, choices=yes_no_choices, null=True)

    def __str__(self):
        return self.sterilized

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )

    breed = models.CharField(max_length=30, null=True)
    weight = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    age = models.IntegerField(null=True)

    #price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Picture
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    #Contact
    name = models.CharField(max_length=100, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    #Comment
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ad_petowned')

    #Foreign keys
    specie     = models.ForeignKey(Specie, null=True, on_delete=models.SET_NULL)
    gender     = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    size       = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    vaccinated = models.ForeignKey(Vaccinated, null=True, on_delete=models.SET_NULL)
    sterilized = models.ForeignKey(Sterilized, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
