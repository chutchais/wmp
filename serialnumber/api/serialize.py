from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import SerialNumber
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

serialnumber_detail_url=HyperlinkedIdentityField(
		view_name='serialnumber-api:detail',
		lookup_field='slug'
		)





class SerialNumberListSerializer(ModelSerializer):
	url = serialnumber_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = SerialNumber
		# fields ='__all__'
		fields =[
			'number',
			'workorder',
			'url',
			'description',
			'category1',
			'category2',
			'routing',
			'current_operation',
			'user'
		]

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



