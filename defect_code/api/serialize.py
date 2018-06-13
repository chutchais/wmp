from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from defect_code.models import DefectCode


defect_code_url = HyperlinkedIdentityField(
		view_name='defectcode-api:detail',
		lookup_field='slug'
		)

class DefectCodeListSerializer(ModelSerializer):
	url = defect_code_url
	# routing 	= RoutingListSerializer(read_only=True)
	class Meta:
		model = DefectCode
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'description',
			'url',
			'slug'
		]

class DefectCodeDetailSerializer(ModelSerializer):

	class Meta:
		model = DefectCode
		fields ='__all__'


class DefectCodeCreateSerializer (ModelSerializer):
	class Meta:
		model = DefectCode
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2'
		]

class DefectCodeUpdateSerializer (ModelSerializer):
	class Meta:
		model = DefectCode
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2'
		]



