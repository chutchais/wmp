from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from item_list.models import ItemList
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

itemlist_detail_url=HyperlinkedIdentityField(
		view_name='item_list-api:detail',
		lookup_field='slug'
		)





class ItemListListSerializer(ModelSerializer):
	url = itemlist_detail_url
	class Meta:
		model = ItemList
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'value',
			'default',
			'ordered',
			'user',
			'url',
			'status'
		]

class ItemListDetailSerializer(ModelSerializer):
	class Meta:
		model = ItemList
		fields ='__all__'

class ItemListCreateSerializer (ModelSerializer):
	class Meta:
		model = ItemList
		fields =[
			'name',
			'title',
			'user'
		]

class ItemListUpdateSerializer (ModelSerializer):
	class Meta:
		model = ItemList
		fields =[
			'name',
			'title',
			'user'
		]



