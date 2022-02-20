from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','id',]
