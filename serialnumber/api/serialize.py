from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import SerialNumber
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer
from workorder.api.serialize import WorkOrderListSerializer

serialnumber_detail_url=HyperlinkedIdentityField(
		view_name='serialnumber-api:detail',
		lookup_field='slug'
		)





class SerialNumberListSerializer(ModelSerializer):
	url = serialnumber_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	# workorder= WorkOrderListSerializer()
	class Meta:
		model = SerialNumber
		# fields ='__all__'
		fields =[
			'number',
			'slug',
			'workorder',
			'url',
			'wip',
			'routing',
			'current_operation',
			'last_operation'
		]
		depth =3

class SerialNumberDetailSerializer(ModelSerializer):
	class Meta:
		model = SerialNumber
		fields ='__all__'

class SerialNumberCreateSerializer (ModelSerializer):
	class Meta:
		model = SerialNumber
		fields =[
			'number',
			'workorder',
			'description',
			'category1',
			'category2',
			'routing',
			'current_operation',
			'user'
		]

class SerialNumberUpdateSerializer (ModelSerializer):
	class Meta:
		model = SerialNumber
		fields =[
			'number',
			'workorder',
			'description',
			'category1',
			'category2',
			'routing',
			'current_operation',
			'user'
		]



