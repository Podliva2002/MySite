from .views import (
    PingApiView,
)

from django.urls import path

app_name = 'demo_api'

urlpatterns = [
    path("ping/", PingApiView.as_view(), name="ping"),

]
