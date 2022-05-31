"""soar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import seap.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from soar.views import EnvironmentViewSet, GroupViewSet, UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'environments', EnvironmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest/', include([
        path('soar/', include(router.urls)),
        path('seap/', include(seap.urls.router.urls)),
    ])),
    path(r'static/', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
