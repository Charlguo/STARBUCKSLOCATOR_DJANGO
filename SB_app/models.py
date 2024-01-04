from django.db import models
import geocoder
# Create your models here.
class City(models.Model):
    city_title = models.CharField(max_length = 60) 
    def __str__(self):
        return self.city_title

class Location(models.Model):
    location = models.CharField(max_length = 200)
    city  =  models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    lat = models.CharField(max_length = 20,null=True,blank=True)
    long = models.CharField(max_length = 20,null=True,blank=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.location, key='pk.eyJ1IjoibWFyc2htYWxsb3dib3NzIiwiYSI6ImNscXR4Nnh1bjQ3ZHEya3BoaXZtZDU5ejcifQ.wqPjNj7r2AIykLhgy5JrPQ')
        dict = list(g.latlng)
        self.lat=dict[0]
        self.long=dict[1]
        super(Location, self).save(*args, **kwargs)

    def __str__(self):
        return self.location