
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .serializers import StockSerializer
from .utils import get_stock_price
from .forms import StockForm

from rest_framework import generics


# List and Create Stocks
class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# Retrieve, Update, Delete a Stock
class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


def stock_list(request):
    stocks = Stock.objects.all()
    for stock in stocks:
        stock.price = get_stock_price(stock.symbol)
        stock.save()
    return render(request, 'stock_list.html', {'stocks': stocks})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock_detail.html', {'stock': stock})

def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock-list')
    else:
        form = StockForm()
    return render(request, 'stock_form.html', {'form': form})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock-list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock_form.html', {'form': form})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('stock-list')


from .task import check_stock_alerts
from django.http import HttpResponse
from celery import shared_task

@shared_task
def check_stock_alerts_task(request):
    alert=check_stock_alerts()
    if alert:
        return HttpResponse("mail is send successfully......")
    else:
        return HttpResponse("stocks price is not increase....")
