from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from bom.models import Bom
from bom_detail.api.serialize import BomDetailListSerializer
# from vessel.api.serialize import VesselSerializer

bom_detail_url=HyperlinkedIdentityField(
		view_name='bom-api:detail',
		lookup_field='slug'
		)





class BomListSerializer(ModelSerializer):
	url = bom_detail_url
	# shipper = ShipperSerializer(allow_null=True)
	
	class Meta:
		model = Bom
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

class BomDetailSerializer(ModelSerializer):
	parts = BomDetailListSerializer(many=True, read_only=True)
	class Meta:
		model = Bom
		fields ='__all__'


class BomCreateSerializer (ModelSerializer):
	class Meta:
		model = Bom
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class BomUpdateSerializer (ModelSerializer):
	class Meta:
		model = Bom
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



