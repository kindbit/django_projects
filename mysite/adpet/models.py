from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Computer(models.Model):
    computer_name = models.CharField(max_length=30)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    users_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    category_choice = (
		('Furniture', 'Furniture'),
		('IT Equipment', 'IT Equipment'),
		('Phone', 'Phone'),
	)
    category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
    def __unicode__(self):
        return self.computer_name

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )

    CAT = 'CT'
    DOG = 'DG'

    NAME_SPECIE =(
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    )

    specie = models.CharField(max_length=200, choices=NAME_SPECIE)
    
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )

    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)

    SEIZE_CHOICES = (
        (0,'Small'),
        (1,'Medium'),
        (2,'Big'),
    )

    seize = models.IntegerField(choices=SEIZE_CHOICES, null=True)

    YES_NO_CHOICES = (
        (0,'Yes'),
        (1,'No'),
    )
    
    vaccinated = models.IntegerField(choices=YES_NO_CHOICES, null=True)
    sterilized = models.IntegerField(choices=YES_NO_CHOICES, null=True)

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
