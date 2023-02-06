from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from productlist.models import ProductList


def details(request, id):
    mydata = ProductList.objects.get(id=id)
    template = loader.get_template('productdetails/index.html')
    context = {
        'details': mydata,
    }
    return HttpResponse(template.render(context, request))
