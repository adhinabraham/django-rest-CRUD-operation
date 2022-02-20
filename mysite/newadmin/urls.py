from os import name
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# router = routers.SimpleRouter()
# router.register('', views.login)

urlpatterns = [
    
    path('login',views.login.as_view(),name=''),
    # path('/users',views.users.as_view(),name=''),
    path('delete/<int:id>',views.delete.as_view(),name=''),
    
   
    
]