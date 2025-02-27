from django.urls import path
from . import views

urlpatterns = [

    path('stocks/', views.StockListCreateView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', views.StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),

   

    path('', views.stock_list, name='stock-list'),
    path('<int:pk>/', views.stock_detail, name='stock-detail'),
    path('create/', views.stock_create, name='stock-create'),
    path('<int:pk>/update/', views.stock_update, name='stock-update'),
    path('<int:pk>/delete/', views.stock_delete, name='stock-delete'),

    path('check_stock_alerts_task/', views.check_stock_alerts_task, name='check_stock_alerts_task')


]


