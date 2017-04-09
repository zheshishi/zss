from datetime import datetime

from django.db import models

from apps.users.models import AuthUser
from libs.utils.string_extension import get_uuid, get_formattime

PLATFORM = (
    ('taobao', '淘宝'),
    ('jd', '京东')
)


class Shop(models.Model):
    id = models.CharField('id', max_length=32, default=get_uuid, primary_key=True)
    seller = models.ForeignKey(AuthUser, verbose_name='用户', null=True)
    shopname = models.CharField('店铺名称', max_length=50, null=True)
    shopkeepername = models.CharField('掌柜名称', max_length=50, null=True)
    platform = models.CharField('店铺平台', choices=PLATFORM, max_length=20, null=True)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'shops'
        verbose_name = '店铺名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shopname

    def to_dict(self):
        return {
            'id': self.id,
            'shopname': self.shopname,
            'shopkeepername': self.shopkeepername,
            'platform': self.platform,
            'add_time': get_formattime(self.add_time)
        }


class Goods(models.Model):
    id = models.CharField('id', max_length=32, default=get_uuid, primary_key=True)
    seller = models.ForeignKey(AuthUser, verbose_name='商家', null=True)
    shop = models.ForeignKey(Shop, verbose_name='所属店铺', null=True)
    name = models.CharField('商品名称', max_length=100, null=True)
    pgoods_id = models.CharField('平台商品id', max_length=50, null=True)
    platform = models.CharField('平台', max_length=50, null=True)
    sendaddress = models.CharField('发货地', max_length=50, null=True)
    image1 = models.CharField(max_length=100, null=True)
    image2 = models.ImageField(max_length=100, null=True)
    image3 = models.ImageField(max_length=100, null=True)
    keyword1 = models.CharField('关键词1', max_length=50, null=True)
    price1 = models.FloatField('价格1', max_length=50, null=True)
    remark1 = models.CharField('备注1', max_length=50, null=True)
    keyword2 = models.CharField('关键词2', max_length=50, null=True)
    price2 = models.FloatField('价格2', max_length=50, null=True)
    remark2 = models.CharField('备注2', max_length=50, null=True)
    keyword3 = models.CharField('关键词3', max_length=50, null=True)
    price3 = models.FloatField('价格3', max_length=50, null=True)
    remark3 = models.CharField('备注3', max_length=50, null=True)
    keyword4 = models.CharField('关键词4', max_length=50, null=True)
    price4 = models.FloatField('价格4', max_length=50, null=True)
    remark4 = models.CharField('备注4', max_length=50, null=True)
    keywor5 = models.CharField('关键词5', max_length=50, null=True)
    price5 = models.FloatField('价格5', max_length=50, null=True)
    remark5 = models.CharField('备注5', max_length=50, null=True)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def to_dict(self):
        return {
            'id': self.id,
            'shop_id': self.shop.id,
            'shop_name': self.shop.shopname,
            'name': self.name,
            'price1': self.price1,
            'pgoods_id': self.pgoods_id,
            'platform': self.platform,
            'add_time': get_formattime(self.add_time)
        }
