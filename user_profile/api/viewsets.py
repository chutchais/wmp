from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from user_profile.models import Profile
from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('user','department','title')

	@detail_route()
	def access(self, request, pk=None):
		profile = self.get_object()
		serializer = UserAccessListSerializer(profile.access.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)