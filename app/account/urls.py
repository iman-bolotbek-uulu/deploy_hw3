from django.urls import path, include
from rest_framework import routers
from . import views as acc_views

acc_router = routers.DefaultRouter()
acc_router.register('register', acc_views.ProfileRegisterAPIView)


urlpatterns = [
    path('api/', include(acc_router.urls)),
]