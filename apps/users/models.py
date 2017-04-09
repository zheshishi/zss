from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractBaseUser继承自己的字段，还可以增加自己的字段


class AuthUser(AbstractUser):
    address = models.CharField(max_length=130, default=u"", null=True, blank=True, verbose_name=u"地址")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号")
    balance = models.DecimalField('账户余额', default=0, max_digits=18, decimal_places=2, blank=True, null=True)
    wechatName = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"微信名")
    wechat = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"微信号")
    qq = models.CharField(max_length=13, null=True, blank=True, verbose_name=u"qq")
    alipay = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"alipay")
    bankName = models.CharField(choices=(
    ('zsbank', '招商银行'), ('zgbank', '中国银行'), ('jsbank', '建设银行'), ('gsbank', '工商银行'), ('nybank', '农业银行'),
    ('jtbank', '交通银行')), null=True, verbose_name=u"银行", max_length=9)
    bankID = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"银行")
    realname = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"真名")
    tags = models.CharField(max_length=200, null=True, blank=True, verbose_name=u"标签")
    image = models.ImageField(upload_to="image/Userimage/%Y/%m", default=u'image/default.png', max_length=100,
                              null=True)
    referrercode = models.CharField(max_length=40, null=True, blank=True, verbose_name=u"推荐号")
    remark = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"备注")

    class Meta:
        db_table = 'auth_user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # USERNAME_FIELD = 'username'
    def __unicode__(self):
        return self.username


class AuthPlatformUser(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)
    platform = models.CharField(max_length=20, blank=True, null=True)
    openid = models.CharField(max_length=200, blank=True, null=True)
    unionid = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.CharField(max_length=200, blank=True, null=True)
    refresh_token = models.CharField(max_length=200, blank=True, null=True)
    expiretime = models.DateTimeField(blank=True, null=True)
    profileurl = models.CharField(max_length=200, blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'auth_platform_user'


class buyscore(models.Model):
    user = models.ForeignKey(AuthUser, verbose_name=u'用户')
    scoregood = models.IntegerField(default='0', verbose_name=u'好评数')
    scoremiddle = models.IntegerField(default='0', verbose_name=u'中评数')
    scorepoor = models.IntegerField(default='0', verbose_name=u'差评数')

    class Meta:
        verbose_name = u'买家好评'
        verbose_name_plural = verbose_name


class sellscore(models.Model):
    user = models.ForeignKey(AuthUser, verbose_name=u'用户')
    scoregood = models.IntegerField(default='0', verbose_name=u'好评数')
    scoremiddle = models.IntegerField(default='0', verbose_name=u'中评数')
    scorepoor = models.IntegerField(default='0', verbose_name=u'差评数')

    class Meta:
        verbose_name = u'卖家好评'
        verbose_name_plural = verbose_name
