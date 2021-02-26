from django.contrib import admin
from adpet.models import Specie,Gender,Size,Vaccinated,Sterilized,Ad 

class AdAdmin(admin.ModelAdmin):
    list_display=['phone','name','title','specie']

admin.site.register(Specie)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Vaccinated)
admin.site.register(Sterilized)
admin.site.register(Ad)
