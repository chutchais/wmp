from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from item.models import Item,ItemList



class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['name','title','description',
				'category1','category2','url']

class ItemListSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemList
		fields = ['name','item','value','default','title','description',
		'category1','category2','url']

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField,
# 	StringRelatedField,
# 	SlugRelatedField,
# 	HyperlinkedModelSerializer,
# 	ReadOnlyField
# 	)
# # from rest_framework.serializers import (
# # 	ModelSerializer,
# # 	HyperlinkedIdentityField,
# # 	SerializerMethodField,
# # 	HyperlinkedModelSerializer,
# # 	ReadOnlyField
# # 	)


# from item.models import Item
# from item_list.api.serialize import ItemListListSerializer
# # from vessel.api.serialize import VesselSerializer

# item_detail_url=HyperlinkedIdentityField(
# 		view_name='item-api:detail',
# 		lookup_field='slug'
# 		)





# class ItemListSerializer(ModelSerializer):
# 	url = item_detail_url
# 	# shipper = ShipperSerializer(allow_null=True)
# 	# lists = ItemListListSerializer(many=True, read_only=True)
# 	# lists = StringRelatedField(many=True)


# 	class Meta:
# 		model = Item
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'slug',
# 			'product',
# 			'description',
# 			'input_type',
# 			'default_value',
# 			'regexp',
# 			'url',
# 			'status'
# 		]

# class ItemDetailSerializer(ModelSerializer):
# 	lists = ItemListListSerializer(many=True, read_only=True)
# 	snippet 	 = SlugRelatedField (many=False,read_only=True,slug_field='slug')
# 	url = item_detail_url
# 	class Meta:
# 		model = Item
# 		fields ='__all__'
# 		# fields =[
# 		# 	'name',
# 		# 	'title',
# 		# 	'product',
# 		# 	'description',
# 		# 	'input_type',
# 		# 	'lists',
# 		# 	'default_value',
# 		# 	'regexp',
# 		# 	'user',
# 		# 	'snippet',
# 		# 	'expected_return',
# 		# 	'url'
# 		# ]

# class ItemCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Item
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]

# class ItemUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Item
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]



