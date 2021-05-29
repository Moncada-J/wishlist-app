from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Item
# Create your views here.


def items_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = ''
