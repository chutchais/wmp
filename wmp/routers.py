from rest_framework import routers

from bom.api.viewsets import BomViewSet,BomDetailViewSet,BomAlternateViewSet
from item.api.viewsets import ItemViewSet,ItemListViewSet
from operation.api.viewsets import OperationViewSet
from parameter.api.viewsets import ParameterViewSet
from product.api.viewsets import ProductViewSet
from user_profile.api.viewsets import ProfileViewSet
from routing.api.viewsets import (RoutingViewSet,RoutingDetailViewSet,
                                RoutingDetailNextViewSet,RoutingDetailAcceptViewSet,
                                RoutingDetailRejectViewSet,RoutingDetailHookViewSet,
                                RoutingDetailParameterViewSet)
from snippet.api.viewsets import SnippetViewSet
from serialnumber.api.viewsets import SerialNumberViewSet
from workorder.api.viewsets import WorkorderViewSet
from performing.api.viewsets import PerformingViewSet
from parametric.api.viewsets import ParametricViewSet

router = routers.DefaultRouter()
router.register(r'bom', BomViewSet)
router.register(r'bom-detail', BomDetailViewSet)
router.register(r'bom-alternate', BomAlternateViewSet)
router.register(r'item', ItemViewSet)
router.register(r'item-list', ItemListViewSet)
router.register(r'parameter', ParameterViewSet)
router.register(r'operation', OperationViewSet)
router.register(r'parametric', ParametricViewSet)
router.register(r'performing', PerformingViewSet)
router.register(r'product', ProductViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'routing', RoutingViewSet)
router.register(r'routing-detail', RoutingDetailViewSet)
router.register(r'routing-detail-next', RoutingDetailNextViewSet)
router.register(r'routing-detail-accept', RoutingDetailAcceptViewSet)
router.register(r'routing-detail-reject', RoutingDetailRejectViewSet)
router.register(r'routing-detail-hook', RoutingDetailHookViewSet)
router.register(r'routing-detail-parameter', RoutingDetailParameterViewSet)
router.register(r'snippet', SnippetViewSet),
router.register(r'serialnumber', SerialNumberViewSet),
router.register(r'workorder', WorkorderViewSet)