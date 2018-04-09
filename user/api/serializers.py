from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField
	)

from rest_framework import serializers

from django.contrib.auth.models import User
from snippet.models import Snippet



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippets = snippet_url
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')