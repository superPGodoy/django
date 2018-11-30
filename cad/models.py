from django.db import models

# Create your models here.
from django.db import models


class Supplier(models.Model):
  name = models.CharField(max_length=50, blank=False)



  def __str__(self):
    return self.name

class Client(models.Model):
  name = models.CharField( max_length=50, blank=False)


  def __str__(self):
    return self.name
