from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField
	)


from snippet.models import Snippet
# from itemlist.api.serialize import ItemListListSerializer
# from vessel.api.serialize import VesselSerializer

snippet_detail_url=HyperlinkedIdentityField(
		view_name='snippet-api:detail',
		lookup_field='slug'
		)





class SnippetListSerializer(ModelSerializer):
	url = snippet_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# lists = ItemListListSerializer(many=True, read_only=True)
	# lists = StringRelatedField(many=True)

	class Meta:
		model = Snippet
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user',
			'url'
		]

class SnippetDetailSerializer(ModelSerializer):
	# shipper = ShipperSerializer(allow_null=True)
	# lists = ItemListListSerializer(many=True, read_only=True)
	# lists = StringRelatedField(many=True)

	class Meta:
		model = Snippet
		fields ='__all__'
		

class SnippetCreateSerializer (ModelSerializer):
	class Meta:
		model = Snippet
		fields =[
			'name',
			'title',
			'description',
			'user'
		]

class SnippetUpdateSerializer (ModelSerializer):
	class Meta:
		model = Snippet
		fields =[
			'name',
			'title',
			'description',
			'user'
		]



