from django.db import models

# Create your models here.
class SalesHistory(models.Model):
    saleshistory_id = models.BigAutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    tenate_id = models.CharField(max_length=55)
    node = models.CharField(max_length=50)
    channle = models.CharField(max_length=50)
    salesman_email = models.CharField(max_length=50)
    salesman_name = models.CharField(max_length=50)
    actual_sales_volume = models.IntegerField()
    actual_sales_volume_uom = models.CharField(max_length=50)
    actual_sales_value = models.IntegerField()
    actual_sales_value_uom = models.CharField(max_length=50)

    def __int__(self):
        return self.saleshistory_id
