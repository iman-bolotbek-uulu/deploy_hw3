from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ProfileRegisterSerializer
from .models import Profile
from rest_framework.decorators import action


class ProfileRegisterAPIView(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def create_profile(self, request, is_author):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_author=is_author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def author(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=['POST'], detail=False)
    def guest(self, request, pk=None):
        return self.create_profile(request, False)

