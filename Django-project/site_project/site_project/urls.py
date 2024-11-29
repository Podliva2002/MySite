from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from site_app.api_views import UserViewSet, CurrentUserView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path("site/", include("site_app.urls")),
    path('api/demo/', include("demo_api.urls")),
    path('api/site/', include("site_app.api_urls")),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/current-user/', CurrentUserView.as_view(), name='current-user'),
]

if not settings.TESTING:
    urlpatterns.extend(
        debug_toolbar_urls(),
    )
