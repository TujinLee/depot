# -*- coding: utf8 -*-
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from models import *
from forms import *

def create_product(request):
    form = ProductForm(request.POST or None) # 创建一个表单对象，以请求对象或空填充
    if form.is_valid(): # 验证表单是否合法
        form.save() # 表单写入数据库
        form = ProductForm() # 重置表单为空
    t = get_template('depotapp/create_product.html') # 渲染模版
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_product(request):
    list_items = Product.objects.all() # 获取产品列表
    paginator = Paginator(list_items ,10) # 设置一个分页对象
    try:
        page = int(request.GET.get('page', '1')) # 获取页数，异常时默认为第1页
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page) # 获取某页产品列表
    except :
        list_items = paginator.page(paginator.num_pages) # 页面太大等异常时获取最后一页
    t = get_template('depotapp/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def view_product(request, id):
    product_instance = Product.objects.get(id = id) # 获取某个产品对象
    t=get_template('depotapp/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):
    product_instance = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance = product_instance) # 创建一个表单对象，以产品对象填充
    if form.is_valid():
        form.save()
    t=get_template('depotapp/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
