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

from routing_next.models import RoutingNext

from .serialize import (RoutingNextListSerializer,
						RoutingNextCreateSerializer,
						RoutingNextDetailSerializer,
						RoutingNextUpdateSerializer)



class RoutingNextListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = RoutingNextListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = RoutingNext.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = RoutingNext.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class RoutingNextDetailAPIView(RetrieveAPIView):
	queryset= RoutingNext.objects.all()
	serializer_class = RoutingNextDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class RoutingNextDeleteAPIView(DestroyAPIView):
	queryset= RoutingNext.objects.all()
	serializer_class = RoutingNextDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class RoutingNextCreateAPIView(CreateAPIView):
	queryset= RoutingNext.objects.all()
	serializer_class = RoutingNextCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class RoutingNextUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=RoutingNext.objects.all()
	serializer_class = RoutingNextUpdateSerializer
	lookup_field='slug'

