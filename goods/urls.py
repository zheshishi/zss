# coding:utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^index/', views.GoodsManagerView.as_view(), name='index'),
    url(r'^add/$', views.GoodsCreateView.as_view(), name='add'),
    url(r'^edit/$', views.GoodsEditView.as_view(), name='edit'),
    url(r'^delete/$', views.delete_goods, name='delete'),

    url(r'^shop/index/', views.ShopManagerViews.as_view(), name='shop_index'),
    url(r'^shop/add/$', views.ShopCreateView.as_view(), name='shop_add'),
    url(r'^shop/edit/$', views.ShopEditView.as_view(), name='shop_edit'),
    url(r'^shop/delete/$', views.delete_shops, name='shop_delete'),

    url(r'^getgooods/$', views.get_goods, name='getgoods'),
    url(r'^getshops/$', views.get_shops, name='getshops')
]
