from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
  products = Product.objects.all().order_by('name')
  context = {"products": products}
  response = render(request, "products/index.html", context)
  return response

def show(request, product_id):
  p = get_object_or_404(Product, pk=product_id)
  context={'p':p}
  response = render(request, 'products/show.html', context)
  return response

