from django.db import models

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=False, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00) 

    class Meta:
        db_table = 'product'
