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

from routing_reject.models import RoutingReject

from .serialize import (RoutingRejectListSerializer,
						RoutingRejectCreateSerializer,
						RoutingRejectDetailSerializer,
						RoutingRejectUpdateSerializer)



class RoutingRejectListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = RoutingRejectListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = RoutingReject.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = RoutingReject.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class RoutingRejectDetailAPIView(RetrieveAPIView):
	queryset= RoutingReject.objects.all()
	serializer_class = RoutingRejectDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class RoutingRejectDeleteAPIView(DestroyAPIView):
	queryset= RoutingReject.objects.all()
	serializer_class = RoutingRejectDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class RoutingRejectCreateAPIView(CreateAPIView):
	queryset= RoutingReject.objects.all()
	serializer_class = RoutingRejectCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class RoutingRejectUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=RoutingReject.objects.all()
	serializer_class = RoutingRejectUpdateSerializer
	lookup_field='slug'

