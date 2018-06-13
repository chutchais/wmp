from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from symptom_code.models import SymptomCode


symptom_code_url = HyperlinkedIdentityField(
		view_name='symptomcode-api:detail',
		lookup_field='slug'
		)

class SymptomCodeListSerializer(ModelSerializer):
	url = symptom_code_url
	# routing 	= RoutingListSerializer(read_only=True)
	class Meta:
		model = SymptomCode
		# fields ='__all__'
		fields =[
			'name',
			'title',
			'description',
			'url',
			'slug'
		]

class SymptomCodeDetailSerializer(ModelSerializer):

	class Meta:
		model = SymptomCode
		fields ='__all__'


class SymptomCodeCreateSerializer (ModelSerializer):
	class Meta:
		model = SymptomCode
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2'
		]

class SymptomCodeUpdateSerializer (ModelSerializer):
	class Meta:
		model = SymptomCode
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2'
		]



