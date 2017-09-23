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
    url(r'api/performing/', include("performing.api.urls", namespace='performing-api')),
    url(r'api/serialnumber/', include("serialnumber.api.urls", namespace='serialnumber-api')),
    url(r'api/workorder/', include("workorder.api.urls", namespace='workorder-api')),
    url(r'api/product/', include("product.api.urls", namespace='product-api')),
    url(r'api/operation/', include("operation.api.urls", namespace='operation-api')),
    url(r'api/routing/', include("routing.api.urls", namespace='routing-api')),
    url(r'api/routing-detail/', include("routingdetail.api.urls", namespace='routingdetail-api')),
    url(r'api/bom/', include("bom.api.urls", namespace='bom-api')),
    url(r'api/bom-detail/', include("bomdetail.api.urls", namespace='bomdetail-api')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)