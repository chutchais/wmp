from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from shopfloor.models import BomDetail
# from shipper.api.serialize import ShipperSerializer
# from vessel.api.serialize import VesselSerializer

bomdetail_detail_url=HyperlinkedIdentityField(
		view_name='bomdetail-api:detail',
		lookup_field='slug'
		)





class BomDetailListSerializer(ModelSerializer):
	url = bomdetail_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = BomDetail
		# fields ='__all__'
		fields =[
			'rd',
			'pn',
			'alt_pn',
			'bom',
			'url',
			'customer_pn',
		]

class BomDetailDetailSerializer(ModelSerializer):
	class Meta:
		model = BomDetail
		fields ='__all__'

class BomDetailCreateSerializer (ModelSerializer):
	class Meta:
		model = BomDetail
		fields =[
			'rd',
			'pn',
			'alt_pn',
			'bom'
			'url',
			'customer_pn',
			'description',
			'category1',
			'category2',
			'user'
		]

class BomDetailUpdateSerializer (ModelSerializer):
	class Meta:
		model = BomDetail
		fields =[
			'rd',
			'pn',
			'alt_pn',
			'customer_pn',
			'description',
			'category1',
			'category2',
			'user'
		]



