from django.db import models
from datetime import datetime, date

class Operating_System(models.Model):

    os_choice = (
            ('Windows 10','Windows 10'),
            ('Windows 8', 'Windows 8'),
            ('Linux','Linux'),
            )   

    operating_system = models.CharField(max_length=30, blank=True)

    #def __unicode__(self):
    def __str__(self):
        return self.operating_system

class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True)
    IP_address = models.CharField(max_length=30, blank=True)
    operating_system = models.ForeignKey(Operating_System, blank=True, null=True, on_delete=models.SET_NULL)
    MAC_address = models.CharField(max_length=30, blank=True)
    users_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    purchase_date = models.DateField("Purchase Date (mm/dd/yyyy)", auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    export_to_CSV = models.BooleanField(default=False)

    def __unicode__(self):
        return self.IP_address + ' ' + self.computer_name
