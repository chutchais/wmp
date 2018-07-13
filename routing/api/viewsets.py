from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from routing.models import Routing
from routing.api.serializers import RoutingSerializer


class RoutingViewSet(viewsets.ModelViewSet):
	queryset = Routing.objects.all()
	serializer_class = RoutingSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title','category1','category2', 'description')

	# @detail_route()
	# def workorders(self, request, pk=None):
	# 	product = self.get_object()
	# 	serializer = WorkorderSerializer(product.workorders.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)