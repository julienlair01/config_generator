from django.db import models
from catalog.models import Manufacturer, Customer

class Install(models.Model):
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.reference
    
    
class Chargebox(models.Model):
    install_id = models.ForeignKey(Install, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.install_id
    
    class Meta:
        verbose_name_plural = "Chargeboxes"
        

class Evse(models.Model):
    chargebox_id = models.ForeignKey(Chargebox, on_delete=models.CASCADE)
    evse_id = models.CharField(max_length=6)
    
    def __str__(self):
        return self.install_id