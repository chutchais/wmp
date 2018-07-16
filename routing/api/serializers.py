from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	SerializerMethodField
	)

from routing.models import Routing,RoutingDetail,RoutingDetailNext,RoutingDetailNextSet



class RoutingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routing
		fields = ['name','title','description',
				'category1','category2','url']

class RoutingDetailSerializer(serializers.ModelSerializer):
	next_code = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailnext-detail')
	class Meta:
		model = RoutingDetail
		fields =  ['operation','routing','position','title','description',
				'category1','category2','next_pass','next_fail','next_code','status','url']

class RoutingDetailNextSerializer(serializers.ModelSerializer):
	snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	class Meta:
		model = RoutingDetailNext
		fields = ['name','title','description','slug',
				'category1','category2','status','snippet','url']


class RoutingNextSetSerializer(serializers.ModelSerializer):
	routingnext = RoutingDetailNextSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailNextSet
		fields =  ['title','ordered','operation','routingnext','status']




# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)

# from rest_framework import serializers


# from routing.models import Routing
# from routing_detail.api.serialize import RoutingDetailListSerializer
# # from vessel.api.serialize import VesselSerializer

# routing_detail_url=HyperlinkedIdentityField(
# 		view_name='routing-api:detail',
# 		lookup_field='slug'
# 		)





# class RoutingListSerializer(ModelSerializer):
# 	url = routing_detail_url
# 	class Meta:
# 		model = Routing
# 		# exclude = ('users',)
# 		# fields ='__all__'
# 		# depth = 1
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'slug'
# 		]

# class RoutingDetailSerializer(ModelSerializer):
# 	# details =  RoutingDetailListSerializer()
# 	# operations = serializers.StringRelatedField(many=True)
# 	# operations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
# 	# operations = serializers.HyperlinkedRelatedField(
# 	# 			        many=True,
# 	# 			        read_only=True,
# 	# 			        view_name='routing-api:detail'
# 	# 			    )
# 	# operations = serializers.SlugRelatedField(
#  #        many=True,
#  #        read_only=True,
#  #        slug_field='slug'
#  #     )
# 	# operations = RoutingDetailListSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Routing
# 		fields ='__all__'
# 		# fields =[
# 		# 	'name',
# 		# 	'title',
# 		# 	# 'url',
# 		# 	# 'details',
# 		# 	'description',
# 		# 	'category1',
# 		# 	'category2',
# 		# 	'user',
# 		# 	'operations'
# 		# ]

# class RoutingCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Routing
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]

# class RoutingUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Routing
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]



