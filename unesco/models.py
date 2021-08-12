from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name
        

class State(models.Model) :
    name = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.name
        
    
class ISO(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.name
        
    
class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    

    def __str__(self) :
        return self.name
