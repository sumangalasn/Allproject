from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class LoginformList(models.Model):
  username = models.AutoField(
    primary_key=True
  )
  password = models.IntegerField(max_length=10, blank=True)




  class Meta:
    db_table = 'loginform'