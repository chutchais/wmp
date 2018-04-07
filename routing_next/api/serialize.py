from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from routing_next.models import RoutingNext


routing_next_url=HyperlinkedIdentityField(
		view_name='routing_next-api:detail',
		lookup_field='slug'
		)





class RoutingNextListSerializer(ModelSerializer):
	url = routing_next_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = RoutingNext
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class RoutingNextDetailSerializer(ModelSerializer):
	class Meta:
		model = RoutingNext
		fields ='__all__'

class RoutingNextCreateSerializer (ModelSerializer):
	class Meta:
		model = RoutingNext
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]
		
		# def perform_create(self, serializer):
  #   serializer.save(owner=self.request.user)


class RoutingNextUpdateSerializer (ModelSerializer):
	class Meta:
		model = RoutingNext
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



