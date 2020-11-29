import csv  # https://docs.python.org/3/library/csv.html

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

    for row in reader:
        print(row)
        print("rrzm: hola")
        print("rrzm: ", row[0])
        print("rrzm: ", row[1])
        print("rrzm: ", row[2])

        n, created = Site.objects.get_or_create(name=row[0])
        d, created = Site.objects.get_or_create(description=row[1])
        j, created = Site.objects.get_or_create(justification=row[2])
        y, created = Site.objects.get_or_create(year=row[3])
        lo, created = Site.objects.get_or_create(longitude=row[4])
        la, created = Site.objects.get_or_create(latitude=row[5])
        a, created = Site.objects.get_or_create(area_hectare=row[6])
    
        c, created = Category.objects.get_or_create(categoryname=row[7])
        s, created = States.objects.get_or_create(statename=row[8])
        r, created = Region.objects.get_or_create(regionname=row[9])
        i, created = Iso.objects.get_or_create(isoname=row[10])
        
        try:
            j = row[2]
        except:
            j = None

        try:
            a = int(row[6])
        except:
            a = None

        try:
            i = row[10]
        except:
            i= None

        si = Site(name=n, year=y, category=c, states=s, regionname=r, isoname=i, justification=j, longitude=lo, latitude=la, area_hectare=a )
        si.save()
