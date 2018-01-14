# response

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# class-based views

from django.views.generic import View

# models
from .models import Country, City

# Create your views here.

class CreatePage(View):
    template_country = 'page/country.html'
    template_city = 'page/city.html'
    def get(self, request, *a, **kw):
        field = kw.get('field')
        if field == 'city':
            return render(request, self.template_city)
        else:
            return render(request, self.template_country)


    def post(self, request, *a, **kw):
        field = kw.get('field')
        if field == 'country':
            name_ascii = request.POST.get('name')
            name_unicode = request.POST.get('name1')
            country_code = request.POST.get('code')
            if name_ascii and name_unicode and country_code:
                Country.objects.create(name_ascii = name_ascii, name_unicode = name_unicode, country_code = country_code)
                return HttpResponse('success')
            else:
                return HttpResponse('error')
        if field == 'city':
            name_ascii = request.POST.get('name')
            name_unicode = request.POST.get('name1')
            city_code = request.POST.get('code')
            country_code = request.POST.get('code1')
            if name_ascii and name_unicode and city_code and country_code:
                country = Country.objects.get(country_code__exact = country_code)
                City.objects.create(country = country, name_ascii = name_ascii, name_unicode = name_unicode, city_code = city_code)
                return HttpResponse('success')
            else:
                return HttpResponse('error')

