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

from defect_code.models import DefectCode
from .serialize import (DefectCodeListSerializer,
						DefectCodeCreateSerializer,
						DefectCodeDetailSerializer,
						DefectCodeUpdateSerializer)



class DefectCodeListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = DefectCodeListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list = DefectCode.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = DefectCode.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class DefectCodeDetailAPIView(RetrieveAPIView):
	queryset= DefectCode.objects.all()
	serializer_class = DefectCodeDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class DefectCodeDeleteAPIView(DestroyAPIView):
	queryset= DefectCode.objects.all()
	serializer_class= DefectCodeDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class DefectCodeCreateAPIView(CreateAPIView):
	queryset= DefectCode.objects.all()
	serializer_class= DefectCodeCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class DefectCodeUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=DefectCode.objects.all()
	serializer_class=DefectCodeUpdateSerializer
	lookup_field='slug'

