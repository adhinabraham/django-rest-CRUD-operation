from dataclasses import field
from rest_framework import serializers
from .models import person
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = ['id','name','email','password']
        # extra_kwargs={"password":{"write_only":True}}


  
