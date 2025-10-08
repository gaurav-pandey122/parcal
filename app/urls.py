from django.urls import path

from .views import dashboard

urlpatterns = [
    path("", dashboard.DashboardView.as_view(), name="dashboard"),
    path("delivery/<str:status>", dashboard.DeliveryView.as_view(), name="delivery"),
]
