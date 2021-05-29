from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Item
from .forms import ItemForm
# Create your views here.


def items_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'


# def add_item(request):
#  if request.method == 'POST':
#      form = ItemForm(request.POST)
#      if form.is_valid():
#          return HttpResponseRedirect('/')
#      else:
#         form = ItemForm()
#         return render(request, 'add.html', {'form': form})
