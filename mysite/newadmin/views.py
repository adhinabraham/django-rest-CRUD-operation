

from asyncio.log import logger
from curses.ascii import RS

from multiprocessing import AuthenticationError
from operator import is_not
from pickle import PERSID

from django.http import response

from login.models import person
# from mysite.login import serializers
# from mysite.login import serializers

from .serializer import admin_serializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializer import  admin_serializer

# from mysite.newadmin import serializer







class login(APIView):
    def post(self,request):
        print(" kerundooo")
        username=request.data.get('username')
        print(username)
        password=request.data.get('password')
        print(password)
       
        aj=authenticate(username=username,password=password)
       
        if aj is not None:
            print("user endeeee....")
            if aj.is_superuser:
               print("admin")
               admin=True
            #    data=User.objects.all()
            #    print(data)
            #    serialzer=admin_serializer(data,many=True)
            #    print(serialzer.data)
               return Response({'istrue':admin})
            else:
                admin=False
                print("not admin")
                return Response({'failed':admin})
        else:
            print("not a user ")
            admin=False
            return Response({'failed':admin})
    def get(self,request):
        print("")
        data=User.objects.all()
        serialzer=admin_serializer(data,many=True)
        print("serialzer  : ",serialzer)
        print("serialzer.data  : ",serialzer.data)
        return Response(serialzer.data)

  



  


class delete(APIView):
    def delete(self,request,id):
        data = User.objects.get(id=id)
        print(id)
        if data is not None:
           print("user endee")
           data.delete()
           message=("data deleted")
           return Response(message)
        else:
            return Response("user not found")
        

            
            
        
              
      



        




       
# {"username":"adhinabraham",
# "password":"1414"}



