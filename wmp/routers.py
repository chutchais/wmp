from rest_framework import routers

from bom.api.viewsets import BomViewSet,BomDetailViewSet,BomAlternateViewSet
from item.api.viewsets import ItemViewSet,ItemListViewSet
from operation.api.viewsets import OperationViewSet
from parameter.api.viewsets import ParameterViewSet
from product.api.viewsets import ProductViewSet
from user_profile.api.viewsets import ProfileViewSet
from routing.api.viewsets import RoutingViewSet,RoutingDetailViewSet,RoutingDetailNextViewSet
from snippet.api.viewsets import SnippetViewSet
from workorder.api.viewsets import WorkorderViewSet

router = routers.DefaultRouter()
router.register(r'bom', BomViewSet)
router.register(r'bom-detail', BomDetailViewSet)
router.register(r'bom-alternate', BomAlternateViewSet)
router.register(r'item', ItemViewSet)
router.register(r'item-list', ItemListViewSet)
router.register(r'parameter', ParameterViewSet)
router.register(r'operation', OperationViewSet)
router.register(r'product', ProductViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'routing', RoutingViewSet)
router.register(r'routing-detail', RoutingDetailViewSet)
router.register(r'routing-detail-next', RoutingDetailNextViewSet)
router.register(r'snippet', SnippetViewSet)
router.register(r'workorder', WorkorderViewSet)