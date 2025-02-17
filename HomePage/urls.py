from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),]