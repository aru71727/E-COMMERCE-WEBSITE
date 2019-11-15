
from .models import Offers
from .models import Product
from django.shortcuts import render

# Create your views here.
def index(request):
    offers = Offers.objects.all()
    products = Product.objects.all()
    nslides = len(offers)
    n = len(products)
    params = {'range': range(1,nslides),'offer': offers,'product': products}
    return render(request, 'myapp/homepage.html', params)

def deals(request):
	products = Product.objects.all()
	params = {'product': products}
	return render(request, 'myapp/deals.html', params)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'myapp/prodView.html', {'product':product[0]})

