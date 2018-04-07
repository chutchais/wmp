from django.db.models import Q

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

# from .serialize import VoySerializer,VoyDetailSerializer
# from berth.models import Voy

from routing_detail.models import RoutingDetail
from .serialize import (RoutingDetailListSerializer,
						RoutingDetailCreateSerializer,
						RoutingDetailDetailSerializer,
						RoutingDetailUpdateSerializer)



class RoutingDetailListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = RoutingDetailListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = RoutingDetail.objects.all()
		# route = self.request.GET.get("route")
		# operation = self.request.GET.get("operation")
		# if route != None and operation != None  :
		# 	queryset_list = RoutingDetail.objects.filter(
		# 			Q(routing__name = route)&
		# 			Q(operation__name = operation))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class RoutingDetailDetailAPIView(RetrieveAPIView):
	queryset= RoutingDetail.objects.all()
	serializer_class = RoutingDetailDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class RoutingDetailDeleteAPIView(DestroyAPIView):
	queryset= RoutingDetail.objects.all()
	serializer_class= RoutingDetailDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class RoutingDetailCreateAPIView(CreateAPIView):
	queryset= RoutingDetail.objects.all()
	serializer_class= RoutingDetailCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class RoutingDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=RoutingDetail.objects.all()
	serializer_class=RoutingDetailUpdateSerializer
	lookup_field='slug'

