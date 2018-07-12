from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from workorder.models import WorkOrder
from workorder.api.serializers import WorkorderSerializer
# from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class WorkorderViewSet(viewsets.ModelViewSet):
	queryset = WorkOrder.objects.all()
	serializer_class = WorkorderSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title','category1','category2', 'description')

	# @detail_route()
	# def users(self, request, pk=None):
	# 	operation = self.get_object()
	# 	serializer = UserAccessListSerializer(operation.users.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)