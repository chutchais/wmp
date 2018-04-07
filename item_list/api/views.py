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

from item_list.models import ItemList
from .serialize import (ItemListListSerializer,
						ItemListCreateSerializer,
						ItemListDetailSerializer,
						ItemListUpdateSerializer)



class ItemListListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = ItemListListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = ItemList.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = ItemList.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class ItemListDetailAPIView(RetrieveAPIView):
	queryset= ItemList.objects.all()
	serializer_class = ItemListDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class ItemListDeleteAPIView(DestroyAPIView):
	queryset= ItemList.objects.all()
	serializer_class= ItemListDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class ItemListCreateAPIView(CreateAPIView):
	queryset= ItemList.objects.all()
	serializer_class= ItemListCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class ItemListUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=ItemList.objects.all()
	serializer_class=ItemListUpdateSerializer
	lookup_field='slug'

