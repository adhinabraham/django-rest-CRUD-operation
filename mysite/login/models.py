import email
from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class person(models.Model):
   name  = models.CharField(max_length=255)
   password  = models.SlugField(unique=True, max_length=255)
   email = models.EmailField(max_length=254,)
  