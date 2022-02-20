
from .models import Article
from .serializer import Articleserialzer,UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User




class Articleviewset(viewsets.ViewSet):
    def list(self,request):

        articles=Article.objects.all()
        serializer=Articleserialzer(articles,many=True)
        # return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

