from django.db import models


class Item(models.Model):
    product_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_name}"


class Receipt(models.Model):
    created_on = models.DateTimeField()
    items = models.ManyToManyField(Item, related_name="items")
