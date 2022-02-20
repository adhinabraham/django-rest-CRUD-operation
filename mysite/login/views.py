import email
from lib2to3 import refactor

from urllib import response
from django.forms import PasswordInput
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth import authenticate,login
from mysite.settings import AUTH_PASSWORD_VALIDATORS
from .serializers import user_serializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import person
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
# class login(viewsets.ModelViewSet):
#     queryset = person.objects.all()
#     serializer_class = user_serializer
    
    
    # def get(self, request, format=None):
    #     user = person.objects.all()
    #     print(user)
    #     serializer =  user_serializer(data = user ,many = True)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
        

       

    # def create (self,request):
    #     print("enterd")
    #     name = request.data.get('name')
    #     password = request.data.get('password')
    #     email = request.data.get('email')
        
    #     print(name)
    #     password1 = make_password(password)
    #     print(password)
    #     print(email)
    #     person.objects.create(name=name,password=password1,email=email)
    #     return Response( status=status.HTTP_201_CREATED)

class login(APIView):
    def post(self,request):
        print ('login')
        # token=(IsAuthenticated,)

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        print(username,password,email)
        password1 = make_password(password)
        user =User.objects.create(username=username,password=password1,email=email)
        user.save()
        token = Token.objects.create(user=user)
        print(token.key)
        data = {"sucess":"user created successfully"}
        print(data)

        return Response(data, status=status.HTTP_201_CREATED)

class homepage(APIView):
    def post (self,request):
        password=request.data.get('password')
        email=request.data.get('email')
        print(password,email)


            # refresh = RefreshToken.for_user(user)
            #         return Response({
            #             "user"  : serializers.data,
            #             'refresh': str(refresh),
            #             'access': str(refresh.access_token),
            #         })
      
        # password1 =request.data.get('password')
        # user = {"email":email1,"password":password1}
        if User.objects.filter(email=email).exists():
            
            
            print('user is in the database ')
            refresh = RefreshToken.for_user(User)
            
          
            request.session=True
            print(refresh)
            
            return Response({'refresh':str(refresh),'access':str(refresh.access_token)},status=status.HTTP_200_OK)
     
        else:
            request.session=False
            print('user is not the database ')
            data={"data":"false"}
            return Response (data)
       

# class FormClass:
# 	username = ...
# 	def clean(self):
# 		super(FormClass, self).clean()
#     	username = self.cleaned_data['username']
#     	if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#         	raise forms.ValidationError(f'Username "{username}" is already in use.')
#     	return username
# {"email":"adhin@gmail.com",
# "password":"1414"}
#   {"username":"a",
# "email":"a@gmail.com",
# "password":"123456"}


