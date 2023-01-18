from django.urls import path, include
from rest_framework import routers
from . import views as firm_views

firm_router = routers.DefaultRouter()
firm_router.register('employee', firm_views.EmployeeViewSet)


urlpatterns = [
    path('api/', include(firm_router.urls)),
    path('api/position/', firm_views.PositionListCreateAPIView.as_view()),
    path('api/position/<int:pk>/', firm_views.PositionRetrieveUpdateDestroyAPIView.as_view()),
]