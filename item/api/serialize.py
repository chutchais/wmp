from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField,
	SlugRelatedField,
	HyperlinkedModelSerializer,
	ReadOnlyField
	)
# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField,
# 	HyperlinkedModelSerializer,
# 	ReadOnlyField
# 	)


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
			'url',
			'status'
		]

class ItemDetailSerializer(ModelSerializer):
	# shipper = ShipperSerializer(allow_null=True)
	lists = ItemListListSerializer(many=True, read_only=True)
	# lists = StringRelatedField(many=True)
	snippet =SlugRelatedField (many=False,read_only=True,slug_field='slug')

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
			'snippet',
			'expected_return'
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



