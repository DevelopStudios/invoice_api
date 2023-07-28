from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('invoices', views.invoice_list),
    path('statuses', views.status_list),
    path('items', views.item_list),
    path('payment_terms', views.payment_terms),
    path('invoices/<str:id>/', views.invoice_detail),
]