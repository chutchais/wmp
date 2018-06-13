"""wmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Page
    url(r'^bom/',include(('bom.urls','bom'),namespace='bom')),
    url(r'^bom-detail/',include(('bom_detail.urls','bom_detail'),namespace='bom_detail')),
    url(r'^item/',include(('item.urls','item'),namespace='item')),
    url(r'^item-list/',include(('item_list.urls','item_list'),namespace='item-list')),
    url(r'^operation/',include(('operation.urls','operation'),namespace='operation')),
    url(r'^parameter/',include(('parameter.urls','parameter'),namespace='parameter')),
    url(r'^performing/',include(('performing.urls','performing'),namespace='performing')),
    url(r'^product/',include(('product.urls','product'),namespace='product')),
    url(r'^routing/',include(('routing.urls','routing'),namespace='routing')),
    url(r'^routing-accept/',include(('routing_accept.urls','routing_accept'),namespace='routing-accept')),
    url(r'^routing-detail/',include(('routing_detail.urls','routing_detail'),namespace='routing-detail')),
    url(r'^routing-next/',include(('routing_next.urls','routing_next'),namespace='routing-next')),
    url(r'^routing-reject/',include(('routing_reject.urls','routing_reject'),namespace='routing-reject')),
    url(r'^serialnumber/',include(('serialnumber.urls','serialnumber'),namespace='serialnumber')),
    url(r'^snippet/',include(('snippet.urls','snippet'),namespace='snippet')),
    url(r'^symptom-code/',include(('symptom_code.urls','symptom_code'),namespace='symptom-code')),
    url(r'^workorder/',include(('workorder.urls','workorder'),namespace='workorder')),
    
    # API
    url(r'api/bom/', include(('bom.api.urls','bom'), namespace='bom-api')),
    url(r'api/bom-detail/', include(("bom_detail.api.urls",'bom_detail'), namespace='bom_detail-api')),
    url(r'api/defectcode/', include(("defect_code.api.urls",'defectcode'), namespace='defectcode-api')),
    url(r'api/item/', include(("item.api.urls",'item'), namespace='item-api')),
    url(r'api/item-list/', include(("item_list.api.urls",'item_list'), namespace='item_list-api')),
    url(r'api/hook/', include(("hook.api.urls",'hook'), namespace='hook-api')),
    url(r'api/routing/', include(("routing.api.urls",'routing'), namespace='routing-api')),
    url(r'api/routing-accept/', include(("routing_accept.api.urls",'routing_accept'), namespace='routing_accept-api')),
    url(r'api/routing-next/', include(("routing_next.api.urls",'routing_next'), namespace='routing_next-api')),
    url(r'api/routing-reject/', include(("routing_reject.api.urls",'routing_reject'), namespace='routing_reject-api')),
    url(r'api/performing/', include(("performing.api.urls",'performing'), namespace='performing-api')),
    url(r'api/serialnumber/', include(("serialnumber.api.urls",'serialnumber'), namespace='serialnumber-api')),
    url(r'api/workorder/', include(("workorder.api.urls",'workorder'), namespace='workorder-api')),
    url(r'api/product/', include(("product.api.urls",'product'), namespace='product-api')),
    url(r'api/operation/', include(("operation.api.urls",'operation'), namespace='operation-api')), 
    url(r'api/routing-detail/', include(("routing_detail.api.urls",'routing_detail'), namespace='routing_detail-api')),
    url(r'api/parameter/', include(("parameter.api.urls",'parameter'), namespace='parameter-api')),
    url(r'api/snippet/', include(("snippet.api.urls",'snippet'), namespace='snippet-api')),
    url(r'api/symptomcode/', include(("symptom_code.api.urls",'snippet'), namespace='symptomcode-api')),
    url(r'api/users/', include(("user.api.urls",'user'), namespace='user-api')),

    #Restful Authentication
    url(r'^api-auth/', include('rest_framework.urls')),
    # Token
    url(r'^api/login/', include(('user.urls','user'),namespace='login')),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)