from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path("site/", include("site_app.urls")),
    path('frontend/', include("frontend.urls")),
    path('api/demo/', include("demo_api.urls")),
    path('api/site/', include("site_app.api_urls")),
]

if not settings.TESTING:
    urlpatterns.extend(
        debug_toolbar_urls(),
    )
