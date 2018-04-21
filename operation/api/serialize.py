from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from operation.models import Operation


operation_detail_url=HyperlinkedIdentityField(
		view_name='operation-api:detail',
		lookup_field='slug'
		)

class OperationListSerializer(ModelSerializer):
	url = operation_detail_url
	class Meta:
		model = Operation
		fields =[
			'name',
			'title',
			'url',
			'slug'
		]

class OperationDetailSerializer(ModelSerializer):
	class Meta:
		model = Operation
		fields ='__all__'

class OperationCreateSerializer (ModelSerializer):
	class Meta:
		model = Operation
		fields =[
			'name',
			'title',
			'url',
			'description',
			'category1',
			'category2',
			'user'
		]

class OperationUpdateSerializer (ModelSerializer):
	class Meta:
		model = Operation
		fields =[
			'name',
			'title',
			'description',
			'category1',
			'category2',
			'user'
		]



