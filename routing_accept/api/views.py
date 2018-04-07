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

from routing_accept.models import RoutingAccept

from .serialize import (RoutingAcceptListSerializer,
						RoutingAcceptCreateSerializer,
						RoutingAcceptDetailSerializer,
						RoutingAcceptUpdateSerializer)



class RoutingAcceptListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = RoutingAcceptListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = RoutingAccept.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = RoutingAccept.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class RoutingAcceptDetailAPIView(RetrieveAPIView):
	queryset= RoutingAccept.objects.all()
	serializer_class = RoutingAcceptDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class RoutingAcceptDeleteAPIView(DestroyAPIView):
	queryset= RoutingAccept.objects.all()
	serializer_class = RoutingAcceptDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class RoutingAcceptCreateAPIView(CreateAPIView):
	queryset= RoutingAccept.objects.all()
	serializer_class = RoutingAcceptCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class RoutingAcceptUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=RoutingAccept.objects.all()
	serializer_class = RoutingAcceptUpdateSerializer
	lookup_field='slug'

