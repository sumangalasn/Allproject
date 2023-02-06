
from django.db import models
# Create your models here.


class ProductList(models.Model):
  id = models.AutoField(
    primary_key=True
  )
  name = models.CharField(max_length=10, blank=True)
  price = models.IntegerField(blank=True)
  quality = models.CharField(max_length=30, blank=True)
  image = models.ImageField(max_length=255, blank=True)

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=True,
    blank=False
  )

  class Meta:
    db_table = 'products'