from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from bom.models import Bom,Bom_Detail,Alternate_Part
from bom.api.serializers import BomSerializer,BomDetailSerializer,BomAlternateSerializer


class BomViewSet(viewsets.ModelViewSet):
	queryset = Bom.objects.all()
	serializer_class = BomSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'description')

	@detail_route()
	def items(self, request, pk=None):
		bom = self.get_object()
		serializer = BomDetailSerializer(bom.items.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)

class BomDetailViewSet(viewsets.ModelViewSet):
	queryset = Bom_Detail.objects.all()
	serializer_class = BomDetailSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('rd','pn', 'description')

	@detail_route()
	def alternates(self, request, pk=None):
		bom_detail = self.get_object()
		serializer = BomAlternateSerializer(bom_detail.alternates.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)


class BomAlternateViewSet(viewsets.ModelViewSet):
	queryset = Alternate_Part.objects.all()
	serializer_class = BomAlternateSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('pn', 'description')