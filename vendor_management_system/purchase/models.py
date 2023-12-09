from django.db import models
from vendor.models import vendor
import jsonfield

# Create your models here.
class purchase(models.Model):
    po_number=models.CharField(max_length=150)
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=jsonfield.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=150) # current,completed,canceled
    quality_rating=models.FloatField()
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField()



































