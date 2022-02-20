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
    # path('', views.login.as_view(), name='post_list'),
    # path('', include(router.urls))
    path('',views.login.as_view(),name=''),
    path('login/',views.homepage.as_view(),name='')


]
 