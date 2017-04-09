# coding:utf-8
from django.conf.urls import url

from apps.wechat.views import activity

urlpatterns = [
    url(r'', activity.ActivityView.as_view(), name='activity')
]
