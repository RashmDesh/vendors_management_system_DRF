
from django.urls import path
from  . import views

urlpatterns = [
    path('vendors/',views.VendoreListApiView.as_view()),
    path('vendors/<int:vendore_id>/',views.VendoreDetailApiView.as_view())
]
