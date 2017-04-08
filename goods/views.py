import json

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.base import View

from libs.common.form import invalid_msg
from libs.common.helper import save_file
from libs.utils.http import JSONResponse
from libs.utils.response import paged_result
from .models import Shop, Goods
from .forms import GoodsForm, ShopForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopManagerViews(LoginRequiredMixin, View):
    template_name = 'goods/shop/index.html'

    def get(self, request, *args, **kwargs):
        form = ShopForm()
        return render(request, self.template_name, {'form': form})


class ShopCreateView(View):
    template_name = 'goods/shop/add.html'

    def get(self, request, *args, **kwargs):
        form = ShopForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ShopForm(request.POST)
        if not form.is_valid():
            errors = {key: invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        shop = form.save(commit=False)
        shop.seller_id = request.user.id
        shop.save()

        return redirect('goods:shop_index')


class ShopEditView(View):
    template_name = 'goods/shop/edit.html'

    def get(self, request, *args, **kwargs):
        shop_id = request.GET.get('id')
        shop = get_object_or_404(Shop, id=shop_id)
        form = ShopForm(instance=shop)
        return render(request, self.template_name, {'form': form, 'id': shop_id})

    def post(self, request, *args, **kwargs):
        shop_id = request.POST.get('id')
        shop = get_object_or_404(Shop, id=shop_id)
        form = ShopForm(request.POST, instance=shop)
        if not form.is_valid():
            errors = {key: invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        form.save()

        return redirect('goods:shop_index')


def get_shops(request):
    ''' 获取店铺列表 '''

    page = int(request.GET.get('page', 1))
    pagesize = int(request.GET.get('rows', 15))
    keyword = request.GET.get('keywords')

    shops = Shop.objects.filter(seller_id=request.user.id)
    if keyword:
        shops = shops.filter(shopname__contains=keyword)  # 按店铺名称查询
    count = shops.count()  # 总数
    shops = shops.order_by('-add_time')[(page - 1) * pagesize:page * pagesize]
    result = [item.to_dict() for item in list(shops)]

    paged_result.set(page, pagesize, count, result)

    return JsonResponse(paged_result.to_dict())


@csrf_exempt
@require_http_methods(['POST'])
def delete_shops(request):
    try:
        data = json.loads(request.body.decode())
        shop_ids = data.get('ids')

        with transaction.atomic():
            # 删除商品
            Goods.objects.filter(shop_id__in=shop_ids).delete()
            # 删除店铺
            Shop.objects.filter(id__in=shop_ids).delete()
    except Exception as e:
        return JSONResponse(msg='删除失败！')
    return JSONResponse()


class GoodsManagerView(View):
    template_name = 'goods/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class GoodsCreateView(LoginRequiredMixin, View):
    '''新增商品'''
    template_name = 'goods/add.html'

    def get(self, request, *args, **kwargs):
        shops = Shop.objects.filter(seller_id=request.user.id)
        form = GoodsForm(initial={'shop': shops})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = GoodsForm(request.POST, request.FILES)
        if not form.is_valid():
            errors = {key: invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        goods = form.save(commit=False)
        goods.seller_id = request.user.id
        goods.save()

        return redirect('goods:index')


class GoodsEditView(View):
    template_name = 'goods/edit.html'

    def get(self, request, *args, **kwargs):
        goods_id = request.GET.get('id')
        goods = get_object_or_404(Goods, id=goods_id)
        form = GoodsForm(instance=goods)
        return render(request, self.template_name, {'form': form, 'model': goods})

    def post(self, request, *args, **kwargs):
        goods_id = request.POST.get('id')
        goods = get_object_or_404(Goods, id=goods_id)
        form = GoodsForm(request.POST, request.FILES, instance=goods)
        if not form.is_valid():
            errors = {key: invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        form.save()

        return redirect('goods:index')


@csrf_exempt
@require_http_methods(['POST'])
def delete_goods(request):
    try:
        data = json.loads(request.body.decode())
        goods_ids = data.get('ids')
        # 删除商品
        Goods.objects.filter(id__in=goods_ids).delete()
    except Exception as e:
        return JSONResponse(msg='删除失败！')
    return JSONResponse()


def get_goods(request):
    ''' 获取商品表 '''

    page = int(request.GET.get('page', 1))
    pagesize = int(request.GET.get('rows', 15))
    keyword = request.GET.get('keywords')

    goods = Goods.objects.filter(seller_id=request.user.id)
    if keyword:
        goods = goods.filter(name__contains=keyword)  # 按商品名称查询
    count = goods.count()  # 总数
    goods = goods.order_by('-add_time')[(page - 1) * pagesize:page * pagesize]
    result = [item.to_dict() for item in list(goods)]

    paged_result.set(page, pagesize, count, result)

    return JsonResponse(paged_result.to_dict())
