from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from performing.models import Performing
from performing.api.serializers import PerformingSerializer



class PerformingViewSet(viewsets.ModelViewSet):
	queryset = Performing.objects.all()
	serializer_class = PerformingSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter)
	search_fields = ('sn','operation__name','resource_name')

	# @detail_route()
	# def users(self, request, pk=None):
	# 	operation = self.get_object()
	# 	serializer = UserAccessListSerializer(operation.users.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)