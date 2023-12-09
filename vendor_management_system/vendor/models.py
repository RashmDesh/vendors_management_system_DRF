from django.db import models

# Create your models here.
class vendor(models.Model):
    name=models.CharField(max_length=200)
    contact_details=models.TextField()
    address=models.TextField()
    vendore_code=models.CharField( max_length=100)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField
    

class historical_data(models.Model):
    vendor=models.ForeignKey(vendor, on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

