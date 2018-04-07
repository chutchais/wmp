from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from routing_reject.models import RoutingReject
# from shiproutingper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

routing_reject_url=HyperlinkedIdentityField(
		view_name='routing_reject-api:detail',
		lookup_field='slug'
		)





class RoutingRejectListSerializer(ModelSerializer):
	url = routing_reject_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = RoutingReject
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

class RoutingRejectDetailSerializer(ModelSerializer):
	class Meta:
		model = RoutingReject
		fields ='__all__'

class RoutingRejectCreateSerializer (ModelSerializer):
	class Meta:
		model = RoutingReject
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


class RoutingRejectUpdateSerializer (ModelSerializer):
	class Meta:
		model = RoutingReject
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



