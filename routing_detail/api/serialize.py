from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	SlugRelatedField,
	HyperlinkedModelSerializer,
	ReadOnlyField
	)


from routing_detail.models import (	RoutingDetail,
									RoutingDetailNextSet)


from parameter.api.serialize import ParameterListSerializer

routingdetail_detail_url=HyperlinkedIdentityField(
		view_name='routing_detail-api:detail',
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

class RoutingDetailNextSetSerializer(HyperlinkedModelSerializer ):
	# name = ReadOnlyField(source='routingdetail.name')
	# title = ReadOnlyField(source='routingdetail.title')
	# description = ReadOnlyField(source='RoutingExcept.description')

	# 'url',
	# slug = SlugRelatedField(source='routingnext.slug')
	slug = SlugRelatedField(source='routingnext.snippet',many=False,read_only=True,slug_field='slug')
	class Meta:
		model = RoutingDetailNextSet
		fields = ['title','ordered','status','operation','slug']

class RoutingDetailDetailSerializer(ModelSerializer):
	# parameter = ParameterListSerializer (many=True, read_only=True)
	# accept_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# except_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# next_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')

	# parameter = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	accept_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	reject_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	parameter   = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	next_code = SlugRelatedField (many=True,read_only=True,slug_field='slug')
	# next_code =  RoutingDetailNextSetSerializer(source='routingdetailsets', many=True)
	class Meta:
		model = RoutingDetail
		fields ='__all__'
		# fields =[
		# 	'routing',
		# 	'operation',
		# 	'parameter',
		# 	'accept_code',
		# 	'reject_code',
		# 	'next_code',
		# 	'next_pass',
		# 	'next_fail'

		# ]
		# depth=1

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



