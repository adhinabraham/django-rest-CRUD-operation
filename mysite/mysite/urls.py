
from django.contrib import admin
from django.urls import path ,include


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView





urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('api.urls')),
    path ('',include('login.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/',include('newadmin.urls')),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
