#-*- coding: UTF-8 -*-
from django.contrib import admin
from .models import buyscore, sellscore, AuthUser
# Register your models here.


admin.site.register(AuthUser)
admin.site.register(buyscore)
admin.site.register(sellscore)
