import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Region, State, ISO


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    ISO.objects.all().delete()
    
    for row in reader:
        print(row)

        name = row[0]
        category, created = Category.objects.get_or_create(name=row[7])
        region, created = Region.objects.get_or_create(name=row[9])
        state, created = State.objects.get_or_create(name=row[8])
        iso, created = ISO.objects.get_or_create(name=row[10])
        
        try:
            year = int(row[3])
        except:
            year = None
            
        try:
            longitude = float(row[4])
        except:
            longitude = None
            
        try:
            latitude = float(row[5])
        except:
            latitude = None
            
        try:
            area_hectares = float(row[6])
        except:
            area_hectares = None
        
        m = Site(name=name, year=year, category=category, state=state, region=region, iso=iso,
        longitude=longitude, latitude=latitude, area_hectares=area_hectares)
        m.save()
    