from rest_framework import routers

from bom.api.viewsets import BomViewSet,BomDetailViewSet,BomAlternateViewSet
from product.api.viewsets import ProductViewSet
from user_profile.api.viewsets import ProfileViewSet
from operation.api.viewsets import OperationViewSet
from workorder.api.viewsets import WorkorderViewSet

router = routers.DefaultRouter()
router.register(r'bom', BomViewSet)
router.register(r'bom-detail', BomDetailViewSet)
router.register(r'bom-alternate', BomAlternateViewSet)
router.register(r'operation', OperationViewSet)
router.register(r'product', ProductViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'workorder', WorkorderViewSet)