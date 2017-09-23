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

from shopfloor.models import SerialNumber
from .serialize import (SerialNumberListSerializer,
						SerialNumberCreateSerializer,
						SerialNumberDetailSerializer,
						SerialNumberUpdateSerializer)



class SerialNumberListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = SerialNumberListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['number']
	def get_queryset(self,*args,**kwargs):
		queryset_list =None #Booking.objects.all()
		number = self.request.GET.get("number")
		if number != None :
			queryset_list = SerialNumber.objects.filter(
					Q(number__icontains = number))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class SerialNumberDetailAPIView(RetrieveAPIView):
	queryset= SerialNumber.objects.all()
	serializer_class = SerialNumberDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class SerialNumberDeleteAPIView(DestroyAPIView):
	queryset= SerialNumber.objects.all()
	serializer_class= SerialNumberDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class SerialNumberCreateAPIView(CreateAPIView):
	queryset= SerialNumber.objects.all()
	serializer_class= SerialNumberCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class SerialNumberUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=SerialNumber.objects.all()
	serializer_class=SerialNumberUpdateSerializer
	lookup_field='slug'

