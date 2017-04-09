from django import forms

from apps.orders.models import PLATFORM
from libs.common.helper import save_file
from .models import Shop, Goods


class ShopForm(forms.ModelForm):
    attrs = {
        'class': 'form-control',
    }

    shopname = forms.CharField(widget=forms.TextInput(attrs=attrs), max_length=50)
    shopkeepername = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False, max_length=50)
    platform = forms.ChoiceField(widget=forms.Select(attrs=attrs), choices=PLATFORM)

    class Meta:
        model = Shop
        fields = ['shopname', 'shopkeepername', 'platform']


class GoodsForm(forms.ModelForm):
    attrs = {
        'class': 'form-control',
    }

    name = forms.CharField(widget=forms.TextInput(attrs=attrs), max_length=50)
    # shop = forms.ChoiceField(widget=forms.TextInput(attrs=attrs))
    pgoods_id = forms.IntegerField(widget=forms.NumberInput(attrs=attrs))
    platform = forms.ChoiceField(widget=forms.Select(attrs=attrs), choices=PLATFORM)
    price1 = forms.FloatField(widget=forms.TextInput(attrs=attrs))
    image1 = forms.FileField(required=False)
    image2 = forms.FileField(required=False)
    image3 = forms.FileField(required=False)
    image1url = forms.CharField(required=False)
    image2url = forms.CharField(required=False)
    image3url = forms.CharField(required=False)
    keyword1 = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False, max_length=200)
    keyword2 = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False, max_length=200)
    keyword3 = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False, max_length=200)
    remark = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False, max_length=200)

    class Meta:
        model = Goods
        fields = ['name', 'pgoods_id', 'shop', 'platform', 'price1', 'keyword1', 'remark']
        widgets = {
            'shop': forms.Select(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        data = self.cleaned_data
        image1 = data.get('image1')
        image2 = data.get('image2')
        image3 = data.get('image3')
        image1url = data.get('image1url')
        image2url = data.get('image2url')
        image3url = data.get('image3url')

        self.instance.image1 = save_image(image1, image1url)
        self.instance.image2 = save_image(image2, image2url)
        self.instance.image3 = save_image(image3, image3url)

        return super(GoodsForm, self).save(commit)


def save_image(image_file, old_image_filename):
    if image_file:
        return save_file(image_file)  # 上传图片
    if not old_image_filename:  # 删除图片
        return ''
    return old_image_filename  # 无修改
