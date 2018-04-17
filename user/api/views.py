from user.api.serializers import UserSerializer
from rest_framework import generics

# from django.contrib.auth.models import User
from user.models import WMPUser

class UserList(generics.ListAPIView):
    queryset = WMPUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = WMPUser.objects.all()
    serializer_class = UserSerializer