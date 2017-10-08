from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import ItemList
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

itemlist_detail_url=HyperlinkedIdentityField(
		view_name='itemlist-api:detail',
		lookup_field='slug'
		)





class ItemListListSerializer(ModelSerializer):
	url = itemlist_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
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
			'description',
			'user'
		]

class ItemListUpdateSerializer (ModelSerializer):
	class Meta:
		model = ItemList
		fields =[
			'name',
			'title',
			'description',
			'user'
		]



