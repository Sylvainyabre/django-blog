from rest_framework import generics
from .serializers import UserSerializer, ProfileSerializer

from ..models import CustomUser,Profile


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer





