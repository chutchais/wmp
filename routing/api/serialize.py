from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import Routing
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

routing_detail_url=HyperlinkedIdentityField(
		view_name='routing-api:detail',
		lookup_field='slug'
		)





class RoutingListSerializer(ModelSerializer):
	url = routing_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Routing
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

class RoutingDetailSerializer(ModelSerializer):
	class Meta:
		model = Routing
		fields ='__all__'

class RoutingCreateSerializer (ModelSerializer):
	class Meta:
		model = Routing
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class RoutingUpdateSerializer (ModelSerializer):
	class Meta:
		model = Routing
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



