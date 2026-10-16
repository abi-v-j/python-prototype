
from django.db import models
from django.db.models import Q


class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_code = models.CharField(max_length=20, unique=True)
    item_name = models.CharField(max_length=100)
    uom = models.CharField(max_length=10, default="NOS")
    unit_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

 