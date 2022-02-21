from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Station(models.Model):
    reference = models.CharField(max_length=200)
    evse_count = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


    def __str__(self):
        return self.reference
    
