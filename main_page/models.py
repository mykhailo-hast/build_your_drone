from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField (max_length=200) #, blank=False, null=False
    google_id = models.CharField (max_length=200)
    password = models.CharField (max_length=200)
    name = models.CharField (max_length=200)
    surname = models.CharField (max_length=200)
    phone = models.DecimalField (decimal_places=2, max_digits=12)

class Build(models.Model):
    name = models.CharField (max_length=200)
    description = models.TextField (null=True, blank=True)
    date = models.DateTimeField ()
    user_id = models.ForeignKey (User, on_delete=models.SET_NULL, null=True, blank=True)

class Components(models.Model):
    name = models.CharField (max_length=200)
    description = models.CharField (max_length=200)
    category = models.CharField (max_length=200)
    manufacturer = models.CharField (max_length=200)
    amount = models.PositiveIntegerField()
    price = models.DecimalField (decimal_places=2, max_digits=12)
    photo = models.ImageField ()

class Builds_components(models.Model):
    build_id = models.ForeignKey (Build, on_delete=models.SET_NULL, null=True, blank=True)
    component_id = models.ForeignKey (Components, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.PositiveIntegerField ()

class Favorites (models.Model):
    user_id = models.ForeignKey (User, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey (Components, on_delete=models.SET_NULL, null=True, blank=True)
