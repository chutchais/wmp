from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import Parameter
from item.api.serialize import ItemListSerializer
# from vessel.api.serialize import VesselSerializer

parameter_detail_url=HyperlinkedIdentityField(
		view_name='parameter-api:detail',
		lookup_field='slug'
		)





class ParameterListSerializer(ModelSerializer):
	url = parameter_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Parameter
		fields =[
			'name',
			'title',
			'item_count',
			'description',
			'user',
			'url'
		]


class ParameterDetailSerializer(ModelSerializer):
	items = ItemListSerializer(read_only=True, many=True)
	class Meta:
		model = Parameter
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'items',
			'description',
			'items',
			'user'
		]
class ParameterCreateSerializer (ModelSerializer):
	class Meta:
		model = Parameter
		fields =[
			'name',
			'title',
			'description',
			'user'
		]

class ParameterUpdateSerializer (ModelSerializer):
	class Meta:
		model = Parameter
		fields =[
			'name',
			'title',
			'description',
			'user'
		]



