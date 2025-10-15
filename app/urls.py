from django.urls import path

from .views import dashboard, order, store

urlpatterns = [
    path("", dashboard.DashboardView.as_view(), name="dashboard"),
    # store
    path("stores", store.StoreListView.as_view(), name="stores"),
    path("stores/create", store.StoreCreateView.as_view(), name="store-create"),
    path("stores/<int:pk>/edit/", store.StoreUpdateView.as_view(), name="store_edit"),
    path(
        "stores/<int:pk>/delete/", store.StoreDeleteView.as_view(), name="store_delete"
    ),
    # oders
    path("delivery/create", order.OrderCreateView.as_view(), name="delivery-create"),
    path("delivery/api", order.OrderAPIView.as_view(), name="delivery-api"),
    path("delivery/<str:state>", order.OrderView.as_view(), name="delivery"),
]
