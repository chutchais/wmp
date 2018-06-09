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

from hook.models import Hook
from .serialize import (HookListSerializer,
						HookCreateSerializer,
						HookDetailSerializer,
						HookUpdateSerializer)



class HookListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = HookListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['q']
	def get_queryset(self,*args,**kwargs):
		queryset_list =Hook.objects.all()
		name = self.request.GET.get('q')
		if name != None :
			queryset_list = Hook.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class HookDetailAPIView(RetrieveAPIView):
	queryset= Hook.objects.all()
	serializer_class = HookDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class HookDeleteAPIView(DestroyAPIView):
	queryset= Hook.objects.all()
	serializer_class= HookDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class HookCreateAPIView(CreateAPIView):
	queryset= Hook.objects.all()
	serializer_class= HookCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class HookUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Hook.objects.all()
	serializer_class=HookUpdateSerializer
	lookup_field='slug'

