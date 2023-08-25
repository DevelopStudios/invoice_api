from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('api/invoices', views.invoice_list),
    path('api/statuses', views.status_list),
    path('api/payment_terms', views.payment_terms),
    path('api/invoices/<str:id>/', views.invoice_detail),
    path('api/items', views.item_list),
    path('api/items/<str:id>/', views.item_detail)
]