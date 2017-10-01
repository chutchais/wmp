from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField
	)


from shopfloor.models import Item
from itemlist.api.serialize import ItemListListSerializer
# from vessel.api.serialize import VesselSerializer

item_detail_url=HyperlinkedIdentityField(
		view_name='item-api:detail',
		lookup_field='slug'
		)





class ItemListSerializer(ModelSerializer):
	url = item_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	lists = ItemListListSerializer(many=True, read_only=True)
	# lists = StringRelatedField(many=True)

	class Meta:
		model = Item
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'product',
			'description',
			'input_type',
			'lists',
			'default_value',
			'regexp',
			'user',
			'url'
		]

class ItemDetailSerializer(ModelSerializer):
	# shipper = ShipperSerializer(allow_null=True)
	lists = ItemListListSerializer(many=True, read_only=True)
	# lists = StringRelatedField(many=True)

	class Meta:
		model = Item
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'product',
			'description',
			'input_type',
			'lists',
			'default_value',
			'regexp',
			'user',
		]

class ItemCreateSerializer (ModelSerializer):
	class Meta:
		model = Item
		fields =[
			'name',
			'title',
			'description',
			'user'
		]

class ItemUpdateSerializer (ModelSerializer):
	class Meta:
		model = Item
		fields =[
			'name',
			'title',
			'description',
			'user'
		]


