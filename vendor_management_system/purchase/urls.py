
from django.urls import path
from  purchase.views import PurchaseListApiView,PurchaseDetailApiView

urlpatterns = [
    path('api/purchase_orders/',PurchaseListApiView.as_view()),
    path('api/purchase_orders/<int:po_id>/',PurchaseDetailApiView.as_view())
]