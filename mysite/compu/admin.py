from django.contrib import admin
from compu.models import Computer, Operating_System
from .forms import ComputerForm

class ComputerAdmin(admin.ModelAdmin):
    list_display = ['computer_name', 'IP_address', 'users_name', 'MAC_address', 'purchase_date', 'timestamp']
    form = ComputerForm
    list_filter = ['computer_name', 'IP_address']
    search_fields = ['computer_name', 'IP_address', 'MAD_address']

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Operating_System)
