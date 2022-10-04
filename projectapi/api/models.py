from django.db import models

# Create your models here.


class SalesHistory(models.Model):
    saleshistory_id = models.BigAutoField(primary_key=True)
    sku = models.CharField(max_length=50, null=True)
    tenate_id = models.CharField(max_length=55, null=True)
    node = models.CharField(max_length=50, null=True)
    channle = models.CharField(max_length=50, null=True)
    salesman_email = models.CharField(max_length=50, null=True)
    salesman_name = models.CharField(max_length=50, null=True)
    actual_sales_volume = models.IntegerField(null=True)
    actual_sales_volume_uom = models.CharField(max_length=50, null=True)
    actual_sales_value = models.IntegerField(null=True)
    actual_sales_value_uom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.saleshistory_id)
