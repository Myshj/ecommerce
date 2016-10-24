from django.shortcuts import render, Http404
from django.db.models import Q

# Create your views here.

from marketing.forms import EmailForm
from marketing.models import MarketingMessage, Slider

from .models import Product, ProductImage, Category

from django.core.cache import caches

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}



    return render(request, template, context)


def home(request):
    sliders = Slider.objects.all_featured()
    products = Product.objects.all()
    template = 'products/home.html'
    context = {
        "products": products,
        "sliders": sliders,
    }
    return render(request, template, context)


def all(request):
    print("/////////////////////////////////////////////////")
    print(caches['default'])
    print("/////////////////////////////////////////////////")

    categories = Category.objects.all()

    if request.method == 'POST':
        checked_categories = []
        for key in request.POST.keys():
            try:
                checked_categories.append(int(key))
            except:
                pass
    else:
        checked_categories = [category.pk for category in categories]

    categories_to_display = Category.objects.filter(pk__in=checked_categories)
    products = Product.objects.filter(category__in=categories_to_display)

    if request.POST.get('lowerPrice', default='') != '':
        products = products.filter(price__gte=request.POST.get('lowerPrice'))

    if request.POST.get('upperPrice', default='') != '':
        products = products.filter(price__lte=request.POST.get('upperPrice'))

    context = {'products': products,
               'categories': categories,
               'checked_categories': checked_categories,
               'lowerPrice': request.POST.get('lowerPrice', default=''),
               'upperPrice': request.POST.get('upperPrice', default='')}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        # images = product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        context = {'product': product, "images": images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404
