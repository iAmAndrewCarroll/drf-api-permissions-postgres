from django.urls import path
from .views import Lab32List, Lab32Detail

urlpatterns = [
    path("", Lab32List.as_view(), name="home"),
    path('<int:pk>', Lab32Detail.as_view(), name='lab32_detail'),
]