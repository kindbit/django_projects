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
        
        #print("This is the row[6] = ", row[6], type(row[6]))

        area = row[6]
        if bool(row[6]) is False:
            print("I found a null:", row[6])
            area = '0.001'
            print("area = ", area, "type: ", type(area), "cnt = ", cnt)
            

        n, created = Site.objects.get_or_create(name=row[0])
        d, created = Site.objects.get_or_create(description=row[1]) 
        j, created = Site.objects.get_or_create(justification=row[2]) 
        y, created = Site.objects.get_or_create(year=row[3])
        lo, created = Site.objects.get_or_create(longitude=row[4])
        la, created = Site.objects.get_or_create(latitude=row[5])
        a, created = Site.objects.get_or_create(area_hectares=row[6])
        
        c, created = Category.objects.get_or_create(categoryname=row[7])
        s, created = States.objects.get_or_create(statename=row[8])
        r, created = Region.objects.get_or_create(regionname=row[9])
        i, created = Iso.objects.get_or_create(isoname=row[10])

        #if(cnt<5 or cnt==48):
            #print("rrzm: row[0]", row[0], "-", n)
            #print("rrzm: row[1]", row[1], "-", d)
            #print("rrzm: row[2]", row[2], "-", j)
            #print("rrzm: row[3]", row[3], "-", y)
            #print("rrzm: row[4]", row[4], "-", lo)
            #print("rrzm: row[5]", row[5], "-", la)
            #print("rrzm: row[6]", row[6], "-", a)
            #print("rrzm: row[7]", row[7], "-", c)
            #print("rrzm: row[8]", row[8], "-", s)
            #print("rrzm: row[9]", row[9], "-", r)
            #print("rrzm: row[10]",row[10], "-", i)
            #print("rrzm: cnt=", cnt)
            #print("-----------------------------------")
        #cnt=cnt+1
        si = Site(name=n, description=d, justification=j, year=y, longitude=lo, latitude=la, area_hectares=a, category=c, states=s, region=r, iso=i)
        si.save()
