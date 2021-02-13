from django.contrib import admin
from compu.models import Computer
from .forms import ComputerForm

class ComputerAdmin(admin.ModelAdmin):
    list_display = ['computer_name', 'IP_address', 'MAC_address']
    form = ComputerForm
    list_filter = ['computer_name', 'IP_address']
    search_fields = ['computer_name', 'IP_address']

admin.site.register(Computer, ComputerAdmin)
