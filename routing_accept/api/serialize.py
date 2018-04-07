from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from routing_accept.models import RoutingAccept
# from shiproutingper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

routing_accept_url=HyperlinkedIdentityField(
		view_name='routing_accept-api:detail',
		lookup_field='slug'
		)





class RoutingAcceptListSerializer(ModelSerializer):
	url = routing_accept_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = RoutingAccept
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

class RoutingAcceptDetailSerializer(ModelSerializer):
	class Meta:
		model = RoutingAccept
		fields ='__all__'

class RoutingAcceptCreateSerializer (ModelSerializer):
	class Meta:
		model = RoutingAccept
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


class RoutingAcceptUpdateSerializer (ModelSerializer):
	class Meta:
		model = RoutingAccept
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



