from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	SerializerMethodField
	)

from routing.models import (Routing,RoutingDetail,RoutingDetailNext,
							RoutingDetailNextSet,RoutingDetailAccept,RoutingDetailAcceptSet,
							RoutingDetailReject,RoutingDetailRejectSet)



class RoutingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routing
		fields = ['name','title','description',
				'category1','category2','url']

class RoutingDetailSerializer(serializers.ModelSerializer):
	accept_code = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailaccept-detail')
	reject_code = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailreject-detail')
	next_code   = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailnext-detail')
	class Meta:
		model = RoutingDetail
		fields =  ['operation','routing','position','title','description',
				'category1','category2','next_pass','next_fail',
				'accept_code','reject_code','next_code','status','url']



# Next Code Serialize
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
# ---------------------------

# Accept Serialize
class RoutingDetailAcceptSerializer(serializers.ModelSerializer):
	snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	class Meta:
		model = RoutingDetailAccept
		fields = ['name','title','description','slug',
				'category1','category2','status','snippet','url']

class RoutingDetailAcceptSetSerializer(serializers.ModelSerializer):
	routingnext = RoutingDetailAcceptSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailAcceptSet
		fields =  ['title','ordered','operation','routingnext','status']


# Reject Serialize
class RoutingDetailRejectSerializer(serializers.ModelSerializer):
	snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	class Meta:
		model = RoutingDetailReject
		fields = ['name','title','description','slug',
				'category1','category2','status','snippet','url']

class RoutingDetailRejectSetSerializer(serializers.ModelSerializer):
	routingnext = RoutingDetailRejectSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailRejectSet
		fields =  ['title','ordered','operation','routingnext','status']
