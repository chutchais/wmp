from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from rest_framework import serializers


from routing.models import Routing
from routing_detail.api.serialize import RoutingDetailListSerializer
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
		# exclude = ('users',)
		# fields ='__all__'
		# depth = 1
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
	# details =  RoutingDetailListSerializer()
	# operations = serializers.StringRelatedField(many=True)
	# operations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# operations = serializers.HyperlinkedRelatedField(
	# 			        many=True,
	# 			        read_only=True,
	# 			        view_name='routing-api:detail'
	# 			    )
	# operations = serializers.SlugRelatedField(
 #        many=True,
 #        read_only=True,
 #        slug_field='slug'
 #     )
	operations = RoutingDetailListSerializer(many=True, read_only=True)
	class Meta:
		model = Routing
		# fields ='__all__'
		fields =[
			'name',
			'title',
			# 'url',
			# 'details',
			'description',
			'category1',
			'category2',
			'user',
			'operations'
		]

class RoutingCreateSerializer (ModelSerializer):
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



