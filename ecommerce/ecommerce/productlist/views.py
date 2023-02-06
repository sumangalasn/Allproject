from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import ProductList


def testing(request):
    mydata = ProductList.objects.all().values()
    template = loader.get_template('productlist/index.html')
    context = {
        'byproductlist': mydata,
    }
    return HttpResponse(template.render(context, request))
