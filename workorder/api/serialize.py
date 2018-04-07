from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from workorder.models import WorkOrder

workorder_detail_url=HyperlinkedIdentityField(
		view_name='workorder-api:detail',
		lookup_field='slug'
		)





class WorkOrderListSerializer(ModelSerializer):
	url = workorder_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = WorkOrder
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'url',
			'description',
			'product',
			'routing',
			'category1',
			'category2',
			'user',
			'slug'
		]

class WorkOrderDetailSerializer(ModelSerializer):
	class Meta:
		model = WorkOrder
		fields ='__all__'

class WorkOrderCreateSerializer (ModelSerializer):
	class Meta:
		model = WorkOrder
		fields =[
			'name',
			'title',
			'url',
			'description',
			'product',
			'routing'
			'category1',
			'category2',
			'user'
		]

class WorkOrderUpdateSerializer (ModelSerializer):
	class Meta:
		model = WorkOrder
		fields =[
			'name',
			'title',
			'description',
			'product',
			'routing',
			'category1',
			'category2',
			'user'
		]



