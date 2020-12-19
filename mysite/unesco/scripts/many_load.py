import csv  # https://docs.python.org/3/library/csv.html
from decimal import Decimal

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    cnt=0
    for row in reader:

        area = row[6]
        if bool(row[6]) is False:
            print("I found a null:", row[6])
            area = '0.001'
            print("area = ", area, "type: ", type(area), "cnt = ", cnt)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        si, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=row[3], longitude=row[4], latitude=row[5], area_hectares=row[6], category=c, states=s, region=r, iso=i)

        si.save()
