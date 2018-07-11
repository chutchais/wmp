from rest_framework import routers
# from company.api.viewsets import CompanyViewSet
# from department.api.viewsets import DepartmentViewSet,SectionViewSet
# from employee.api.viewsets import EmployeeViewSet,PositionViewSet

from user_profile.api.viewsets import ProfileViewSet
from operation.api.viewsets import OperationViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'operation', OperationViewSet)
# router.register(r'section', SectionViewSet)
# router.register(r'position', PositionViewSet)
# router.register(r'employee', EmployeeViewSet)