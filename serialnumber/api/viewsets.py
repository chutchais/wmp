from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from serialnumber.models import SerialNumber
from serialnumber.api.serializers import SerialNumberSerializer

class SerialNumberViewSet(viewsets.ModelViewSet):
	queryset = SerialNumber.objects.all().order_by('last_modified_date')
	serializer_class = SerialNumberSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter)
	search_fields = ('=number','workorder__name','description')

	# @detail_route()
	# def workorders(self, request, pk=None):
	# 	product = self.get_object()
	# 	serializer = WorkorderSerializer(product.workorders.all(), 
	# 	context={'request': request}, many=True)
	# 	return Response(serializer.data)