from rest_framework import routers

from product.api.viewsets import ProductViewSet
from user_profile.api.viewsets import ProfileViewSet
from operation.api.viewsets import OperationViewSet

router = routers.DefaultRouter()
router.register(r'operation', OperationViewSet)
router.register(r'product', ProductViewSet)
router.register(r'profile', ProfileViewSet)