from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import Product
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

product_detail_url=HyperlinkedIdentityField(
		view_name='product-api:detail',
		lookup_field='slug'
		)





class ProductListSerializer(ModelSerializer):
	url = product_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Product
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class ProductDetailSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields ='__all__'

class ProductCreateSerializer (ModelSerializer):
	class Meta:
		model = Product
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class ProductUpdateSerializer (ModelSerializer):
	class Meta:
		model = Product
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



