from django.urls import path

from .views import Articleviewset, UserViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register('articles',Articleviewset,basename='article')
router.register('users',UserViewSet)


urlpatterns = [
  path('api/',include(router.urls)),
  # path('articles/',Aritclelist.as_view())
  
]
