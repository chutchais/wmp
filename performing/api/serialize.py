from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from performing.models import Performing
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

performing_detail_url=HyperlinkedIdentityField(
		view_name='performing-api:detail',
		lookup_field='slug'
		)





class PerformingListSerializer(ModelSerializer):
	url = performing_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Performing
		# fields ='__all__'
		fields =[
			'sn',
			'operation',
			'url',
			'start_time',
			'stop_time',
			'result',
			'remark',
			'user'
		]

class PerformingDetailSerializer(ModelSerializer):
	# url = booking_detail_url
	class Meta:
		model = Performing
		fields = '__all__'
		# fields =[
		# 	'sn',
		# 	'operation',
		# 	'start_time',
		# 	'stop_time',
		# 	'result',
		# 	'remark',
		# 	'user'
		# ]

class PerformingCreateSerializer (ModelSerializer):
	class Meta:
		model = Performing
		fields =[
			'sn',
			'operation',
			'start_time',
			'stop_time',
			'result',
			'remark'
		]

class PerformingUpdateSerializer (ModelSerializer):
	class Meta:
		model = Performing
		fields =[
			'sn',
			'operation',
			'start_time',
			'stop_time',
			'result',
			'remark',
			'user'
		]



