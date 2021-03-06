# coding:utf-8
import os
from datetime import datetime, timedelta
from django import forms
from apps.orders.models import Order
from apps.cashback.models import CashbackTask, Cashback
from apps.users.models import AuthUser

img_extensions = ['.png', '.jpg', '.bmp']


class ActivityForm(forms.Form):
    id = forms.CharField()
    orderno = forms.CharField(error_messages={'required': '请填写订单号'})
    commentpic = forms.FileField()
    showpic1 = forms.FileField(required=False)
    showpic2 = forms.FileField(required=False)
    wechat = forms.CharField(required=False)
    alipay = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.task = None
        self.order = None
        super(ActivityForm, self).__init__(*args, **kwargs)

    def clean_commentpic(self):
        file = self.cleaned_data.get('commentpic')
        if not check_file_extension(file, img_extensions):
            raise forms.ValidationError('图片格式错误')
        return file

    def clean(self):
        self.task = CashbackTask.objects.filter(id=self.cleaned_data.get('id'))
        if not self.task:
            raise forms.ValidationError('活动不存在')
        self.task = self.task[0]

        #商家
        seller=AuthUser.objects.get(id=self.task.seller_id)

        orderno = self.cleaned_data.get('orderno')
        self.order = Order.objects.filter(id=orderno, seller_id=seller.id)
        if not self.order:
            raise forms.ValidationError('错误的订单号')
        self.order = self.order[0]

        cashback = Cashback.objects.filter(seller_id=seller.id)
        if cashback.filter(orderno=orderno).count() > 0:
            raise forms.ValidationError('请勿重复提交')

        # 限制领取时间
        if seller.task_interval > 0:
            start = datetime.now() - timedelta(days=seller.task_interval)
            if cashback.filter(customer_id=self.order.customer_id, add_time__gte=start).count() > 0:
                raise forms.ValidationError('在{0}天内已有领取'.format(seller.task_interval))

        wechat = self.cleaned_data.get('wechat')
        alipay = self.cleaned_data.get('alipay')

        if not wechat and not alipay:
            raise forms.ValidationError('请填写微信号或者支付宝账号')


def check_file_extension(memory_file, extensions=None):
    extension = os.path.splitext(memory_file.name)[1].lower()
    if extension not in extensions:
        return False
    return True
