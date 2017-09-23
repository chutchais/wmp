from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import RoutingDetail
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

routingdetail_detail_url=HyperlinkedIdentityField(
		view_name='routingdetail-api:detail',
		lookup_field='slug'
		)





class RoutingDetailListSerializer(ModelSerializer):
	url = routingdetail_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel =RoutingDetail VesselSerializer()
	class Meta:
		model = RoutingDetail
		# fields ='__all__'
		fields =[
			'operation',
			'routing',
			'url',
			'position',
			'next_pass',
			'next_fail',
			'description',
			'category1',
			'category2',
			'user'
		]

class RoutingDetailDetailSerializer(ModelSerializer):
	class Meta:
		model = RoutingDetail
		fields ='__all__'

class RoutingDetailCreateSerializer (ModelSerializer):
	class Meta:
		model = RoutingDetail
		fields =[
			'operation',
			'routing',
			'position',
			'next_pass',
			'next_fail',
			'description',
			'category1',
			'category2',
			'user'
		]

class RoutingDetailUpdateSerializer (ModelSerializer):
	class Meta:
		model = RoutingDetail
		fields =[
			'operation',
			'routing',
			# 'url',
			'position',
			'next_pass',
			'next_fail',
			'description',
			'category1',
			'category2',
			'user'
		]



