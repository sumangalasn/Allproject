from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import LoginformList


def testing(request):
    mydata = LoginformList.objects.all().values()
    template = loader.get_template('loginformlist/index.html')
    context = {
        'byloginformlist': mydata,
    }
    return HttpResponse(template.render(context, request))
