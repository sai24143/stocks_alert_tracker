from rest_framework import serializers
from .models import Stock
from .utils import get_stock_price  # Import utility function

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol', 'name']

    def create(self, validated_data):
        """Fetch stock price before saving"""
        stock = Stock(**validated_data)
        stock.price = get_stock_price(stock.symbol)  # Get price from yfinance
        stock.save()
        return stock

    def update(self, instance, validated_data):
        """Update stock price when modifying"""
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.name = validated_data.get('name', instance.name)
        instance.price = get_stock_price(instance.symbol)  # Fetch updated price
        instance.save()
        return instance
