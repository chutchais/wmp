from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	SlugRelatedField,
	HyperlinkedModelSerializer,
	ReadOnlyField
	)

from hook.models import Hook


hook_detail_url=HyperlinkedIdentityField(
		view_name='hook-api:detail',
		lookup_field='slug'
		)





class HookListSerializer(ModelSerializer):
	url = hook_detail_url
	routing_detail =  SlugRelatedField(read_only=True,slug_field='slug')
	snippet 	   =  SlugRelatedField(read_only=True,slug_field='slug')
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Hook
		# fields ='__all__'
		fields =[
			'name',
			'event',
			'title',
			'url',
			'slug',
			'routing_detail',
			'snippet',
			'description',
			'category1',
			'category2',
			'status',
			'user'
		]

class HookDetailSerializer(ModelSerializer):
	# routing 	= RoutingListSerializer(read_only=True)
	class Meta:
		model = Hook
		fields ='__all__'

class HookCreateSerializer (ModelSerializer):
	class Meta:
		model = Hook
		fields =[
			'name',
			'event',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]
		
		# def perform_create(self, serializer):
  #   serializer.save(owner=self.request.user)


class HookUpdateSerializer (ModelSerializer):
	class Meta:
		model = Hook
		fields =[
			'name',
			'event',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



