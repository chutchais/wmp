from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from bom_detail.models import Bom_Detail


bomdetail_detail_url=HyperlinkedIdentityField(
		view_name='bom_detail-api:detail',
		lookup_field='slug'
		)





class BomDetailListSerializer(ModelSerializer):
	url = bomdetail_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	# vessel = VesselSerializer()
	class Meta:
		model = Bom_Detail
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
		model = Bom_Detail
		fields ='__all__'

class BomDetailCreateSerializer (ModelSerializer):
	class Meta:
		model = Bom_Detail
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
		model = Bom_Detail
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



