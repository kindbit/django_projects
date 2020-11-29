from django.contrib import admin
from ads.models import Ad, Comment

# Register your models here.

# We want the admin UI to leave the picture and content_type alone

# Define the AdAdmin class
class AdAdmin(admin.ModelAdmin):
    exclude = ('content_type',)

# Register the admin class with the associated model
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
