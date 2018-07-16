from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from routing.models import (Routing,RoutingDetail,
								RoutingDetailNext,RoutingDetailReject,RoutingDetailAccept)
from routing.api.serializers import (RoutingSerializer,RoutingDetailSerializer,
								RoutingNextSetSerializer,RoutingDetailNextSerializer,
								RoutingDetailAcceptSerializer,RoutingDetailRejectSerializer)


class RoutingViewSet(viewsets.ModelViewSet):
	queryset = Routing.objects.all()
	serializer_class = RoutingSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title','category1','category2', 'description')

	@detail_route()
	def details(self, request, pk=None):
		routing = self.get_object()
		print (routing)
		serializer = RoutingDetailSerializer(routing.details.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)

class RoutingDetailViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetail.objects.all()
	serializer_class = RoutingDetailSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('operation')

	@detail_route()
	def nexts(self, request, pk=None):
		routingdetail = self.get_object()
		serializer = RoutingNextSetSerializer(routingdetail.nexts.all(), 
					context={'request': request}, many=True)
		return Response(serializer.data)


class RoutingDetailNextViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailNext.objects.all()
	serializer_class = RoutingDetailNextSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title')

class RoutingDetailAcceptViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailAccept.objects.all()
	serializer_class = RoutingDetailAcceptSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title')

class RoutingDetailRejectViewSet(viewsets.ModelViewSet):
	queryset = RoutingDetailReject.objects.all()
	serializer_class = RoutingDetailRejectSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','title')