from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usd_to_egp/', views.usd_to_egp, name='usd-to-egp'),
    path('get_price/', views.get_price, name='live-indomie-price'),
    # pssst, yes, you'll write code here :)
]
