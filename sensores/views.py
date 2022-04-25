from django.shortcuts import render
from django.views.generic import TemplateView, ListView #,DetailView
from pprint import pprint

from .models import Bmp280, Dht11

# class Dht11ListView(ListView):
#     model = Dht11

# class IndexListView(ListView):
#     model = Dht11
#     # model = Bmp280

class MultipleModelView(TemplateView):
    template_name='sensores/bmp280_list.html'
    
    def get_context_data(self, **kwargs):
         context = super(MultipleModelView, self).get_context_data(**kwargs)
         context['dht11'] = Dht11.objects.all()
         context['bmp280'] = Bmp280.objects.all()
        #  return pprint(context['bmp280'][0].temperatura)
         return context

# class Dht11DetailView(DetailView):
#     model = Dht11

def teste(request):
    dht11 = Dht11.objects.all()
    bmp280 = Bmp280.objects.all()
    return render(request, 'sensores/bmp280_list.html', {'dht11s': dht11, 'bmp280s': bmp280})