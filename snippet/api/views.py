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

from shopfloor.models import Snippet
from .serialize import (SnippetListSerializer,
						SnippetCreateSerializer,
						SnippetDetailSerializer,
						SnippetUpdateSerializer)



class SnippetListAPIView(ListAPIView):
	queryset = None #Booking.objects.all()
	serializer_class = SnippetListSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['name']
	def get_queryset(self,*args,**kwargs):
		queryset_list =None #Booking.objects.all()
		name = self.request.GET.get("name")
		if name != None :
			queryset_list = Snippet.objects.filter(
					Q(name__icontains = name))
		return queryset_list
	# pagination_class = PostPageNumberPagination

class SnippetDetailAPIView(RetrieveAPIView):
	queryset= Snippet.objects.all()
	serializer_class = SnippetDetailSerializer
	lookup_field = 'slug'
	# print ("vessel details")

class SnippetDeleteAPIView(DestroyAPIView):
	queryset= Snippet.objects.all()
	serializer_class= SnippetDetailSerializer
	lookup_field='slug'
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class SnippetCreateAPIView(CreateAPIView):
	queryset= Snippet.objects.all()
	serializer_class= SnippetCreateSerializer
	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		print ('Voy is %s' % self.kwargs.get('voy'))
# 		serializer.save()
class SnippetUpdateAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Snippet.objects.all()
	serializer_class=SnippetUpdateSerializer
	lookup_field='slug'

