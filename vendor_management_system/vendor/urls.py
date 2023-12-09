
from django.urls import path
from  . import views

urlpatterns = [
    path('vendors/',views.VendoreListApiView.as_view())
]
