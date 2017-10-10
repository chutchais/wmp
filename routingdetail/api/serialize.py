from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	SlugRelatedField
	)


from shopfloor.models import RoutingDetail
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

from parameter.api.serialize import ParameterListSerializer

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
			'slug'
		]

class RoutingDetailDetailSerializer(ModelSerializer):
	parameter = ParameterListSerializer (many=True, read_only=True)
	accept_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	except_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	next_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')

	# parameter = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# accept_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# except_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# next_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')

	class Meta:
		model = RoutingDetail
		fields ='__all__'
		fields =[
			'routing',
			'operation',
			'parameter',
			'accept_code',
			'except_code',
			'next_code'
		]

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



