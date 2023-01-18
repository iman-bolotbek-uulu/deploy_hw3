from rest_framework import viewsets, generics
from rest_framework import permissions

from . import models
from . import serializers
from account.permissions import IsAuthorPermission


class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAuthorPermission, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

