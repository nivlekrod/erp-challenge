from django.urls import path
from principal import consumers

urlrouter = [path('sale_channel/', consumers.SaleConsumer.as_asgi())]
