from django.db import models

class newadmin(models.Model):
    adminname  = models.CharField(max_length=255)
    password  = models.SlugField(unique=True, max_length=255)
    email = models.EmailField(max_length=254,)
  