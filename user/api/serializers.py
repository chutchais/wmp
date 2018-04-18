from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField
	)

from rest_framework import serializers

# from django.contrib.auth.models import User
from user.models import WMPUser
from snippet.models import Snippet

from operation.api.serialize import  OperationListSerializer



class UserDetailSerializer(serializers.ModelSerializer):
    operations = OperationListSerializer(many=True, read_only=True)
    class Meta:
        model = WMPUser
        fields = ('id', 'username','operations','groups')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WMPUser
        fields = ('id', 'username')