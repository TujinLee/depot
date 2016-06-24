from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from forms import *


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('depotapp/create_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def list_product(request):
    list_items = Product.objects.all()
    paginator = Paginator(list_items, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except EmptyPage:
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def view_product(request, id):
    product_instance = Product.objects.get(id=id)

    t = get_template('depotapp/view_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def edit_product(request, id):
    product_instance = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product_instance)
    if form.is_valid():
        form.save()

    t = get_template('depotapp/edit_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
