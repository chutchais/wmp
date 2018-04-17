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

from bom_detail.models import Bom_Detail
from .serialize import (BomDetailListSerializer,
						BomDetailCreateSerializer,
						BomDetailDetailSerializer,
						BomDetailUpdateSerializer)



class BomDetailListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = BomDetailListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list =Bom_Detail.objects.all()
		name = self.request.GET.get("q")
		if name != None :
			queryset_list = BomDetail.objects.filter(
					Q(bom__name = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class BomDetailDetailAPIView(RetrieveAPIView):
	queryset= Bom_Detail.objects.all()
	serializer_class = BomDetailDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class BomDetailDeleteAPIView(DestroyAPIView):
	queryset= Bom_Detail.objects.all()
	serializer_class= BomDetailDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class BomDetailCreateAPIView(CreateAPIView):
	queryset= Bom_Detail.objects.all()
	serializer_class= BomDetailCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class BomDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Bom_Detail.objects.all()
	serializer_class=BomDetailUpdateSerializer
	lookup_field='slug'
