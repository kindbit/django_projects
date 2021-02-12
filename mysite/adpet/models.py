from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
#from phone_field import PhoneField

#class Contact(models.model):
#    name = models.CharField(max_length=100, null=True)
#    phone = PhoneField(blank=True, help_text='Contact phone number')

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )

    specie_choices =(
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
    )

    specie = models.CharField(max_length=50, choices=specie_choices, null=True)

    gender_choices= (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = models.CharField(max_length=50, choices=gender_choices, null=True)

    size_choices = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Big','Big'),
    )

    size = models.CharField(max_length=50, choices=size_choices, null=True)

    yes_no_choices = (
        ('Yes','Yes'),
        ('No','No'),
    )

    vaccinated = models.CharField(max_length=50, choices=yes_no_choices, null=True)
    sterilized = models.CharField(max_length=50, choices=yes_no_choices, null=True)

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

    #Comment
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ad_petowned')
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='adpet_commented')

    # Favorites
    #favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #    through='Fav', related_name='favorite_adpet')

    # Shows up in the admin list
    def __str__(self):
        return self.title

class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_petowned')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'

class Fav(models.Model) :
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fav_user')

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.ad.title[:10])
