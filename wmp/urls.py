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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Page
    url(r'^bom/',include('bom.urls',namespace='bom')),
    url(r'^bom-detail/',include('bom_detail.urls',namespace='bom_detail')),
    url(r'^item/',include('item.urls',namespace='item')),
    url(r'^item-list/',include('item_list.urls',namespace='item-list')),
    url(r'^operation/',include('operation.urls',namespace='operation')),
    url(r'^parameter/',include('parameter.urls',namespace='parameter')),
    url(r'^performing/',include('performing.urls',namespace='performing')),
    url(r'^product/',include('product.urls',namespace='product')),
    url(r'^routing/',include('routing.urls',namespace='routing')),
    url(r'^routing-accept/',include('routing_accept.urls',namespace='routing-accept')),
    url(r'^routing-detail/',include('routing_detail.urls',namespace='routing-detail')),
    url(r'^routing-next/',include('routing_next.urls',namespace='routing-next')),
    url(r'^routing-reject/',include('routing_reject.urls',namespace='routing-reject')),
    url(r'^serialnumber/',include('serialnumber.urls',namespace='serialnumber')),
    url(r'^snippet/',include('snippet.urls',namespace='snippet')),
    url(r'^workorder/',include('workorder.urls',namespace='workorder')),
    
    # API
    url(r'api/bom/', include("bom.api.urls", namespace='bom-api')),
    url(r'api/bom-detail/', include("bom_detail.api.urls", namespace='bom_detail-api')),
    url(r'api/item/', include("item.api.urls", namespace='item-api')),
    url(r'api/item-list/', include("item_list.api.urls", namespace='item_list-api')),

    url(r'api/routing/', include("routing.api.urls", namespace='routing-api')),
    url(r'api/routing-accept/', include("routing_accept.api.urls", namespace='routing_accept-api')),
    url(r'api/routing-next/', include("routing_next.api.urls", namespace='routing_next-api')),
    url(r'api/routing-reject/', include("routing_reject.api.urls", namespace='routing_reject-api')),

    url(r'api/performing/', include("performing.api.urls", namespace='performing-api')),
    url(r'api/serialnumber/', include("serialnumber.api.urls", namespace='serialnumber-api')),
    url(r'api/workorder/', include("workorder.api.urls", namespace='workorder-api')),
    url(r'api/product/', include("product.api.urls", namespace='product-api')),
    url(r'api/operation/', include("operation.api.urls", namespace='operation-api')),
    
    url(r'api/routing-detail/', include("routing_detail.api.urls", namespace='routing_detail-api')),
    
    
    url(r'api/parameter/', include("parameter.api.urls", namespace='parameter-api')),
    
    url(r'api/snippet/', include("snippet.api.urls", namespace='snippet-api')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)